import EloSystem from '../src/elo_system'

describe('Elo System without Ranking', () => {
  let exampleSystem: EloSystem

  beforeEach(() => {
    exampleSystem = new EloSystem()

    exampleSystem.add_player('Alice')
    exampleSystem.add_player('Bob', 1400)
  })

  it('Remove Player', () => {
    expect(exampleSystem.get_overall_list()).toEqual([
      {
        player: 'Bob',
        elo: 1400,
        wins: 0,
        losses: 0,
        draws: 0,
      },
      {
        player: 'Alice',
        elo: 1000,
        wins: 0,
        losses: 0,
        draws: 0,
      },
    ])

    exampleSystem.remove_player('Bob')

    expect(exampleSystem.get_overall_list()).toEqual([
      {
        player: 'Alice',
        elo: 1000,
        wins: 0,
        losses: 0,
        draws: 0,
      },
    ])
  })

  it('Elo Methods', () => {
    exampleSystem.add_elo('Bob', 100)
    expect(exampleSystem.get_player_elo('Bob')).toBe(1500)

    exampleSystem.set_elo('Bob', 1400)
    expect(exampleSystem.get_player_elo('Bob')).toBe(1400)

    exampleSystem.remove_elo('Bob', 100)
    expect(exampleSystem.get_player_elo('Bob')).toBe(1300)

    exampleSystem.reset_elo('Bob')
    expect(exampleSystem.get_player_elo('Bob')).toBe(exampleSystem.base_elo)
  })

  it('Get Methods', () => {
    exampleSystem.record_match({ winner: 'Alice', loser: 'Bob' })
    exampleSystem.record_match({ winner: 'Bob', loser: 'Alice' })
    exampleSystem.record_match({ winner: 'Alice', loser: 'Bob', draw: true })

    expect(exampleSystem.get_player_wins('Alice')).toBe(1)
    expect(exampleSystem.get_player_losses('Alice')).toBe(1)
    expect(exampleSystem.get_player_draws('Alice')).toBe(1)
    expect(exampleSystem.get_players_with_elo(1037)).toEqual(['Alice'])
    expect(exampleSystem.get_players_with_wins(1)).toEqual(['Alice', 'Bob'])
    expect(exampleSystem.get_players_with_losses(1)).toEqual(['Alice', 'Bob'])
    expect(exampleSystem.get_players_with_draws(1)).toEqual(['Alice', 'Bob'])
  })

  it('Player Count', () => {
    expect(exampleSystem.get_player_count()).toBe(2)
  })
})
