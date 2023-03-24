# Python Implementation - Elo Rating System

This is a fork of Python Implementation - Elo Rating System by Kraktoos and adds
the following features:

- Ranks can be turned on or off.
- Win, lose and draw counts.
- Uses hatch instead of setup.py for packaging.
- Rewritten to use a player class instead of a dictionary to store statistics.
- Use a dictionary as a record for players and statistics instead of a list.
- Use argument keywords to set winner, loser and draws.

## Examples

### Creating an Implementation

```python
from elo_system import EloSystem
elo = EloSystem(base_elo = 1000, k = 32) # Base values for base_elo and k and has support for rankings
```

### Adding and Removing Players

```python
elo.add_player("John")
elo.add_player("Marcus", 1400)
print(elo.get_overall_list())
elo.remove_player("Marcus")
print(elo.get_overall_list())
```

```bash
[{'player': 'Marcus', 'elo': 1400, 'rank': 'Silver'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
[{'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
```

### Recording a Match

```python
elo.add_player("John")
elo.add_player("Marcus", 1400)
print(elo.get_overall_list())
elo.record_match(winner="Marcus", loser="John")
print(elo.get_overall_list())
elo.record_match(loser="Marcus", winner="John")
print(elo.get_overall_list())
elo.record_match(winner="Marcus", loser="John", draw=True) # When draw is passed true, regardless who is the winner, the match is a draw
print(elo.get_overall_list())
```

```bash
[{'player': 'Marcus', 'elo': 1400, 'rank': 'Silver'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
[{'player': 'Marcus', 'elo': 1402, 'rank': 'Silver'}, {'player': 'John', 'elo': 997, 'rank': 'Iron'}]
[{'player': 'Marcus', 'elo': 1372, 'rank': 'Silver'}, {'player': 'John', 'elo': 1026, 'rank': 'Iron'}]
[{'player': 'Marcus', 'elo': 1359, 'rank': 'Silver'}, {'player': 'John', 'elo': 1038, 'rank': 'Iron'}]
```

### Other Useful Methods

```python
elo.add_player("John")
elo.add_player("Marcus", 2400)
elo.add_player("James", 1000)
# There is also set_elo(), reset_elo(), add_elo(), remove_elo(), and get_wins(), etc...
print(elo.get_overall_list())
print(elo.get_player_elo("John"))
print(elo.get_player_rank("Marcus"))
print(elo.get_player_count())
print(elo.get_players_with_elo(1000))
print(elo.get_players_with_rank("Silver"))
```

```bash
[{'player': 'Marcus', 'elo': 2400, 'rank': 'Grand Master'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}, {'player': 'James', 'elo': 1000, 'rank': 'Iron'}]
1000
Grand Master
3
['John', 'James']
[]
```
