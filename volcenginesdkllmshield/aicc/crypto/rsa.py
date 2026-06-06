"""
RSA 加密和签名算法.
"""

__all__ = ["PublicKey", "PrivateKey"]

from dataclasses import dataclass

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey, RSAPublicKey
from typing_extensions import Self, Union

from .. import error

ENCRYPT_PADDING = padding.OAEP(
    mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None
)
SIGN_PADDING = padding.PSS(
    mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
)
SIGN_HASH = hashes.SHA256()


@dataclass(eq=False, frozen=True)
class PublicKey:
    """
    RSA 公钥.

    本类不含可变状态, 所有方法是线程安全的.
    """

    public_key: RSAPublicKey

    @classmethod
    def from_public_pem(cls, public_pem: Union[str, bytes]) -> Self:
        """
        读取 PEM 格式的 RSA 公钥.

        Args:
            private_pem: PEM 格式的 RSA 公钥.
        """
        if isinstance(public_pem, str):
            public_pem = public_pem.encode("utf-8")
        try:
            public_key = serialization.load_pem_public_key(public_pem)
        except Exception as e:
            raise error.ParamError("public_pem", "Invalid RSA public key") from e
        if not isinstance(public_key, RSAPublicKey):
            raise error.ParamError("public_pem", "Key is not RSA")

        return cls(public_key)

    def encrypt(self, plaintext: bytes) -> bytes:
        """
        RSA 加密.

        Raises:
            EncryptionError:
        """
        try:
            return self.public_key.encrypt(plaintext, ENCRYPT_PADDING)
        except Exception as e:
            raise error.EncryptionError("RSA encryption failed") from e

    def public_pem(self) -> str:
        """
        获取 PEM 格式的公钥.
        """
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode("utf-8")

    def verify(self, signature: bytes, message: Union[str, bytes]) -> bool:
        """
        公钥验签.

        Raises:
            SignatureError:
        """
        if isinstance(message, str):
            message = message.encode("utf-8")
        try:
            self.public_key.verify(signature, message, SIGN_PADDING, SIGN_HASH)
            return True
        except Exception as e:
            print(e)
            return False


@dataclass(init=False, eq=False, frozen=True)
class PrivateKey(PublicKey):
    """
    RSA 密钥对.
    """

    private_key: RSAPrivateKey

    def __init__(self, private_key: RSAPrivateKey):
        # Workaround frozen class
        object.__setattr__(self, "private_key", private_key)
        object.__setattr__(self, "public_key", private_key.public_key())

    @classmethod
    def from_private_pem(cls, private_pem: Union[str, bytes]) -> Self:
        """
        读取 PEM 格式的 RSA 密钥对.

        Args:
            private_pem: PEM 格式的 RSA 私钥.
        """
        if isinstance(private_pem, str):
            private_pem = private_pem.encode("utf-8")
        private_key = serialization.load_pem_private_key(private_pem, password=None)
        if not isinstance(private_key, RSAPrivateKey):
            raise error.ParamError("private_pem", "Key is not RSA")

        return cls(private_key)

    @classmethod
    def generate(cls) -> Self:
        """
        随机生成密钥对.
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=4096)
        return cls(private_key)

    def private_pem(self) -> str:
        """
        获取 PEM 格式的私钥.
        """
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        ).decode("utf-8")

    def decrypt(self, plaintext: bytes) -> bytes:
        """
        RSA 解密.

        Raises:
            DecryptionError:
        """
        try:
            return self.private_key.decrypt(plaintext, ENCRYPT_PADDING)
        except Exception as e:
            raise error.DecryptionError("RSA decryption failed") from e

    def sign(self, message: Union[str, bytes]) -> bytes:
        """
        私钥签名.

        Raises:
            SignatureError:
        """
        if isinstance(message, str):
            message = message.encode("utf-8")
        try:
            signature = self.private_key.sign(message, SIGN_PADDING, SIGN_HASH)
            return signature
        except Exception as e:
            raise error.SignatureError("RSA signing failed") from e
