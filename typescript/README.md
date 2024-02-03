# TypesScript/JavaScript Implementation - Elo Rating System

A port of Kraktoos's Python Implementation - Elo Rating System to
TypeScript/Javascript with improvements from the python fork.

## Examples

### Creating an Implementation

```javascript
import EloSystem from "elo_system"
// Base values for base_elo and k and has support for rankings
elo = EloSystem(1000, 32)
```

### Adding and Removing Players

```javascript
> elo.add_player("John")
> elo.add_player("Marcus", 1400)
> console.log(elo.get_overall_list())
[{'name': 'Marcus', 'elo': 1400}, {'name': 'John', 'elo': 1000}]

> elo.remove_player("Marcus")
> console.log(elo.get_overall_list())
[{'name': 'John', 'elo': 1000}]
```

### Recording a Match

```javascript
> elo.add_player("John")
> elo.add_player("Marcus", 1400)
> console.log(elo.get_overall_list())
[{'name': 'Marcus', 'elo': 1400}, {'name': 'John', 'elo': 1000}]

> elo.record_match("Marcus", "John", "Marcus")
> console.log(elo.get_overall_list())
[{'name': 'Marcus', 'elo': 1402}, {'name': 'John', 'elo': 997}]

> elo.record_match("Marcus", "John", "John")
> console.log(elo.get_overall_list())
[{'name': 'Marcus', 'elo': 1372}, {'name': 'John', 'elo': 1026}]

> elo.record_match("Marcus", "John")
> console.log(elo.get_overall_list())
[{'name': 'Marcus', 'elo': 1359}, {'name': 'John', 'elo': 1038}]
```

### Other Useful Methods

```javascript
> elo.add_player("John")
> elo.add_player("Marcus", 2400)
> elo.add_player("James", 1000)

// There is also set_elo(), reset_elo(), add_elo(), remove_elo(), and get_wins(), etc...
> console.log(elo.get_overall_list())
[{'name': 'Marcus', 'elo': 2400}, {'name': 'John', 'elo': 1000}, {'name': 'James', 'elo': 1000}]

> console.log(elo.get_player_elo("John"))
1000

> console.log(elo.get_player_count())
3

> console.log(elo.get_players_with_elo(1000))
['John', 'James']
```

## License

This implementation is licensed under the MIT License.
