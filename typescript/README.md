# TypesScript/JavaScript Implementation - Elo Rating System

A port of Kraktoos's Python Implementation - Elo Rating System to
TypeScript/Javascript with improvements from the python fork.

## Examples

### Creating an Implementation

```javascript
import EloSystem from "elo_system"
elo = EloSystem({base_elo = 1000, k = 32}) // Base values for base_elo and k and has support for rankings
```

### Adding and Removing Players

```javascript
elo.add_player("John")
elo.add_player("Marcus", 1400)
console.log(elo.get_overall_list())
elo.remove_player("Marcus")
console.log(elo.get_overall_list())
```

```bash
[{'player': 'Marcus', 'elo': 1400, 'rank': 'Silver'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
[{'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
```

### Recording a Match

```javascript
elo.add_player("John")
elo.add_player("Marcus", 1400)
console.log(elo.get_overall_list())
elo.record_match({"Marcus", "John"})
console.log(elo.get_overall_list())
elo.record_match({"Marcus", "John"})
console.log(elo.get_overall_list())
elo.record_match({"Marcus", "John", True}) // When draw is passed true, regardless who is the winner, the match is a draw
console.log(elo.get_overall_list())
```

```bash
[{'player': 'Marcus', 'elo': 1400, 'rank': 'Silver'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
[{'player': 'Marcus', 'elo': 1402, 'rank': 'Silver'}, {'player': 'John', 'elo': 997, 'rank': 'Iron'}]
[{'player': 'Marcus', 'elo': 1372, 'rank': 'Silver'}, {'player': 'John', 'elo': 1026, 'rank': 'Iron'}]
[{'player': 'Marcus', 'elo': 1359, 'rank': 'Silver'}, {'player': 'John', 'elo': 1038, 'rank': 'Iron'}]
```

### Other Useful Methods

```javascript
elo.add_player("John")
elo.add_player("Marcus", 2400)
elo.add_player("James", 1000)
// There is also set_elo(), reset_elo(), add_elo(), remove_elo(), and get_wins(), etc...
console.log(elo.get_overall_list())
console.log(elo.get_player_elo("John"))
console.log(elo.get_player_rank("Marcus"))
console.log(elo.get_player_count())
console.log(elo.get_players_with_elo(1000))
console.log(elo.get_players_with_rank("Silver"))
```

```bash
[{'player': 'Marcus', 'elo': 2400, 'rank': 'Grand Master'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}, {'player': 'James', 'elo': 1000, 'rank': 'Iron'}]
1000
Grand Master
3
['John', 'James']
[]
```
