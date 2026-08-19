"""
OpenADR 2.0b VTN/VEN stubs.
XML-based DR events over HTTP or XMPP (TLS).
"""

from typing import Optional


class VTN:
    """Virtual Top Node (utility side)."""

    def __init__(self, endpoint: str = "https://vtn.example.com"):
        self.endpoint = endpoint
        self.ssl_ctx = True  # placeholder

    def send_event(self, ven_id: str, event_xml: str) -> int:
        """HTTP POST (PUSH) or XMPP publish. Stub returns 200."""
        if not event_xml.strip().startswith("<"):
            raise ValueError("Expected XML event")
        # In production: requests.post(..., data=event_xml, verify=...)
        return 200


class VEN:
    """Virtual End Node (client side)."""

    def __init__(self, vtn_endpoint: str = "https://vtn.example.com"):
        self.vtn_endpoint = vtn_endpoint
        self.ssl_ctx = True

    def poll_events(self) -> str:
        """HTTP GET or XMPP retrieve. Stub returns sample XML."""
        return """<?xml version=\"1.0\"?>
<oadrPayload>
  <oadrSignedObject>
    <oadrDistributeEvent>
      <eiEvent>
        <eventDescriptor>
          <eventID>sample-price-event-001</eventID>
        </eventDescriptor>
      </eiEvent>
    </oadrDistributeEvent>
  </oadrSignedObject>
</oadrPayload>"""
