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


def load_events(path: pathlib.Path):
    """Load events from JSON text at path."""
    with open(path, 'rt', encoding=ENCODING) as handle:
        event_data = handle.read()
    return orjson.loads(event_data)


def parse_meta(events):
    """Parse the meta data from the events dictionary.

    "_meta": {
      "binary": {
        "logic": "first",
        "evaluation": [
          "is_good",
          "is_bad"
        ]
      },
      "is_bad": [
        true
      ],
      "is_good": [
        {
          "key": "closed",
          "values": [
            {
              "is": true
            }
          ]
        },
        {
          "key": "status",
          "values": [
            {
              "eq": "MERGED"
            }
          ]
        }
      ],
      "time_window": [
        {
          "key": "create_at"
        },
        {
          "key": "close_at"
        }
      ]
    }
    """
    algorithm = {
        'order': events['_meta']['binary']['logic'],
        'evaluation': events['_meta']['binary']['evaluation'],
        'is_bad': events['_meta']['is_bad'][0],  # HACK A DID ACK
        'is_good': events['_meta']['is_good'],
        'time_window': tuple(v['key'] for v in events['_meta']['time_window']),
    }
    # TODO use operator module later and real meta processing
    return algorithm


def test_load_events():
    events = load_events(pathlib.Path('test', 'fixtures', 'custom', 'events.json'))
    assert 'data' in events


def test_parse_meta():
    events = load_events(pathlib.Path('test', 'fixtures', 'custom', 'events.json'))
    algorithm = parse_meta(events)
    assert algorithm['is_bad'] is True
    assert algorithm['is_good'][0]['key'] == 'closed'
    assert algorithm['is_good'][1]['key'] == 'status'
    assert algorithm['time_window'] == ('create_at', 'close_at')
