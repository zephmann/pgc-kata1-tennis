# :coding: utf-8

import tennis
import tennis.core


def test_create_match():
    match = tennis.create_match("Team A", "Team B")
    assert isinstance(match, tennis.core.Match)
