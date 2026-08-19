# Consolidated Smart Grid & Secure Kernel System

Standards-based Python codebase integrating smart-grid communication protocols (IEEE 2030.5, OpenADR 2.0b, IEC 61850, DNP3) with a deterministic compute kernel and clean-room research ingestion pipeline.

## Architecture Overview

- **core/** – Deterministic kernel (exact rational arithmetic, L6 seal gates) + Merkle tree for archival integrity
- **protocols/** – Protocol adapters / stubs for IEEE 2030.5, OpenADR, IEC 61850, DNP3
- **crypto/** – PKI/HSM interface + NIST PQC (ML-KEM / ML-DSA) placeholders
- **tests/** – Unit tests for kernel, Merkle, and protocol payloads

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Run the deterministic kernel verification
python -m smartgrid_system.core.deterministic
# or
verify-kernel
```

Expected output:
```
ALL DETERMINISTIC KERNEL CHECKS PASSED: T1_LOCKED
```

## Run Tests

```bash
pytest smartgrid_system/tests/ -v
```

## Project Structure

```
smartgrid_system/
├── core/
│   ├── deterministic.py   # L6 seal + rational checks
│   ├── merkle_tree.py     # SHA-256 Merkle integrity
│   └── utils.py
├── protocols/
│   ├── ieee2030.py        # IEEE 2030.5 DERControl
│   ├── openadr.py         # OpenADR 2.0b VTN/VEN
│   ├── iec61850.py        # GOOSE / MMS stubs
│   └── dnp3.py            # DNP3 adapter
├── crypto/
│   ├── pki_hsm.py
│   └── pqc_kem_dsa.py
└── tests/
```

## Security Notes

- All network paths expect mutual TLS (X.509)
- Deterministic kernel uses only integer / Fraction arithmetic (no floats, no RNG)
- PQC modules are placeholders pending approved library integration
- HSM operations are stubbed; replace with PKCS#11 / CloudHSM in production

## References

- IEEE 2030.5 (SEP 2.0)
- IEC 61850 / IEC 62351
- OpenADR 2.0b
- DNP3 (IEEE 1815) Secure Authentication v5
- NIST FIPS 203 (ML-KEM) / FIPS 204 (ML-DSA)
- FIPS 140-3 HSM guidance

## License

This repository is provided for research and architecture validation purposes.
