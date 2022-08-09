# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""API of interface operations for calculating binary year to date metrics with monthly cumulative slices.."""
# import os
import sys
from typing import List, Union

import kdl  # type: ignore

# from first import first


def it_starts_with_silence() -> None:
    """Stub to bootstrap development and survive the make rounds before implementation is in place."""
    # assert os.getenv('DO_NOT_COMPLAIN_IF_THIS_IS_PRESENT_IN_YOUR_ENV', 'all good') == 'all good'
    # assert sys.path > []
    doc = kdl.Document()
    doc.append(
        kdl.Node(
            name='simple-name',
            properties=None,
            arguments=[123],
            children=[
                kdl.Node(
                    name='complex name here!',
                    properties=None,
                    arguments=None,
                    children=None,
                )
            ],
        )
    )
    _ = kdl.parse(doc)
    # assert next(ast[0]) == 123
    # assert first((1, 2)) == 1


def main(argv: Union[List[str], None] = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    return 0
