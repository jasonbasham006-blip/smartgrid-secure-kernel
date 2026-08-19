"""Unit tests for the deterministic kernel."""

import pytest
from smartgrid_system.core.deterministic import (
    DeterministicKernel,
    verify_sovereign_kernel_core,
)


def test_verify_gates_default():
    kernel = DeterministicKernel()
    assert kernel.verify_gates() is True


def test_lock_check():
    kernel = DeterministicKernel()
    assert kernel.lock_check() is True


def test_rational_check():
    kernel = DeterministicKernel()
    assert kernel.rational_check(221) is True


def test_full_kernel():
    kernel = DeterministicKernel()
    assert kernel.verify_sovereign_kernel_core() is True


def test_standalone_function(capsys):
    verify_sovereign_kernel_core()
    captured = capsys.readouterr()
    assert "T1_LOCKED" in captured.out


def test_gate_failure():
    kernel = DeterministicKernel()
    # Wrong a,b should fail
    assert kernel.verify_gates(a=1, b=1, offset=4477) is False
