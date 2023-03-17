# SPDX-FileCopyrightText: 2023 Samuel Wu
#
# SPDX-License-Identifier: MIT
"""Created by Samuel Wu on 03/15/2023."""

from typing import Optional, Union


class Player:
    """A class that stores the statistics of a player."""

    def __init__(self, elo: int):
        """Create a player.

        :param elo: The initial ratings of a player.
        :type elo: int
        """
        self.elo = elo
        self.wins: int = 0
        self.losses: int = 0
        self.draws: int = 0
        self.rank: Optional[str] = None

    def calculate_rank(self) -> None:
        """Calculate the rankings of a player if rankings are enabled."""
        if self.elo >= 2400:
            self.rank = "Grand Master"
        elif self.elo >= 2000:
            self.rank = "Master"
        elif self.elo >= 1850:
            self.rank = "Diamond"
        elif self.elo >= 1650:
            self.rank = "Platinum"
        elif self.elo >= 1500:
            self.rank = "Gold"
        elif self.elo >= 1300:
            self.rank = "Silver"
        elif self.elo >= 1100:
            self.rank = "Bronze"
        else:
            self.rank = "Iron"

    def asdict(self) -> dict[str, Union[int, str]]:
        """Store the statistics of a player as a dictionary.

        :return: The statistics of a player as a dictionary.
        :rtype: dict[str, Union[int, str]]
        """
        dictionary: dict[str, Union[int, str]] = {
            "elo": self.elo,
            "wins": self.wins,
            "losses": self.losses,
            "draws": self.draws,
        }

        if self.rank is not None:
            dictionary.update(rank=self.rank)

        return dictionary
