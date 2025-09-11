
# Copyright (c) [2025] [OpenAI]
# Copyright (c) [2025] [ByteDance Ltd. and/or its affiliates.]
# SPDX-License-Identifier: Apache-2.0
#
# This file has been modified by [ByteDance Ltd. and/or its affiliates.] on 2025.7
#
# Original file was released under Apache License Version 2.0, with the full license text
# available at https://github.com/openai/openai-python/blob/main/LICENSE.
#
# This modified file is released under the same license.

from __future__ import annotations

import base64
from typing import Tuple


def aes_gcm_encrypt_bytes(
    key: bytes, iv: bytes, plain_bytes: bytes, associated_data: bytes = b""
) -> bytes:
    # aes_gcm_encrypt_bytes encrypt message using AES-GCM
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
    ).encryptor()
    # associated_data will be authenticated but not encrypted,
    # it must also be passed in on decryption.
    encryptor.authenticate_additional_data(associated_data)
    # Encrypt the plaintext and get the associated ciphertext.
    # GCM does not require padding.
    ciphertext = encryptor.update(plain_bytes) + encryptor.finalize()
    return ciphertext + encryptor.tag


def aes_gcm_encrypt_base64_string(key: bytes, nonce: bytes, plaintext: str) -> str:
    """aes_gcm_encrypt_base64_string Encrypt message from base64 string to string using AES-GCM"""
    plain_bytes = plaintext.encode()
    # Encrypt message to string using AES-GCM
    c = aes_gcm_encrypt_bytes(key, nonce, plain_bytes)
    return base64.b64encode(c).decode()


def aes_gcm_decrypt_bytes(
    key: bytes, iv: bytes, cipher_bytes: bytes, associated_data: bytes = b""
) -> bytes:
    """aes_gcm_decrypt_bytes Decrypt message from bytes to bytes using AES-GCM"""
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

    tag_length = 16  # default aes gcm tag length
    cipher = cipher_bytes[:-tag_length]
    tag = cipher_bytes[-tag_length:]
    # Construct a Cipher object, with the key, iv, and additionally the
    # GCM tag used for authenticating the message.
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
    ).decryptor()
    # We put associated_data back in or the tag will fail to verify
    # when we finalize the decryptor.
    decryptor.authenticate_additional_data(associated_data)
    # Decryption gets us the authenticated plaintext.
    # If the tag does not match an InvalidTag exception will be raised.
    return decryptor.update(cipher) + decryptor.finalize()


def aes_gcm_decrypt_base64_string(key: bytes, nonce: bytes, ciphertext: str) -> str:
    # Decrypt message(base64.std.string) using AES-GCM
    cipher_bytes = base64.decodebytes(ciphertext.encode())
    return aes_gcm_decrypt_bytes(key, nonce, cipher_bytes).decode()


def marshal_cryptography_pub_key(key) -> bytes:
    # python version of crypto/elliptic/elliptic.go Marshal
    # without point on curve check
    return bytes([4]) + key.x.to_bytes(32, "big") + key.y.to_bytes(32, "big")


class key_agreement_client:
    def __init__(self, certificate_pem_string: str) -> None:
        """Load cert and extract public key"""
        __fixed_version__ = "42.0.0"  # version check
        from cryptography import __version__

        if __version__ < __fixed_version__:
            raise Exception(
                "The cryptography package of Ark SDK only supports versions after {}, "
                'please install the cryptography package by using pip install "cryptography>={}"'.format(
                    __fixed_version__, __fixed_version__
                )
            )
        from cryptography import x509
        from cryptography.hazmat.primitives.asymmetric import ec

        pem_data = certificate_pem_string.encode()
        self._cert = x509.load_pem_x509_certificate(pem_data)
        cert_pub = self._cert.public_key().public_numbers()
        self._curve = ec._CURVE_TYPES[self._cert.public_key().curve.name]
        self._public_key = ec.EllipticCurvePublicNumbers(
            cert_pub.x, cert_pub.y, self._curve
        ).public_key()

    def encrypt_string(self, plaintext: str) -> Tuple[bytes, bytes, str, str]:
        """encrypt_string encrypt plaintext with ECIES DH protocol"""
        key, nonce, token = self.generate_ecies_key_pair()
        # Encrypt message using AES-GCM
        ciphertext = aes_gcm_encrypt_base64_string(key, nonce, plaintext)
        return key, nonce, token, ciphertext

    def encrypt_string_with_key(self, key: bytes, nonce: bytes, plaintext: str) -> str:
        """encrypt_string_with_key encrypt plaintext with ECIES DH protocol"""
        # Encrypt message using AES-GCM
        ciphertext = aes_gcm_encrypt_base64_string(key, nonce, plaintext)
        return ciphertext

    def decrypt_string_with_key(self, key: bytes, nonce: bytes, ciphertext: str) -> str:
        """decrypt_string_with_key decrypt ciphertext with ECIES DH protocol"""
        # Decrypt message using AES-GCM
        return aes_gcm_decrypt_base64_string(key, nonce, ciphertext)

    def generate_ecies_key_pair(self) -> Tuple[bytes, bytes, str]:
        """generate_ecies_key_pair generate ECIES key pair"""
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.hkdf import HKDF
        from cryptography.hazmat.primitives.asymmetric import ec

        # Generate an ephemeral elliptic curve scalar and point
        peer_private_key = ec.generate_private_key(self._curve)
        dh = peer_private_key.exchange(ec.ECDH(), self._public_key)
        R = peer_private_key.public_key().public_numbers()

        # Derive symmetric key and nonce via HKDF
        length = 32 + 12
        buf = HKDF(
            algorithm=hashes.SHA256(),
            length=length,
            salt=None,
            info=None,
        ).derive(dh)
        key = buf[:32]
        nonce = buf[32:length]

        token = marshal_cryptography_pub_key(R)
        return key, nonce, base64.b64encode(token).decode()
