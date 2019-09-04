"""
Test Script Using PyTest Framework
author: rsimari
date: 9/4/19
"""

import pytest
import hash_tool

def test_sha256_digest():
	result = hash_tool.main('sha256')
	assert result is not None

