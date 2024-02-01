from pytest import fixture

from elo_system import EloSystem


@fixture
def example_system():
    elo = EloSystem()

    elo.add_player("Alice")
    elo.add_player("Bob", 1400)

    return elo


def test_add_player(example_system: EloSystem):
    assert example_system.get_overall_list() == [
        {"player": "Bob", "elo": 1400, "wins": 0, "losses": 0, "draws": 0},
        {"player": "Alice", "elo": 1000, "wins": 0, "losses": 0, "draws": 0},
    ]


def test_remove_player(example_system: EloSystem):
    example_system.remove_player("Bob")

    assert example_system.get_overall_list() == [
        {"player": "Alice", "elo": 1000, "wins": 0, "losses": 0, "draws": 0},
    ]


def test_elo_functions(example_system: EloSystem):
    example_system.add_elo("Bob", 100)
    assert example_system.get_player_elo("Bob") == 1500

    example_system.set_elo("Bob", 2000)
    assert example_system.get_player_elo("Bob") == 2000

    example_system.remove_elo("Bob", 100)
    assert example_system.get_player_elo("Bob") == 1900

    example_system.reset_elo("Bob")
    assert example_system.get_player_elo("Bob") == example_system.base_elo


def test_get_methods(example_system: EloSystem):
    example_system.record_match("Alice", "Bob", "Alice")
    example_system.record_match("Alice", "Bob", "Bob")
    example_system.record_match("Alice", "Bob")

    assert example_system.get_player_wins("Alice") == 1
    assert example_system.get_player_losses("Alice") == 1
    assert example_system.get_player_draws("Alice") == 1
    assert example_system.get_players_with_elo(1037) == ["Alice"]
    assert example_system.get_players_with_wins(1) == ["Alice", "Bob"]
    assert example_system.get_players_with_losses(1) == ["Alice", "Bob"]
    assert example_system.get_players_with_draws(1) == ["Alice", "Bob"]


def test_player_count(example_system: EloSystem):
    assert len(example_system) == 2
