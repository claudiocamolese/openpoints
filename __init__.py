"""Minimal OpenPoints package init for local backbone reuse.

The original package eagerly imports transforms and other optional
dependencies. For the NTRL KUKA experiments we only need the PointNext
backbone, so keep package import lightweight and let callers import the
submodules they actually need.
"""

__all__: list[str] = []
