"""
Created: 10/20/2021
Author: Kraktoos
"""
class EloSystem:
    """
    A class that represents an implementation of the Elo Rating System
    """
    def __init__(self, base_elo: int = 1000, k: int = 32):
        """
        Runs at Ini
        """
        self.base_elo = base_elo
        self.k = k
        self.players = []

    # Player Methods

    def add_player(self, player: str, elo: int = None):
        """
        Adds the Player to the Players List, as well as their Elo
        Paramaters: Player, Elo (optional)
        Returns: None
        """
        info = {}
        if elo == None:
            elo = self.base_elo
        info["player"] = player
        info["elo"] = elo
        info["rank"] = None
        self.players.append(info)
        self._update_everything()

    def remove_player(self, player: str):
        """
        Removes the Mentioned Player from the Players List
        Paramaters: Player
        Returns: None
        """
        for i in self.players:
            if i["player"] == player:
                self.players.remove(i)

    # Elo Methods

    def set_elo(self, player: str, elo: int):
        """
        Sets a Players Elo
        Paramaters: Player, Elo
        Returns: None
        """
        for i in self.players:
            if i["player"] == player:
                i["elo"] = int(elo)
        self._update_everything()

    def reset_elo(self, player: str):
        """
        Resets a Players Elo to the Base Elo
        Paramaters: Player
        Returns: None
        """
        for i in self.players:
            if i["player"] == player:
                i["elo"] = self.base_elo
        self._update_everything()

    def add_elo(self, player: str, elo: int):
        """
        Adds Elo to a Player
        Paramaters: Player, Elo
        Returns: None
        """
        for i in self.players:
            if i["player"] == player:
                i["elo"] += int(elo)
        self._update_everything()

    def remove_elo(self, player: str, elo: int):
        """
        Removes Elo of a Player
        Paramaters: Player, Elo
        Returns: None
        """
        for i in self.players:
            if i["player"] == player:
                i["elo"] -= int(elo)
        self._update_everything()

    # Return Methods

    def get_player_elo(self, player: str):
        """
        Returns the Player Elo
        Paramaters: Player
        Returns: Player Elo
        """
        for i in self.players:
            if i["player"] == player:
                return i["elo"]

    def get_player_rank(self, player: str):
        """
        Returns the Player Rank
        Paramaters: Player
        Returns: Player Rank
        """
        for i in self.players:
            if i["player"] == player:
                return i["rank"]

    def get_player_count(self):
        """
        Returns the Player Count
        Paramaters: None
        Returns: None
        """
        return len(self.players)

    # Return List Methods

    def get_overall_list(self):
        """
        Returns the Player, Elo and Ranks List
        Paramaters: None
        Returns: List of Dictionaries
        """
        elo_list = sorted(self.players, key=lambda d: d["elo"], reverse=True) 
        return elo_list

    def get_players_with_elo(self, elo: int):
        """
        Returns a List of Players with the given Elo
        Paramaters: Elo
        Returns: List
        """
        players = []
        for i in self.players:
            if i["elo"] == elo:
                players.append(i["player"])
        return players

    def get_players_with_rank(self, rank: str):
        """
        Returns a List of Players with the given Rank
        Paramaters: Rank
        Returns: List
        """
        players = []
        for i in self.players:
            if i["rank"] == rank:
                players.append(i["player"])
        return players

    # Main Matching System

    def record_match(self, player_a: str, player_b: str, winner: str = None):
        """
        Runs the Calculations and Updates the Score of both Player A and B Following a Simple Elo System
        Paramaters: Player A, Player B, Winner (if Winner is None it will be considered a draw)
        Returns: None
        """
        for i in self.players:
            if i["player"] == player_a:
                index_a = self.players.index(i)
                elo_a = i["elo"]
            elif i["player"] == player_b:
                index_b = self.players.index(i)
                elo_b = i["elo"]

        ra = 10**(elo_a/400)
        rb = 10**(elo_b/400)
        ea = ra / (ra + rb)
        eb = rb / (ra + rb)

        if winner == player_a:
            score_a = 1
            score_b = 0
        elif winner == player_b:
            score_a = 0
            score_b = 1
        else:
            score_a = 0.5
            score_b = 0.5

        self.players[index_a]["elo"] += self.k * (score_a - ea)
        self.players[index_b]["elo"] += self.k * (score_b - eb)

        self._update_everything()
    
    def _update_everything(self):
        """
        Updates All Ranks and Guarantees that Players don't get Negative Elo
        Paramaters: None
        Returns: None
        """
        for i in self.players:
            i["elo"] = int(i["elo"])
            if i["elo"] >= 2400:
                i["rank"] = "Grand Master"
            elif i["elo"] >= 2000:
                i["rank"] = "Master"
            elif i["elo"] >= 1850:
                i["rank"] = "Diamond"
            elif i["elo"] >= 1650:
                i["rank"] = "Platinum"
            elif i["elo"] >= 1500:
                i["rank"] = "Gold"
            elif i["elo"] >= 1300:
                i["rank"] = "Silver"
            elif i["elo"] >= 1100:
                i["rank"] = "Bronze"
            elif i["elo"] >= 0:
                i["rank"] = "Iron"
            else:
                i["rank"] = "Iron"
                i["elo"] = 0