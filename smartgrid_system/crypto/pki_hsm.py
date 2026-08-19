"""
PKI / HSM interface stubs.
Uses cryptography library for X.509 when available.
HSM operations are stubs (PKCS#11 or CloudHSM in production).
"""

from typing import List, Optional, Any


class CertChain:
    def __init__(self, certs: List[Any]):
        self.certs = certs


def load_cert_chain(chain_paths: List[str]) -> CertChain:
    """Parse X.509 chain from PEM files. Stub returns empty chain."""
    return CertChain([])


def verify_certificate(cert: Any, ca_store: Any) -> bool:
    """Verify signature and expiration. Stub always True for demo."""
    return True


def hsm_sign(data: bytes) -> bytes:
    """
    Stub: calls real HSM API (PKCS#11 or REST) if available.
    For demo, returns SHA-256 of data (NOT a real signature).
    """
    from hashlib import sha256
    return sha256(data).digest()
