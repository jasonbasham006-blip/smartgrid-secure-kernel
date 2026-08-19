"""
Post-Quantum Crypto placeholders for NIST ML-KEM (FIPS 203) and ML-DSA (FIPS 204).
Stubs only; replace with approved library implementations when available.
"""

from typing import Tuple, Any


def encapsulate(public_key: Any) -> Tuple[bytes, bytes]:
    """
    ML-KEM encapsulate.
    Returns (ciphertext, shared_key).
    Stub returns dummy values.
    """
    return b"dummy-ciphertext", b"dummy-shared-key-32bytes!!!!!!!"


def decapsulate(ciphertext: bytes, private_key: Any) -> bytes:
    """ML-KEM decapsulate. Stub returns dummy shared key."""
    return b"dummy-shared-key-32bytes!!!!!!!"


def sign_dsa(message: bytes, private_key: Any) -> bytes:
    """ML-DSA sign. Stub returns dummy signature."""
    from hashlib import sha256
    return sha256(message).digest()


def verify_dsa(message: bytes, signature: bytes, public_key: Any) -> bool:
    """ML-DSA verify. Stub always returns True for demo."""
    return True
