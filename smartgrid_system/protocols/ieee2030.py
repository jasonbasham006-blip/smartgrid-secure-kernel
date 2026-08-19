"""
IEEE 2030.5 (SEP 2.0) REST client/server stubs.
Uses HTTPS with mutual TLS.
"""

from typing import Dict, Any, Optional
import json


# Sample DERControl payload from the architecture document
SAMPLE_DER_CONTROL = {
    "DERControl": {
        "mRID": "1F3A8B9C00018460",
        "description": "Active Power Curtailment & Volt-VAR Response",
        "creationTime": 1718928000,
        "DERControlBase": {
            "opModFixedW": {"value": 80, "multiplier": 0},
            "opModVoltVar": {
                "curveData": [
                    {"u": 216, "v": 100},
                    {"u": 240, "v": 0},
                    {"u": 264, "v": -100},
                ]
            },
        },
    }
}


def post_der_control(
    endpoint: str,
    payload: Dict[str, Any],
    cert: Optional[str] = None,
    key: Optional[str] = None,
    ca_bundle: Optional[str] = None,
) -> int:
    """
    Send HTTPS POST with mutual TLS (stubbed for offline/demo).
    In production: uses requests with cert=(cert, key), verify=ca_bundle.
    """
    # Offline stub: validate payload structure
    if "DERControl" not in payload:
        raise ValueError("Invalid DERControl payload")
    # Simulate success
    return 201


def validate_der_control(payload: Dict[str, Any]) -> bool:
    """Basic schema validation for DERControl."""
    try:
        der = payload["DERControl"]
        assert "mRID" in der
        assert "DERControlBase" in der
        return True
    except (KeyError, AssertionError, TypeError):
        return False


class IEEE2030Server:
    """Minimal Flask-style server stub (not started by default)."""

    def __init__(self):
        self.last_control: Optional[Dict] = None

    def handle_der_control(self, payload: Dict) -> Dict:
        if not validate_der_control(payload):
            return {"status": "error", "code": 400}
        self.last_control = payload
        return {"status": "accepted", "code": 201}
