# Python Implementation - Elo Rating System
Yet another Python Implementation of the Elo rating system (how innovative am I right?).
Only supports 1vs1 games at the moment.
This whole mini-project/library was just made for me to practice my OOP.
I also added the ranking system just for fun.
## What is the Elo Rating System?
* The Elo rating system is a method for calculating the relative skill levels of players in zero-sum games such as chess. It is named after its creator Arpad Elo, a Hungarian-American physics professor.
## How does the Elo Rating System work? How do I calculate Elo?
Check these websites out if you want to learn more on how the Elo Rating System works!
* https://en.wikipedia.org/wiki/Elo_rating_system
* https://metinmediamath.wordpress.com/2013/11/27/how-to-calculate-the-elo-rating-including-example/
## Examples
#### Creating an Implementation
```python
from elo_system import *
elo = EloSystem(base_elo = 1000, k = 32) # There are the base values for base_elo and k however you can and may change them
```
#### Adding and Removing Players
```python
elo.add_player("John")
elo.add_player("Marcus", 1400)

print(elo.get_overall_list())

elo.remove_player("Marcus")

print(elo.get_overall_list())
```
```shell
[{'player': 'Marcus', 'elo': 1400, 'rank': 'Silver'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
[{'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
```
#### Recording a Match
```python
elo.add_player("John")
elo.add_player("Marcus", 1400)

print(elo.get_overall_list())

elo.record_match("Marcus", "John", "Marcus") # 3rd value is the winner

print(elo.get_overall_list())

elo.record_match("Marcus", "John", "John") # Now the winner is John

print(elo.get_overall_list())

elo.record_match("Marcus", "John") # When the winner is not specified, it is considered a draw

print(elo.get_overall_list())
```
```shell
[{'player': 'Marcus', 'elo': 1400, 'rank': 'Silver'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}]
[{'player': 'Marcus', 'elo': 1402, 'rank': 'Silver'}, {'player': 'John', 'elo': 997, 'rank': 'Iron'}] 
[{'player': 'Marcus', 'elo': 1372, 'rank': 'Silver'}, {'player': 'John', 'elo': 1026, 'rank': 'Iron'}]
[{'player': 'Marcus', 'elo': 1359, 'rank': 'Silver'}, {'player': 'John', 'elo': 1038, 'rank': 'Iron'}]
```
#### Other Useful Methods
```python
elo.add_player("John")
elo.add_player("Marcus", 2400)
elo.add_player("James", 1000)

# There is also set_elo(), reset_elo(), add_elo() and remove_elo()

print(elo.get_overall_list())

print(elo.get_player_elo("John"))

print(elo.get_player_rank("Marcus"))

print(elo.get_player_count())

print(elo.get_players_with_elo(1000))

print(elo.get_players_with_rank("Silver"))
```
```shell
[{'player': 'Marcus', 'elo': 2400, 'rank': 'Grand Master'}, {'player': 'John', 'elo': 1000, 'rank': 'Iron'}, {'player': 'James', 'elo': 1000, 'rank': 'Iron'}]
1000
Grand Master
3
['John', 'James']
[]
```
