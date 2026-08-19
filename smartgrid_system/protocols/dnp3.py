"""
DNP3 (IEEE 1815) adapter using pydnp3 when available.
Otherwise pure stubs.
"""

from typing import Any, Optional


def start_dnp3_outstation(config: Optional[dict] = None) -> Any:
    """
    Start a DNP3 outstation (stub).
    Real: from pydnp3 import opendnp3, asiopal
    """
    return {"status": "stub_outstation_started", "config": config or {}}


def send_dnp3_command(point: str, value: Any) -> bool:
    """Map to DNP3 Class 1/2 command. Stub succeeds."""
    return True


def poll_outstation() -> dict:
    """Simulate a poll response."""
    return {
        "analog_inputs": {"AI0": 120.5, "AI1": 0.0},
        "binary_inputs": {"BI0": True},
        "timestamp": 0,
    }
