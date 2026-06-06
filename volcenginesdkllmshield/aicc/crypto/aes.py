"""
AES 加密算法.
"""

__all__ = [
    "AES_KEY_LEN",
    "AES_MAC_LEN",
    "AES_NONCE_LEN",
    "AesKey",
    "FileMode",
]

import base64
import secrets
from dataclasses import dataclass
from io import BytesIO

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from typing_extensions import IO, Literal, Optional, Self, Tuple

from .. import error

AES_KEY_LEN = 32

AES_NONCE_LEN = 12

AES_MAC_LEN = 16

CHUNK_SIZE = 1024

FileMode = Literal["b", "t"]
"""
文件加密模式: b 表示二进制, t 表示文本 (按行加密, 加密数据 Base64 编码后按行保存).
"""


@dataclass(eq=False, frozen=True)
class AesKey:
    """
    AES 密钥.

    本类不含可变状态, 所有方法是线程安全的.
    """

    key: bytes

    def __post_init__(self):
        if len(self.key) != AES_KEY_LEN:
            raise error.ParamError("key", "Invalid AES key length")

    @classmethod
    def generate(cls) -> Self:
        """
        生成 AES 密钥.
        """
        key = secrets.token_bytes(AES_KEY_LEN)

        return cls(key)

    def encrypt(
        self,
        plaintext: bytes,
        nonce: Optional[bytes] = None,
    ) -> Tuple[bytes, bytes, bytes]:
        """
        用 AES-GCM 加密数据.

        Returns:
            单次随机数, 密文, 及校验码.

        Raises:
            EncryptionError:
        """
        with BytesIO(plaintext) as source, BytesIO() as dest:
            nonce, mac = self.encrypt_stream(source, dest, "b", nonce)
            ciphertext = dest.getvalue()

        return nonce, ciphertext, mac

    def encrypt_stream(
        self,
        source: IO,
        dest: IO,
        mode: FileMode,
        nonce: Optional[bytes] = None,
    ) -> Tuple[bytes, bytes]:
        """
        用 AES-GCM 加密数据流.

        Returns:
            单次随机数及校验码.

        Raises:
            EncryptionError:
        """
        if nonce is None:
            nonce = secrets.token_bytes(AES_NONCE_LEN)
        elif len(nonce) != AES_NONCE_LEN:
            raise error.ParamError("nonce", "wrong length")

        try:
            aes = Cipher(algorithms.AES(self.key), modes.GCM(nonce)).encryptor()

            if mode == "b":
                source_b: IO[bytes] = source
                dest_b: IO[bytes] = dest
                while plaintext := source_b.read(CHUNK_SIZE):
                    ciphertext = aes.update(plaintext)
                    dest_b.write(ciphertext)
            else:
                source_t: IO[str] = source
                dest_t: IO[str] = dest
                for plaintext in source_t:
                    plaintext = plaintext.rstrip("\n")
                    ciphertext = aes.update(plaintext.encode())
                    dest_t.write(base64.b64encode(ciphertext).decode())
                    dest_t.write("\n")

            ciphertext = aes.finalize()
            mac = aes.tag
        except Exception as e:
            raise error.EncryptionError("AES encryption failed") from e

        return nonce, mac

    def decrypt(self, nonce: bytes, ciphertext: bytes, mac: Optional[bytes]) -> bytes:
        """
        用 AES-GCM 解密并校验数据.

        Raises:
            DecryptionError:
        """
        with BytesIO(ciphertext) as source, BytesIO() as dest:
            self.decrypt_stream(source, dest, nonce, mac, "b")
            plaintext = dest.getvalue()

        return plaintext

    def decrypt_stream(
        self,
        source: IO,
        dest: IO,
        nonce: bytes,
        mac: Optional[bytes],
        mode: FileMode,
    ) -> None:
        """
        用 AES-GCM 解密并校验数据流.

        Raises:
            DecryptionError:
        """
        try:
            aes = Cipher(algorithms.AES(self.key), modes.GCM(nonce)).decryptor()

            if mode == "b":
                source_b: IO[bytes] = source
                dest_b: IO[bytes] = dest
                while ciphertext := source_b.read(CHUNK_SIZE):
                    plaintext = aes.update(ciphertext)
                    dest_b.write(plaintext)
            else:
                source_t: IO[str] = source
                dest_t: IO[str] = dest
                for ciphertext in source_t:
                    ciphertext = ciphertext.rstrip("\n")
                    plaintext = aes.update(base64.b64decode(ciphertext)).decode()
                    dest_t.write(plaintext)
                    dest_t.write("\n")

            if mac is not None:
                aes.finalize_with_tag(mac)
        except Exception as e:
            raise error.DecryptionError("AES decryption failed") from e
