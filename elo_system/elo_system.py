# SPDX-FileCopyrightText: 2021 Kraktoos
# SPDX-FileCopyrightText: 2022 Samuel Wu
#
# SPDX-License-Identifier: MIT
"""
Created: 10/20/2021
Modified: 10/01/2022
Author: Kraktoos
Edited: Samuel Wu
"""


class EloSystem:
    """A class that represents an implementation of the Elo Rating System."""

    def __init__(
        self, base_elo: int = 1000, k: int = 32, rankings: bool = True
    ):
        """Initializes the Elo System.

        Args:
            base_elo (int, optional): The base Elo that you want everyone to
            have. Defaults to 1000.
            k (int, optional): The value you want the Elo to change by.
            Defaults to 32.
            rankings (bool, optional): Turn off the rankings if provided False.
            Defaults to True.
        """
        self.base_elo: int = base_elo
        self.k: int = k
        self.players: list = []
        self.rankings: bool = rankings

    # Player Methods

    def add_player(self, player: str, elo: int = None) -> None:
        """Adds a Player to the Player List.

        Args:
            player (str): The Player to add.
            elo (int, optional): Their initial elo value. Defaults to None.
        """
        if elo is None:
            elo = self.base_elo
        if self.rankings:
            info = {
                "player": player,
                "elo": elo,
                "wins": 0,
                "losses": 0,
                "draws": 0,
                "rank": None,
            }
        else:
            info = {
                "player": player,
                "elo": elo,
                "wins": 0,
                "losses": 0,
                "draws": 0,
            }
        self.players.append(info)
        self._update_everything()

    def remove_player(self, player: str) -> None:
        """Removes a Player from the Players List.

        Args:
            player (str): The Player to remove.

        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                self.players.remove(i)
                return
        raise ValueError(f"Player {player} not found")

    # Elo Methods

    def set_elo(self, player: str, elo: int) -> None:
        """Sets a Players Elo.

        Args:
            player (str): The Player you want to their to be set.
            elo (int): The Elo you want the player to have.

        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                i['elo'] = elo
                self._update_everything()
                return
        raise ValueError(f"Player {player} not found")

    def reset_elo(self, player: str) -> None:
        """Reset a player's Elo.

        Args:
            player (str): The Player that you want their Elo to reset to the
            base Elo.

        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                i['elo'] = self.base_elo
                self._update_everything()
                return
        raise ValueError(f"Player {player} not found")

    def add_elo(self, player: str, elo: int) -> None:
        """Adds Elo to a Player.

        Args:
            player (str): The Player that you want their Elo to be add.
            elo (int): The amount of Elo to add by.

        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                i['elo'] += elo
                self._update_everything()
                return
        raise ValueError(f"Player {player} not found")

    def remove_elo(self, player: str, elo: int) -> None:
        """Removes Elo to a Player.

        Args:
            player (str): The Player that you want their Elo to be remove.
            elo (int): The amount of Elo to remove by.


        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                i['elo'] -= elo
                self._update_everything()
                return
        raise ValueError(f"Player {player} not found")

    # Return Methods

    def get_player_elo(self, player: str) -> int:
        """Returns a Player's Elo.

        Args:
            player (str): The Player you want to get the Elo from.

        Returns:
            int: The Elo of the Player.

        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                return i['elo']
        raise ValueError(f"Player {player} not found")

    def get_player_rank(self, player: str) -> str:
        """Returns a Player's Rank.

        Args:
            player (str): The Player you want to get the Rank from.

        Returns:
            str: The Rank of the Player.

        Raises:
            ValueError: The Player is not in the List of Players.
            RuntimeError: The user want the Rank of the Player but Rankings are
            turned off.
        """
        if self.rankings:
            for i in self.players:
                if i['player'] == player:
                    return i['rank']
            raise ValueError(f"Player {player} not found")
        raise RuntimeError("Rankings are turned off")

    def get_player_wins(self, player: str) -> int:
        """Returns a Player's Wins count.

        Args:
            player (str): The Player you want to get the Wins from.

        Returns:
            int: The number of Wins for the Player.

        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                return i['wins']
        raise ValueError(f"Player {player} not found")

    def get_player_losses(self, player: str) -> int:
        """Returns a Player's Losses count.

        Args:
            player (str): The Player you want to get the Losses from.

        Returns:
            int: The number of Losses for the Player.

        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                return i['losses']
        raise ValueError(f"Player {player} not found")

    def get_player_draws(self, player: str) -> int:
        """Returns a Player's Draws count.

        Args:
            player (str): The Player you want to get the Draws from.

        Returns:
            int: The number of Draws for the Player.

        Raises:
            ValueError: The Player is not in the List of Players.
        """
        for i in self.players:
            if i['player'] == player:
                return i['draws']
        raise ValueError(f"Player {player} not found")

    def get_player_count(self) -> int:
        """Returns the Player Count

        Returns:
            int: The number of players in the Elo system.
        """
        return len(self.players)

    # Return List Methods

    def get_overall_list(self):
        """Returns the Player, Elo and Ranks List.

        Returns:
            list: List of all the Players in the Elo system.
        """
        return sorted(self.players, key=lambda d: d['elo'], reverse=True)

    def get_players_with_elo(self, elo: int):
        """Returns a List of Players with the given Elo.

        Args:
            elo (int): The Elo to get Players from.

        Returns:
            list: List of Players with the given Elo.
        """
        return [i['player'] for i in self.players if i['elo'] == elo]

    def get_players_with_rank(self, rank: str) -> list:
        """Returns a List of Players with the given Rank.
        Args:
            rank (str): The Rank to get the Players with.

        Returns:
            list: List of Players with the given Rank.

        Raises:
            RuntimeError: The user want a List of Players with the given Rank
            but Rankings are turned off.
        """
        if self.rankings:
            return [i['player'] for i in self.players if i['rank'] == rank]
        raise RuntimeError("Rankings are turned off")

    def get_players_with_wins(self, wins: int) -> list:
        """Returns a List of Players with the given number of Wins.
        Args:
            wins (int): The number of Wins to get the Players with.

        Returns:
            list: List of Players with the given number of Wins.
        """
        return [i['player'] for i in self.players if i['wins'] == wins]

    def get_players_with_losses(self, losses: int) -> list:
        """Returns a List of Players with the given number of Losses.
        Args:
            losses (int): The number of Losses to get the Players with.

        Returns:
            list: List of Players with the given number of Losses.
        """
        return [i['player'] for i in self.players if i['losses'] == losses]

    def get_players_with_draws(self, draws: int) -> list:
        """Returns a List of Players with the given number of Draws.
        Args:
            draws (int): The number of Draws to get the Players with.

        Returns:
            list: List of Players with the given number of Draws.
        """
        return [i['player'] for i in self.players if i['draws'] == draws]

    # Main Matching System

    def record_match(
        self, player_a: str, player_b: str, winner: str = None
    ) -> None:
        """Runs the Calculations and Updates the Score of both Player A and B
        Following a Simple Elo System.

        Args:
            player_a (str): The first Player in a match.
            player_b (str): The second Player in a match.
            winner (str): The Player you want to win. None for a
            draw. Defaults to None.

        Raises:
            ValueError: The one of the two Players are not in the Players List.
        """
        elo_a: int = -1
        elo_b: int = -1

        for i in self.players:
            if i['player'] == player_a:
                index_a = self.players.index(i)
                elo_a = i['elo']
            elif i['player'] == player_b:
                index_b = self.players.index(i)
                elo_b = i['elo']

        if elo_a == -1:
            raise ValueError(f"Player {player_a} not found")
        elif elo_b == -1:
            raise ValueError(f"Player {player_b} not found")

        ratings_a = 10 ** (elo_a / 400)
        ratings_b = 10 ** (elo_b / 400)
        expected_score_a = ratings_a / (ratings_a + ratings_b)
        expected_score_b = ratings_b / (ratings_a + ratings_b)

        if winner == player_a:
            score_a = 1
            score_b = 0
            self.players[index_a]['wins'] += 1
            self.players[index_b]['losses'] += 1
        elif winner == player_b:
            score_a = 0
            score_b = 1
            self.players[index_a]['losses'] += 1
            self.players[index_b]['wins'] += 1
        else:
            score_a = 0.5
            score_b = 0.5
            self.players[index_a]['draws'] += 1
            self.players[index_b]['draws'] += 1

        self.players[index_a]['elo'] += self.k * (score_a - expected_score_a)
        self.players[index_b]['elo'] += self.k * (score_b - expected_score_b)

        self._update_everything()

    def _update_everything(self) -> None:
        """Updates all Ranks and guarantees that Players don't get negative
        Elo.
        """
        for i in self.players:
            i['elo'] = int(i['elo'])
            if self.rankings:
                if i['elo'] >= 2400:
                    i['rank'] = "Grand Master"
                elif i['elo'] >= 2000:
                    i['rank'] = "Master"
                elif i['elo'] >= 1850:
                    i['rank'] = "Diamond"
                elif i['elo'] >= 1650:
                    i['rank'] = "Platinum"
                elif i['elo'] >= 1500:
                    i['rank'] = "Gold"
                elif i['elo'] >= 1300:
                    i['rank'] = "Silver"
                elif i['elo'] >= 1100:
                    i['rank'] = "Bronze"
                else:
                    i['rank'] = "Iron"
            i['elo'] = max(i['elo'], 0)


# Inspired by https://github.com/HankSheehan/EloPy
