# Python Implementation - Elo Rating System

This is a fork of Python Implementation - Elo Rating System by Kraktoos and adds
the following features:

- Ranks has been removed.
- Win, lose and draw counts.
- Rewritten to use a player class to store statistics.

## Examples

### Creating an Implementation

```python
from elo_system import EloSystem
elo = EloSystem(base_elo = 1000, k = 32) # Base values for base_elo and k
```

### Adding and Removing Players

```python
# Adding players
>>> elo.add_player("John")
>>> elo.add_player("Marcus", 1400)
>>> print(elo.get_overall_list())
[{'player': 'Marcus', 'elo': 1400}, {'player': 'John', 'elo': 1000}]

# Removing Players
>>> elo.remove_player("Marcus")
>>> print(elo.get_overall_list())
[{'player': 'John', 'elo': 1000}]
```

### Recording a Match

```python
>>> elo.add_player("John")
>>> elo.add_player("Marcus", 1400)
>>> print(elo.get_overall_list())
[{'player': 'Marcus', 'elo': 1400}, {'player': 'John', 'elo': 1000}]

>>> elo.record_match(winner="Marcus", loser="John")
>>> print(elo.get_overall_list())
[{'player': 'Marcus', 'elo': 1402}, {'player': 'John', 'elo': 997}]

>>> elo.record_match(loser="Marcus", winner="John")
>>> print(elo.get_overall_list())
[{'player': 'Marcus', 'elo': 1372}, {'player': 'John', 'elo': 1026}]

# When draw is passed true, regardless who is the winner, the match is a draw
>>> elo.record_match(winner="Marcus", loser="John", draw=True)
>>> print(elo.get_overall_list())
[{'player': 'Marcus', 'elo': 1359}, {'player': 'John', 'elo': 1038}]
```

### Other Useful Methods

```python
>>> elo.add_player("John")
>>> elo.add_player("Marcus", 2400)
>>> elo.add_player("James", 1000)

# There is also set_elo(), reset_elo(), add_elo(), remove_elo(), and get_wins(), etc...
>>> print(elo.get_overall_list())
[{'player': 'Marcus', 'elo': 2400}, {'player': 'John', 'elo': 1000}, {'player': 'James', 'elo': 1000}]

>>> print(elo.get_player_elo("John"))
1000

>>> print(elo.get_player_count())
3

>>> print(elo.get_players_with_elo(1000))
['John', 'James']
```
