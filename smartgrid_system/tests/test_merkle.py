"""Unit tests for Merkle tree."""

from smartgrid_system.core.merkle_tree import MerkleTree


def test_empty_root():
    tree = MerkleTree()
    assert tree.compute_root() == ""


def test_single_leaf():
    tree = MerkleTree()
    tree.add_leaf(b"Alice")
    root = tree.compute_root()
    assert len(root) == 64  # SHA-256 hex


def test_multiple_leaves():
    tree = MerkleTree()
    tree.add_leaf(b"Alice")
    tree.add_leaf(b"Bob")
    tree.add_leaf(b"Carol")
    root = tree.compute_root()
    assert isinstance(root, str) and len(root) == 64


def test_deterministic_root():
    tree1 = MerkleTree()
    tree1.add_leaf(b"A")
    tree1.add_leaf(b"B")
    root1 = tree1.compute_root()

    tree2 = MerkleTree()
    tree2.add_leaf(b"A")
    tree2.add_leaf(b"B")
    root2 = tree2.compute_root()

    assert root1 == root2
