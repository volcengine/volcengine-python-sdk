"""
信封加密算法.
"""

__all__ = [
    "ClientSessionKey",
    "EncryptedMessage",
    "ResponseKey",
    "ServerSessionKey",
]

import base64
import dataclasses
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from io import BytesIO
from threading import Lock

from typing_extensions import IO, TYPE_CHECKING, Optional, Self, Set, Tuple, Union

if TYPE_CHECKING:
    from _typeshed import GenericPath
else:
    GenericPath = str


from .. import error
from .aes import AES_KEY_LEN, AES_MAC_LEN, AES_NONCE_LEN, AesKey, FileMode
from .rsa import PrivateKey, PublicKey

logger = logging.getLogger(__name__)


@dataclass(eq=False, frozen=True)
class EncryptedMessage:
    """
    信封加密数据.
    可作为数据发送方的请求, 及数据接收方的响应.

    本类不含可变状态, 所有方法是线程安全的.
    """

    nonce: bytes
    """单次随机数."""

    mac: bytes
    """校验码."""

    key: Optional[bytes] = None
    """
    用公钥加密的对称密钥.
    在数据发送方的加密请求中使用, 在数据接收方的加密响应中为空.
    """

    ciphertext: Optional[bytes] = None
    """
    加密数据.
    在字符串 / 二进制数据加密中使用, 在文件加密中为空.
    """

    def serialize(self) -> str:
        """
        将消息序列化为字符串.
        """
        return json.dumps(
            {
                k: base64.b64encode(v).decode()
                for k, v in self.__dict__.items()
                if v is not None
            },
            separators=(",", ":"),
        )

    @classmethod
    def deserialize(cls, data: Union[str, bytes]) -> Self:
        """
        从字符串反序列化消息.
        """
        try:
            return cls(**{k: base64.b64decode(v) for k, v in json.loads(data).items()})
        except Exception:
            raise error.DecryptionError("Invalid encoding") from None


@dataclass(eq=False, frozen=True)
class ResponseKey:
    """
    对响应加解密的密钥.

    本类不含可变状态, 所有方法是线程安全的.
    """

    _key: AesKey

    def encrypt(self, plaintext: Union[str, bytes]) -> str:
        """
        加密响应 (由服务端使用).
        """
        if isinstance(plaintext, str):
            plaintext = plaintext.encode("utf-8")

        nonce, ciphertext, mac = self._key.encrypt(plaintext)
        return EncryptedMessage(nonce=nonce, mac=mac, ciphertext=ciphertext).serialize()

    def decrypt(self, response: Union[str, bytes]) -> bytes:
        """
        解密响应 (由客户端使用).
        """
        message = EncryptedMessage.deserialize(response)

        if message.ciphertext is None or message.key is not None:
            raise error.ParamError("response", "Message is not server response")
        if len(message.nonce) != AES_NONCE_LEN or len(message.mac) != AES_MAC_LEN:
            raise error.DecryptionError("Invalid data length")

        return self._key.decrypt(message.nonce, message.ciphertext, message.mac)

    def encrypt_file(
        self,
        source_path: GenericPath,
        dest_path: GenericPath,
        mode: FileMode,
        nonce: Optional[bytes] = None,
    ) -> str:
        """
        加密响应文件 (由服务端使用).
        """
        with open(source_path, f"r{mode}") as source, open(
            dest_path, f"w{mode}"
        ) as dest:
            nonce, mac = self._key.encrypt_stream(source, dest, mode, nonce)

            metadata = EncryptedMessage(nonce=nonce, mac=mac)

            return metadata.serialize()

    def decrypt_file(
        self,
        metadata: str,
        source_path: GenericPath,
        dest_path: GenericPath,
        mode: FileMode,
    ):
        """
        解密响应文件 (由客户端使用).
        """
        message = EncryptedMessage.deserialize(metadata)

        if message.ciphertext is not None or message.key is not None:
            raise error.ParamError("response", "Message is not server response")
        if len(message.nonce) != AES_NONCE_LEN or len(message.mac) != AES_MAC_LEN:
            raise error.DecryptionError("Invalid data length")

        return self.decrypt_file_with_nonce(
            source_path, dest_path, message.nonce, message.mac, mode
        )

    def decrypt_file_with_nonce(
        self,
        source_path: GenericPath,
        dest_path: GenericPath,
        nonce: bytes,
        mac: Optional[bytes],
        mode: FileMode,
    ):
        """
        解密响应文件 (由客户端使用).
        """
        with open(source_path, f"r{mode}") as source, open(
            dest_path, f"w{mode}"
        ) as dest:
            self._key.decrypt_stream(source, dest, nonce, mac, mode)


@dataclass(eq=False, frozen=True)
class ClientSessionKey:
    """
    数据发送方持有的密钥.

    本类不含可变状态, 所有方法是线程安全的.
    """

    server_public_key: PublicKey
    """数据接收方公钥."""

    @classmethod
    def load(cls, public_pem: Union[str, bytes]) -> Self:
        """
        通过数据接收方的公钥产生发送方密钥.

        Args:
            private_pem: PEM 格式的 RSA 公钥.
        """
        public_key = PublicKey.from_public_pem(public_pem)

        return cls(public_key)

    def encrypt(
        self, plaintext: Union[str, bytes], key: Optional[AesKey] = None
    ) -> EncryptedMessage:
        """
        信封加密.

        Args:
            key: 指定加密用的对称密钥. 默认为随机生成 (一次一密).
        Returns:
            信封加密数据.
        """
        if isinstance(plaintext, str):
            plaintext = plaintext.encode("utf-8")

        with BytesIO(plaintext) as source, BytesIO() as dest:
            message = self.encrypt_stream(source, dest, "b", key)
            message = dataclasses.replace(message, ciphertext=dest.getvalue())

        return message

    def encrypt_with_response(
        self, plaintext: Union[str, bytes]
    ) -> Tuple[EncryptedMessage, ResponseKey]:
        """
        信封加密, 并获取用于解密响应的密钥.
        """
        key = AesKey.generate()

        return self.encrypt(plaintext, key), ResponseKey(key)

    def encrypt_stream(
        self, source: IO, dest: IO, mode: FileMode, key: Optional[AesKey] = None
    ) -> EncryptedMessage:
        """
        信封加密数据流.

        Returns:
            信封加密元数据.
        """
        symmetric_key = key or AesKey.generate()

        nonce, mac = symmetric_key.encrypt_stream(source, dest, mode)

        encrypted_key = self.server_public_key.encrypt(symmetric_key.key)

        return EncryptedMessage(key=encrypted_key, nonce=nonce, mac=mac)

    def encrypt_stream_with_response(
        self, source: IO, dest: IO, mode: FileMode
    ) -> Tuple[EncryptedMessage, ResponseKey]:
        """
        信封加密数据流, 并获取用于解密响应的密钥.
        """
        key = AesKey.generate()

        return self.encrypt_stream(source, dest, mode, key), ResponseKey(key)


@dataclass(eq=False)
class ServerSessionKey:
    """
    数据接收方持有的密钥.

    本类的所有方法是线程安全的.
    """

    private_key: PrivateKey
    """私钥."""

    expire_at: datetime
    """【未启用】密钥对在此时间后无效."""

    tks_version: Optional[int]
    """【未启用】密钥版本, 用于判断获取的密钥是否变化. """

    pem_md5: Optional[str] = None
    """pem的MD5值."""

    used_nonce: Set[bytes] = field(default_factory=set)
    """已使用的单次随机数列表."""

    used_nonce_lock: Lock = field(init=False, default_factory=Lock)
    """线程安全: 修改 used_nonce 应该加锁."""

    @classmethod
    def load(
        cls,
        private_pem: Union[str, bytes],
        expire_at: datetime,
        tks_version: Optional[int],
        pem_md5: Optional[str],
    ) -> Self:
        """
        通过 PEM 格式的 RSA 私钥产生接收方密钥.

        Args:
            private_pem: PEM 格式的 RSA 私钥.
            :param pem_md5:
            :param private_pem:
            :param expire_at:
            :param tks_version:
        """
        private_key = PrivateKey.from_private_pem(private_pem)

        return cls(private_key, expire_at, tks_version, pem_md5)

    @classmethod
    def generate(cls, expire_at: datetime) -> Self:
        """
        随机生成接收方密钥.
        """
        private_key = PrivateKey.generate()

        return cls(private_key, expire_at, tks_version=None, pem_md5=None)

    def is_expired(self) -> bool:
        """
        是否已超过有效期.
        """
        now = datetime.now(timezone.utc)
        if now > self.expire_at:
            logger.warning("session key maybe expired")

        return False  # 服务端密钥暂时不考虑有效期

    def get_public_key(self) -> str:
        """
        获取 PEM 格式的公钥.
        """
        return self.private_key.public_pem()

    def decrypt(
        self, message: Union[str, bytes, EncryptedMessage]
    ) -> Tuple[bytes, ResponseKey]:
        """
        信封解密.

        Returns:
            明文数据, 及用于加密响应的密钥.

        Raises:
            DecryptionError: 加密消息不合法, 或者加密使用的密钥不是本密钥.
        """
        if isinstance(message, (str, bytes)):
            message = EncryptedMessage.deserialize(message)
        if message.ciphertext is None:
            raise error.ParamError("message", "Message has no data")

        with BytesIO(message.ciphertext) as source, BytesIO() as dest:
            response_key = self.decrypt_stream(message, source, dest, "b")
            plaintext = dest.getvalue()

        return plaintext, response_key

    def decrypt_stream(
        self,
        metadata: Union[str, bytes, EncryptedMessage],
        source: IO,
        dest: IO,
        mode: FileMode,
    ) -> ResponseKey:
        """
        信封解密数据流.

        Returns:
            用于加密响应的密钥.

        Raises:
            DecryptionError: 加密消息不合法, 或者加密使用的密钥不是本密钥.
        """
        if isinstance(metadata, (str, bytes)):
            metadata = EncryptedMessage.deserialize(metadata)
        if metadata.key is None:
            raise error.ParamError("metadata", "Message has no key")

        # with self.used_nonce_lock:
        #     if metadata.nonce in self.used_nonce:
        #         raise error.NonceReusedError()
        #     self.used_nonce.add(metadata.nonce)

        symmetric_key = self.private_key.decrypt(metadata.key)
        if (
            len(symmetric_key) != AES_KEY_LEN
            or len(metadata.nonce) != AES_NONCE_LEN
            or len(metadata.mac) != AES_MAC_LEN
        ):
            raise error.DecryptionError("Invalid data length")

        symmetric_key = AesKey(symmetric_key)
        symmetric_key.decrypt_stream(source, dest, metadata.nonce, metadata.mac, mode)

        return ResponseKey(symmetric_key)
