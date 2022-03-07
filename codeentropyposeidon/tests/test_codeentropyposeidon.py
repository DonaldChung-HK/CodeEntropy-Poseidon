"""
Unit and regression test for the codeentropyposeidon package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import codeentropyposeidon


def test_codeentropyposeidon_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "codeentropyposeidon" in sys.modules
