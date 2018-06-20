# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""
OPENQASM number.
"""

from functools import lru_cache

from sympy import Number


@lru_cache(maxsize=8192, typed=True)
def qasm_number(val):
    return Number(val)
