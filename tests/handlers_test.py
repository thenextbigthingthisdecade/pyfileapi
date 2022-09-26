from __future__ import annotations

from pyfileapi.handlers import find_match


def test_match_handler_returns_single_match() -> None:
    res = find_match(file='handlers_test.py', search_string='pyfileapi')
    assert res is not None
    text, line, (start, end) = res
    assert text == 'pyfileapi'
    assert line == 3
    assert start, end == (5, 12)


def test_match_handler_returns_all_matches_with_all_matches_true() -> None:
    res = find_match(
        file='handlers_test.py',
        search_string='pyfileapi', all_matches=True,
    )
    assert res is not None
    assert len(res) == 1
    text, line, (start, end) = res
    assert text == 'pyfileapi'
    assert line == 3
    assert start, end == (5, 12)
