# Architecture Notes

See the full report: [architecture.pdf](architecture.pdf)

## Key Components

1. **Deterministic Kernel** – Exact rational arithmetic + L6 seal matrix (gates 18/7, parity 158, sacred zero, god seal). Produces T1_LOCKED state.
2. **Clean-Room Ingestion** – Registry check → Merkle root → L6 seal.
3. **Protocol Adapters** – IEEE 2030.5 DERControl, OpenADR, IEC 61850 GOOSE/MMS, DNP3.
4. **Crypto** – PKI/HSM + NIST post-quantum placeholders.

## Implementation Priority (from original report)

- **P0**: Branch seals, EU LOTL root, Merkle forest of archival data
- **P1**: Kernel normalization, IEEE 2030.5 gateway, IEC 61850 GOOSE, cert probing
- **P2**: Tertiary ratio framework, archival spoliation seal, EUDI wallet integration
