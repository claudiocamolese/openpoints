"""Lightweight utility exports for local model reuse.

OpenPoints normally re-exports many optional utilities here. Those imports pull
extra dependencies that are not required when we only want to instantiate the
PointNext encoder inside NTRL. Keep the registry always available and expose the
rest on a best-effort basis.
"""

from . import registry

__all__ = ["registry"]

try:
    from .random import set_random_seed

    __all__.append("set_random_seed")
except Exception:
    set_random_seed = None

try:
    from .config import EasyConfig, print_args

    __all__ += ["EasyConfig", "print_args"]
except Exception:
    EasyConfig = None
    print_args = None
