#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Command line interface operations for calculating binary year to date metrics with monthly cumulative slices."""
import sys
from typing import List, Union

import booq.booq as api


# pylint: disable=expression-not-assigned
def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    return api.main(argv)
