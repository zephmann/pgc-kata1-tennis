# :coding: utf-8

import pytest

import tennis


@pytest.fixture
def match():
    return tennis.create_match()


def test_create_match(match):
    assert isinstance(match, tennis.core.Match)


def test_start_score(match):
    assert match.score == "Love All"


def test_point_server(match):
    match.point_server()
    assert match.score == "15-Love"


def test_point_opponent(match):
    match.point_opponent()
    assert match.score == "Love-15"


@pytest.mark.parametrize(
    "original_score, formatted_score",
    [
        ((0, 0), "Love All"),
        ((0, 1), "Love-15"),
        ((0, 2), "Love-30"),
        ((0, 3), "Love-40"),
        ((0, 4), "Game Opponent"),
        ((1, 0), "15-Love"),
        ((1, 1), "15 All"),
        ((1, 2), "15-30"),
        ((1, 3), "15-40"),
        ((1, 4), "Game Opponent"),
        ((2, 0), "30-Love"),
        ((2, 1), "30-15"),
        ((2, 2), "30 All"),
        ((2, 3), "30-40"),
        ((2, 4), "Game Opponent"),
        ((3, 0), "40-Love"),
        ((3, 1), "40-15"),
        ((3, 2), "40-30"),
        ((3, 3), "Deuce"),
        ((3, 4), "Adv Out"),
        ((3, 5), "Game Opponent"),
        ((4, 0), "Game Server"),
        ((4, 1), "Game Server"),
        ((4, 2), "Game Server"),
        ((4, 3), "Adv In"),
        ((4, 4), "Deuce"),
        ((4, 5), "Adv Out"),
        ((4, 6), "Game Opponent"),
        ((5, 3), "Game Server"),
        ((5, 4), "Adv In"),
        ((5, 5), "Deuce"),
        ((5, 6), "Adv Out"),
        ((5, 7), "Game Opponent"),
        ((6, 4), "Game Server"),
        ((6, 5), "Adv In"),
        ((6, 6), "Deuce"),
        ((6, 7), "Adv Out"),
        ((6, 8), "Game Opponent"),
    ]
)
def test_score(original_score, formatted_score):
    assert tennis.score(original_score) == formatted_score


def test_integration_1(match):
    assert match.score == "Love All"
    match.point_server()
    assert match.score == "15-Love"
    match.point_server()
    assert match.score == "30-Love"
    match.point_opponent()
    assert match.score == "30-15"
    match.point_server()
    assert match.score == "40-15"
    match.point_opponent()
    assert match.score == "40-30"
    match.point_opponent()
    assert match.score == "Deuce"
    match.point_opponent()
    assert match.score == "Adv Out"
    match.point_server()
    assert match.score == "Deuce"
    match.point_server()
    assert match.score == "Adv In"
    match.point_opponent()
    assert match.score == "Deuce"
    match.point_server()
    assert match.score == "Adv In"
    match.point_server()
    assert match.score == "Game Server"


def test_integration_2(match):
    assert match.score == "Love All"
    match.point_opponent()
    assert match.score == "Love-15"
    match.point_opponent()
    assert match.score == "Love-30"
    match.point_server()
    assert match.score == "15-30"
    match.point_server()
    assert match.score == "30 All"
    match.point_opponent()
    assert match.score == "30-40"
    match.point_server()
    assert match.score == "Deuce"
    match.point_server()
    assert match.score == "Adv In"
    match.point_opponent()
    assert match.score == "Deuce"
    match.point_opponent()
    assert match.score == "Adv Out"
    match.point_server()
    assert match.score == "Deuce"
    match.point_opponent()
    assert match.score == "Adv Out"
    match.point_opponent()
    assert match.score == "Game Opponent"
