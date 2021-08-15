# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib

import orjson
import pytest  # type: ignore

import booq.cli as cli

ENCODING = 'utf-8'


def test_main_nok_too_many_arguments_remove_later():
    message = r'main\(\) takes from 0 to 1 positional arguments but 2 were given'
    with pytest.raises(TypeError, match=message):
        cli.main(1, 2)


def test_load_events():
    with open(pathlib.Path('tests', 'fixtures', 'custom', 'events.json'), 'rt', encoding=ENCODING) as handle:
        event_data = handle.read()
    events = orjson.loads(event_data)
    del event_data
    assert 'data' in events
