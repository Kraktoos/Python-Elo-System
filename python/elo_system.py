from math import floor

from attrs import asdict, define, field, frozen


@define
class Player:
    elo: int
    wins: int = 0
    losses: int = 0
    draws: int = 0


@frozen
class EloSystem:
    base_elo: int = 1000
    k_factor: int = 32
    players: dict[str, Player] = field(factory=dict)

    def __len__(self):
        """Get the number of players in the system using `len`.

        Returns:
            int: Number of players
        """
        return len(self.players)

    # Player Methods

    def add_player(self, name: str, elo: int | None = None):
        if elo is None:
            elo = self.base_elo

        self.players[name] = Player(elo)

    def remove_player(self, name: str):
        del self.players[name]

    # Elo Methods

    def set_elo(self, name: str, elo: int):
        self.players[name].elo = elo

    def add_elo(self, name: str, elo: int):
        self.players[name].elo += elo

    def remove_elo(self, name: str, elo: int):
        self.players[name].elo -= elo

    def reset_elo(self, name: str):
        self.players[name].elo = self.base_elo

    # Return Methods

    def get_player_elo(self, name: str):
        return self.players[name].elo

    def get_player_wins(self, name: str):
        return self.players[name].wins

    def get_player_losses(self, name: str):
        return self.players[name].losses

    def get_player_draws(self, name: str):
        return self.players[name].draws

    # Return List Methods

    def get_overall_list(self):
        players: list[dict[str, int | str]] = []

        for name, player in self.players.items():
            dictionary: dict[str, int | str] = {"player": name}
            dictionary.update(asdict(player))
            players.append(dictionary)

        return sorted(players, key=lambda d: d["elo"], reverse=True)

    def get_players_with_elo(self, elo: int):
        return [
            name for name, player in self.players.items() if player.elo == elo
        ]

    def get_players_with_wins(self, wins: int):
        return [
            name
            for name, player in self.players.items()
            if player.wins == wins
        ]

    def get_players_with_losses(self, losses: int):
        return [
            name
            for name, player in self.players.items()
            if player.losses == losses
        ]

    def get_players_with_draws(self, draws: int):
        return [
            name
            for name, player in self.players.items()
            if player.draws == draws
        ]

    # Main Matching System

    def record_match(
        self, player_a: str, player_b: str, winner: str | None = None
    ) -> None:
        elo_a = self.players[player_a].elo
        elo_b = self.players[player_b].elo

        ratings_a = 10 ** (elo_a / 400)
        ratings_b = 10 ** (elo_b / 400)
        expected_score_a = ratings_a / (ratings_a + ratings_b)
        expected_score_b = ratings_b / (ratings_a + ratings_b)

        if winner == player_a:
            score_a = 1
            score_b = 0
            self.players[player_a].wins += 1
            self.players[player_b].losses += 1
        elif winner == player_b:
            score_a = 0
            score_b = 1
            self.players[player_a].losses += 1
            self.players[player_b].wins += 1
        else:
            score_a = 0.5
            score_b = 0.5
            self.players[player_a].draws += 1
            self.players[player_b].draws += 1

        self.players[player_a].elo += floor(
            self.k_factor * (score_a - expected_score_a)
        )
        self.players[player_b].elo += floor(
            self.k_factor * (score_b - expected_score_b)
        )

        self.players[player_a].elo = max(self.players[player_a].elo, 0)
        self.players[player_b].elo = max(self.players[player_b].elo, 0)
