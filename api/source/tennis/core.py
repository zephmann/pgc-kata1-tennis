# :coding: utf-8

import typing


SCORE_NAMES = {
    0: "Love",
    1: "15",
    2: "30",
    3: "40",
}


class Match():
    """Score tracker for a tennis match."""

    def __init__(self):
        """Initialize a new match, set the score to "Love All"."""
        self._score = None
        self._formatted_score = None
        self._is_active = None
        self._server_won = None

        self._reset_score()

    @property
    def score(self):
        """Return a formatted string of the current score."""
        return self._formatted_score

    @property
    def is_active(self):
        return self._active

    @property
    def server_won(self):
        return self._server_won
    
    def _reset_score(self):
        """Reset the score of the match."""
        self._score = (0, 0)
        self._formatted_score = format_score(self._score)
        self._active = True
        self._server_won = None
    
    def point_server(self):
        """Increment the score for the server."""
        if not self._active:
            raise RuntimeError(
                "Unable to increment score, game is no longer active."
            )

        self._update_score(
            (self._score[0]+1, self._score[1])
        )

    def point_opponent(self):
        """Increment the score for the opponent."""
        if not self._active:
            raise RuntimeError(
                "Unable to increment score, game is no longer active."
            )

        self._update_score(
            (self._score[0], self._score[1]+1)
        )

    def _update_score(self, new_score: typing.Tuple[int, int]):
        """Update the human-readable score and check for a winner."""
        self._score = new_score
        self._formatted_score = format_score(self._score)

        if "Game" in self._formatted_score:
            self._server_won = "Server" in self._formatted_score
            self._active = False
        
        else:
            self._server_won = None
            self._active = True


def format_score(score: typing.Tuple[int, int]):
    """Return a human-readable string using tennis terms corresponding
    to *score*, assuming server's score is first.

    """
    diff_score = score[0] - score[1]
    adv_server = diff_score > 0

    # check for a winner
    # note: diff should never be greater than 2, but keeping to be safe
    if (score[0] >= 4 or score[1] >= 4) and abs(diff_score) >= 2:
        winner = "Server" if adv_server else "Opponent"
        return "Game {}".format(winner)

    # check for tie
    if not diff_score:
        if score[0] < 3:
            return "{} All".format(SCORE_NAMES[score[0]])
        
        return "Deuce"

    # check for advantage
    if (score[0] + score[1]) >= 6:
        advantage = "In" if adv_server else "Out"
        return "Adv {}".format(advantage)

    # swap with tennis terms
    server_score = SCORE_NAMES[score[0]]
    opponent_score = SCORE_NAMES[score[1]]
    return "{}-{}".format(server_score, opponent_score)
