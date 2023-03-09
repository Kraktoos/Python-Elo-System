import pytest

from elo_system.elo_system import EloSystem


@pytest.fixture
def example_system() -> EloSystem:
    """Create an EloSystem with two Players for testing.

    Returns:
        EloSystem: An EloSystem with two Players.
    """
    elo = EloSystem()

    elo.add_player("Alice")
    elo.add_player("Bob", 1400)

    return elo


def test_remove_player(example_system: EloSystem):
    assert example_system.get_overall_list() == [
        {
            'player': 'Bob',
            'elo': 1400,
            'wins': 0,
            'losses': 0,
            'draws': 0,
        },
        {
            'player': 'Alice',
            'elo': 1000,
            'wins': 0,
            'losses': 0,
            'draws': 0,
        },
    ]

    example_system.remove_player("Bob")

    assert example_system.get_overall_list() == [
        {
            'player': 'Alice',
            'elo': 1000,
            'wins': 0,
            'losses': 0,
            'draws': 0,
        }
    ]


@pytest.mark.parametrize(
    "function, elo, expected",
    [
        ("add_elo", 100, 1100),
        ("remove_elo", 100, 900),
    ],
)
def test_add_remove_elo(example_system: EloSystem, function, elo, expected):
    eval(f"example_system.{function}('Alice', {elo})")
    assert example_system.get_player_elo("Alice") == expected


@pytest.mark.parametrize(
    "function, input, expected",
    [
        ("get_player_wins", "'Alice'", 1),
        ("get_player_losses", "'Alice'", 1),
        ("get_player_draws", "'Alice'", 1),
        ("get_players_with_elo", 1037, ['Alice']),
        ("get_players_with_wins", 1, ['Alice', 'Bob']),
        ("get_players_with_losses", 1, ['Alice', 'Bob']),
        ("get_players_with_draws", 1, ['Alice', 'Bob']),
    ],
)
def test_get_methods(example_system: EloSystem, function, input, expected):
    example_system.record_match("Alice", "Bob", "Alice")
    example_system.record_match("Alice", "Bob", "Bob")
    example_system.record_match("Alice", "Bob")
    assert eval(f"example_system.{function}({input})") == expected


@pytest.mark.parametrize(
    "function",
    [
        ("get_player_wins"),
        ("get_player_losses"),
        ("get_player_draws"),
        ("get_player_elo"),
        ("reset_elo"),
        ("remove_player"),
    ],
)
def test_raises_valueerror_singleparam(example_system: EloSystem, function):
    with pytest.raises(ValueError):
        eval(f"example_system.{function}('Charlie')")


@pytest.mark.parametrize(
    "function, input_one, input_two",
    [
        ("record_match", "'Charlie'", "'Alice'"),
        ("record_match", "'Alice'", "'Charlie'"),
        ("set_elo", "'Charlie'", 100),
        ("add_elo", "'Charlie'", 100),
        ("remove_elo", "'Charlie'", 100),
    ],
)
def test_raises_valueerror_doubleparam(
    example_system: EloSystem, function, input_one, input_two
):
    with pytest.raises(ValueError):
        eval(f"example_system.{function}({input_one}, {input_two})")


def test_set_reset_elo_and_len(example_system: EloSystem):
    for i in range(49):
        example_system.set_elo("Alice", 50 * i)
        assert example_system.get_player_elo("Alice") == 50 * i

    example_system.reset_elo("Alice")
    assert example_system.get_player_elo("Alice") == 1000

    assert example_system.get_player_count() == 2
