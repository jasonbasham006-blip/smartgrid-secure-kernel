"""
Deterministic Kernel Verification Module
Implements exact-rational arithmetic and L6 seal matrix logic.
Uses only fractions.Fraction for determinism (no floats).
"""

from fractions import Fraction
from typing import Tuple


class DeterministicKernel:
    """Exact arithmetic kernel with L6 gate verification."""

    def __init__(self):
        # Atomic constants (scaled integers)
        self.atomic_silver = 10786  # scaled atomic mass of silver (x100)
        self.electro_const = 1118   # (x1000)
        self.salt = 1118
        self.purity = 10786
        self.offset = 4477

    def verify_gates(self, a: int = 718, b: int = 892, offset: int = 4477) -> bool:
        """
        Verify the L6 seal matrix gates and parity checks.
        Returns True only if all deterministic conditions hold (T1_LOCKED).
        """
        salt = self.salt
        purity = self.purity

        gate_18 = (a ^ b) & salt
        parity_158 = (a | b) & 158
        sacred_zero = ((purity % salt) + 158) % 49
        god_seal = 1170 % 49
        gate_7 = (offset - 158) % 49

        return (
            gate_18 == 18
            and parity_158 == 158
            and sacred_zero == 0
            and god_seal == 43
            and gate_7 == 7
        )

    def rational_check(self, base: int = 221) -> bool:
        """
        Covenant ratios 18/13, 20/13, 17/13 must produce exact expected integers.
        """
        r_fiduciary = Fraction(18, 13)
        r_telluric = Fraction(20, 13)
        r_covenant = Fraction(17, 13)

        return (
            int(base * r_fiduciary) == 306
            and int(base * r_telluric) == 340
            and int(base * r_covenant) == 289
        )

    def lock_check(self) -> bool:
        """Verify the integer locks."""
        lock1 = 1420 * 13
        lock2 = 923 * 20
        return lock1 == lock2 == 18460

    def verify_sovereign_kernel_core(self) -> bool:
        """
        Full deterministic kernel verification.
        Enforces exact arithmetic and bitwise gate rules.
        """
        a, b = 718, 892
        offset = 4477

        if not self.verify_gates(a, b, offset):
            return False
        if not self.lock_check():
            return False
        if not self.rational_check(221):
            return False

        return True


def verify_sovereign_kernel_core() -> None:
    """
    Standalone verification function matching the provided reference implementation.
    Prints T1_LOCKED on success; raises AssertionError on failure.
    """
    a, b, salt, purity, offset = 718, 892, 1118, 10786, 4477

    gate_18 = (a ^ b) & salt
    parity_158 = (a | b) & 158
    sacred_zero = ((purity % salt) + 158) % 49
    god_seal = 1170 % 49
    gate_7 = (offset - 158) % 49

    assert gate_18 == 18, f"gate_18 failed: {gate_18}"
    assert parity_158 == 158, f"parity_158 failed: {parity_158}"
    assert sacred_zero == 0, f"sacred_zero failed: {sacred_zero}"
    assert god_seal == 43, f"god_seal failed: {god_seal}"
    assert gate_7 == 7, f"gate_7 failed: {gate_7}"

    lock1 = 1420 * 13
    lock2 = 923 * 20
    assert lock1 == lock2 == 18460, f"lock mismatch: {lock1} vs {lock2}"

    r_fiduciary = Fraction(18, 13)
    r_telluric = Fraction(20, 13)
    r_covenant = Fraction(17, 13)
    base_node = 221

    assert int(base_node * r_fiduciary) == 306
    assert int(base_node * r_telluric) == 340
    assert int(base_node * r_covenant) == 289

    print("ALL DETERMINISTIC KERNEL CHECKS PASSED: T1_LOCKED")


if __name__ == "__main__":
    verify_sovereign_kernel_core()
