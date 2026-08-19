"""
Merkle Tree Module
Builds and verifies an append-only Merkle tree with SHA-256.
Used for clean-room archival data ingestion integrity.
"""

from hashlib import sha256
from typing import List, Optional


def _hash(data: bytes) -> bytes:
    return sha256(data).digest()


class MerkleTree:
    """Simple binary Merkle tree for integrity verification."""

    def __init__(self, seed: Optional[bytes] = None):
        self.leaves: List[bytes] = []
        if seed is not None:
            self.add_leaf(seed)

    def add_leaf(self, data: bytes) -> None:
        """Add a new leaf (hashed)."""
        self.leaves.append(_hash(data))

    def compute_root(self) -> str:
        """
        Compute the Merkle root as a hex string.
        Standard binary tree: concatenate and hash pairs bottom-up.
        """
        if not self.leaves:
            return ""

        level = list(self.leaves)
        while len(level) > 1:
            next_level = []
            for i in range(0, len(level), 2):
                left = level[i]
                right = level[i + 1] if i + 1 < len(level) else left
                next_level.append(_hash(left + right))
            level = next_level
        return level[0].hex()

    def verify_inclusion(self, data: bytes, proof: List[bytes], root: str) -> bool:
        """Basic inclusion proof verification (simplified)."""
        current = _hash(data)
        for sibling in proof:
            # Order depends on position; simplified for demo
            current = _hash(current + sibling)
        return current.hex() == root
