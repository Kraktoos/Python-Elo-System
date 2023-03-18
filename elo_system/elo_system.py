# SPDX-FileCopyrightText: 2021 Kraktoos
# SPDX-FileCopyrightText: 2022-2013 Samuel Wu
#
# SPDX-License-Identifier: MIT
"""
Originally created by Kraktoos on 10/20/2021.
Rewritten by Samuel Wu on 03/15/2023.
"""

from typing import Dict, List, Optional

from elo_system.player import Player


class EloSystem:
    """A class that represents an implementation of the Elo Rating System."""

    def __init__(
        self,
        base_elo: int = 1000,
        k_factor: int = 32,
        *,
        rankings: bool = False,
    ) -> None:
        """Initialize the Elo System.

        :param base_elo: The default and average average for all players,
        defaults to 1000.
        :type base_elo: int, optional
        :param k_factor: The amount ratings change for players, defaults to 32.
        :type k_factor: int, optional
        :param rankings: Turn rankings on or off, defaults to False.
        :type rankings: bool, optional
        """
        self.base_elo = base_elo
        self.k_factor = k_factor
        self.players: Dict[str, Player] = {}
        self.rankings = rankings

    # Player Methods

    def add_player(self, player: str, elo: Optional[int] = None) -> None:
        """Add a player to the system.

        :param player: The name of the player.
        :type name: str
        :param elo: The initial ratings for the player, defaults to None.
        :type elo: Optional[int], optional
        """
        if elo is None:
            elo = self.base_elo

        self.players[player] = Player(elo)

        if self.rankings:
            self.players[player].calculate_rank()

    def remove_player(self, player: str) -> None:
        """Remove a player from the system.

        :param player: The name of the player.
        :type player: str
        """
        del self.players[player]

    # Elo Methods

    def set_elo(self, player: str, elo: int) -> None:
        """Set new ratings for a player.

        :param player: The name of the player.
        :type player: str
        :param elo: The new ratings for the player.
        :type elo: int
        """
        self.players[player].elo = elo

        if self.rankings:
            self.players[player].calculate_rank()

    def reset_elo(self, player: str) -> None:
        """Set a player's rating back to the average rating.

        :param player: The name of the player.
        :type player: str
        """
        self.players[player].elo = self.base_elo

        if self.rankings:
            self.players[player].calculate_rank()

    def add_elo(self, player: str, elo: int) -> None:
        """Add ratings to a player.

        :param player: The name of a player.
        :type player: str
        :param elo: The amount of ratings to add.
        :type elo: int
        """
        self.players[player].elo += elo

        if self.rankings:
            self.players[player].calculate_rank()

    def remove_elo(self, player: str, elo: int) -> None:
        """Remove ratings of a player.

        :param player: The name of a player.
        :type player: str
        :param elo: The amount of ratings to remove.
        :type elo: int
        """
        self.players[player].elo -= elo

        if self.rankings:
            self.players[player].calculate_rank()

    # Return Methods

    def get_player_elo(self, player: str) -> int:
        """Get the ratings of a player.

        :param player: The name of a player.
        :type player: str
        :return: The ratings of a player.
        :rtype: int
        """
        return self.players[player].elo

    def get_player_rank(self, player: str) -> Optional[str]:
        """Get the rank of a player.

        :param player: The name of a player.
        :type player: str
        :return: The rank of the player, defaults to None of rankings are
        turned off.
        :rtype: Optional[str]
        """
        return self.players[player].rank

    def get_player_wins(self, player: str) -> int:
        """Get the number of times a player has won.

        :param player: The name of the player.
        :type player: str
        :return: The number of wins.
        :rtype: int
        """
        return self.players[player].wins

    def get_player_losses(self, player: str) -> int:
        """Get the number of times a player has lost.

        :param player: The name of the player.
        :type player: str
        :return: The number of losses.
        :rtype: int
        """
        return self.players[player].losses

    def get_player_draws(self, player: str) -> int:
        """Get the number of times a player has drawn.

        :param player: The name of the player.
        :type player: str
        :return: The number of draws.
        :rtype: int
        """
        return self.players[player].draws

    def get_player_count(self) -> int:
        """Get the amount of players in the system.

        :return: The number of players.
        :rtype: int
        """
        return len(self.players)

    # Return List Methods

    def get_overall_list(self) -> List[Dict[str, int | str]]:
        """Get the statistic of all players in the system.

        :return: List of all the players with their statistics.
        :rtype: list[dict[str, int | str]]
        """
        players: List[Dict[str, int | str]] = []

        for key, val in self.players.items():
            dictionary: Dict[str, int | str] = {"player": key}
            dictionary.update(val.asdict())
            players.append(dictionary)

        return sorted(players, key=lambda d: d["elo"], reverse=True)

    def get_players_with_elo(self, elo: int) -> List[str]:
        """Get all players with an exact rating.

        :param elo: The rating to search from.
        :type elo: int
        :return: All the players with that rating.
        :rtype: list[str]
        """
        return [key for key, val in self.players.items() if val.elo == elo]

    def get_players_with_rank(self, rank: str) -> List[str]:
        """Get all players with a rank.

        :param rank: The rank to search from.
        :type rank: str
        :return: All the players with that rank.
        :rtype: list[str]
        """
        return [key for key, val in self.players.items() if val.rank == rank]

    def get_players_with_wins(self, wins: int) -> List[str]:
        """Get all players with an exact number of wins.

        :param wins: The number of wins to search from.
        :type wins: int
        :return: All the players with that number of wins.
        :rtype: list[str]
        """
        return [key for key, val in self.players.items() if val.wins == wins]

    def get_players_with_losses(self, losses: int) -> List[str]:
        """Get all players with an exact number of losses.

        :param losses: The number of losses to search from.
        :type losses: int
        :return: All the players with that number of losses.
        :rtype: list[str]
        """
        return [
            key for key, val in self.players.items() if val.losses == losses
        ]

    def get_players_with_draws(self, draws: int) -> List[str]:
        """Get all players with an exact number of draws.

        :param draws: The number of draws to search from.
        :type draws: int
        :return: All the players with that number of draws.
        :rtype: list[str]
        """
        return [key for key, val in self.players.items() if val.draws == draws]

    # Main Matching System

    def record_match(
        self, *, winner: str, loser: str, draw: bool = False
    ) -> None:
        """Calculate the players' ratings based on of they won, lost or drawn.

        :param winner: The name of the player who won a match.
        :type winner: str
        :param loser: The name of the player who lost a match.
        :type loser: str
        :param draw: Make the match be a draw, defaults to False.
        :type draw: bool, optional
        """
        player_a = self.players[winner]
        player_b = self.players[loser]

        ratings_a = 10 ** (player_a.elo / 400)
        ratings_b = 10 ** (player_b.elo / 400)
        expected_score_a = ratings_a / (ratings_a + ratings_b)
        expected_score_b = ratings_b / (ratings_a + ratings_b)

        if draw:
            player_a.draws += 1
            player_b.draws += 1
            self.add_elo(winner, int(self.k_factor * (0.5 - expected_score_a)))
            self.add_elo(loser, int(self.k_factor * (0.5 - expected_score_b)))
        else:
            player_a.wins += 1
            player_b.losses += 1
            self.add_elo(winner, int(self.k_factor * (1 - expected_score_a)))
            self.add_elo(loser, int(self.k_factor * (0 - expected_score_b)))
