from __future__ import annotations

from typing import cast

from pyfileapi.search import find_match
from pyfileapi.search_helpers import MatchTuple


def test_match_handler_returns_single_match() -> None:
    res: MatchTuple = cast(
        MatchTuple, find_match(file='README.md', search_string='pyfileapi'),
    )
    assert res is not None
    text, line, (start, end) = res
    assert text == 'pyfileapi'
    assert line == 1
    assert start, end == (3, 12)


def test_match_handler_returns_all_matches_with_all_matches_true() -> None:
    res: list[MatchTuple] = cast(
        list[MatchTuple],
        find_match(
            file='README.md',
            search_string='pyfileapi',
            all_matches=True,
        ),
    )
    assert res is not None
    assert len(res) == 1
    text, line, (start, end) = res[0]
    assert text == 'pyfileapi'
    assert line == 1
    assert start, end == (3, 12)
