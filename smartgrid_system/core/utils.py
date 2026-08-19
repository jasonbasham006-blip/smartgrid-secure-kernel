"""
Common helpers: configuration, logging, etc.
"""

import logging
from typing import Any, Dict


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    return logging.getLogger("smartgrid_system")


def load_config(path: str = None) -> Dict[str, Any]:
    """Placeholder config loader."""
    return {
        "tls_min_version": "TLSv1.2",
        "require_mutual_auth": True,
        "use_pqc": False,  # enable when ML-KEM/ML-DSA libs available
    }
