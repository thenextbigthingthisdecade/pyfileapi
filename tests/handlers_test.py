from __future__ import annotations

from pyfileapi import handlers


def test_read_file_handler_can_open_existing_file() -> None:
    f = handlers.read_file('handlers_test.py')
    assert f is not None
    assert f.readline().startswith('from')
