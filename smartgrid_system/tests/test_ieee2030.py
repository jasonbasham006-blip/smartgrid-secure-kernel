"""Tests for IEEE 2030.5 stubs."""

from smartgrid_system.protocols.ieee2030 import (
    SAMPLE_DER_CONTROL,
    validate_der_control,
    post_der_control,
    IEEE2030Server,
)


def test_sample_payload_valid():
    assert validate_der_control(SAMPLE_DER_CONTROL) is True


def test_invalid_payload():
    assert validate_der_control({}) is False
    assert validate_der_control({"DERControl": {}}) is False


def test_post_stub():
    status = post_der_control("https://example.com", SAMPLE_DER_CONTROL)
    assert status == 201


def test_server_handle():
    server = IEEE2030Server()
    resp = server.handle_der_control(SAMPLE_DER_CONTROL)
    assert resp["code"] == 201
    assert server.last_control is not None
