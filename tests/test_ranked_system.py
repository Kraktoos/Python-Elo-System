import pytest


from elo_system.elo_system import EloSystem


@pytest.fixture
def ranked_system() -> EloSystem:
    elo = EloSystem(rankings=True)

    elo.add_player("Alice")

    return elo


def test_ranking(ranked_system: EloSystem):
    assert ranked_system.get_overall_list() == [
        {
            "player": "Alice",
            "elo": 1000,
            "wins": 0,
            "losses": 0,
            "draws": 0,
            "rank": "Iron",
        }
    ]


def test_ranked_elo_methods(ranked_system: EloSystem):
    ranked_system.add_elo("Alice", 300)
    assert ranked_system.get_player_rank("Alice") == "Silver"

    ranked_system.remove_elo("Alice", 200)
    assert ranked_system.get_player_rank("Alice") == "Bronze"


def test_get_methods(ranked_system: EloSystem):
    assert ranked_system.get_player_rank("Alice") == "Iron"
    assert ranked_system.get_players_with_rank("Iron") == ["Alice"]


@pytest.mark.parametrize(
    "elo, rank",
    [
        (1500, "Gold"),
        (1650, "Platinum"),
        (1850, "Diamond"),
        (2000, "Master"),
        (2400, "Grand Master"),
    ],
)
def test_all_ranks(ranked_system: EloSystem, elo: int, rank: str):
    ranked_system.set_elo("Alice", elo)
    assert ranked_system.get_player_rank("Alice") == rank
