"""
IEC 61850 abstraction (MMS / GOOSE / SMV).
GOOSE is Layer-2; real implementation requires raw sockets or vendor SDK.
"""

from typing import Callable, Optional, Any


def send_goose_msg(vlan: int, appid: int, data: bytes) -> bool:
    """
    Send GOOSE multicast frame (EtherType 0x88B8).
    Stub: returns True. Real: raw socket / pylibpcap / pyshark.
    """
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("data must be bytes")
    # Production would bind to process-bus NIC
    return True


def receive_goose_msg(callback: Callable[[bytes], None]) -> None:
    """
    Listen for GOOSE frames and invoke callback.
    Stub: does nothing (requires privileged NIC access).
    """
    pass


def read_logical_node(ied: str, ln: str, do_name: str) -> Any:
    """Stub MMS read of a logical node data object."""
    return {"value": 0.0, "quality": "good", "t": 0}


def write_datasets(ied: str, dataset: str, values: dict) -> bool:
    """Stub MMS write."""
    return True
