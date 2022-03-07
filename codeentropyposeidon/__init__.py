"""Integration of CodeEntropy tool with the POSEIDON code to form a complete and generally applicable set of tools for calculating entropy"""

# Add imports here
from .codeentropyposeidon import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
