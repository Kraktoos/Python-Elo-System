import EloSystem from '../src/elo_system'

describe('Testing Elo System', () => {
  let exampleSystem: EloSystem

  beforeEach(() => {
    exampleSystem = new EloSystem()

    exampleSystem.add_player('Alice')
    exampleSystem.add_player('Bob', 1400)
  })

  it('Add Player', () => {
    expect(exampleSystem.get_overall_list()).toEqual([
      {
        name: 'Bob',
        elo: 1400,
        wins: 0,
        losses: 0,
        draws: 0,
      },
      {
        name: 'Alice',
        elo: 1000,
        wins: 0,
        losses: 0,
        draws: 0,
      },
    ])
  })

  it('Remove Player', () => {
    exampleSystem.remove_player('Bob')

    expect(exampleSystem.get_overall_list()).toEqual([
      {
        name: 'Alice',
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
    exampleSystem.record_match('Alice', 'Bob', 'Alice')
    exampleSystem.record_match('Alice', 'Bob', 'Bob')
    exampleSystem.record_match('Alice', 'Bob')

    expect(exampleSystem.get_player_wins('Alice')).toBe(1)
    expect(exampleSystem.get_player_losses('Alice')).toBe(1)
    expect(exampleSystem.get_player_draws('Alice')).toBe(1)
    expect(exampleSystem.get_players_with_elo(1037)).toEqual(['Alice'])
    expect(exampleSystem.get_players_with_wins(1)).toEqual(['Alice', 'Bob'])
    expect(exampleSystem.get_players_with_losses(1)).toEqual(['Alice', 'Bob'])
    expect(exampleSystem.get_players_with_draws(1)).toEqual(['Alice', 'Bob'])
  })

  it('Player Count', () => {
    expect(exampleSystem.size).toBe(2)
  })

  it('Python Error Behavior', () => {
    expect(() => {
      exampleSystem.remove_player('Charlie')
    }).toThrow(Error)

    expect(() => {
      exampleSystem.set_elo('Charlie', 100)
    }).toThrow(Error)

    expect(() => {
      exampleSystem.reset_elo('Charlie')
    }).toThrow(Error)

    expect(() => {
      exampleSystem.add_elo('Charlie', 100)
    }).toThrow(Error)

    expect(() => {
      exampleSystem.remove_elo('Charlie', 100)
    }).toThrow(Error)

    expect(() => {
      exampleSystem.get_player_elo('Charlie')
    }).toThrow(Error)

    expect(() => {
      exampleSystem.get_player_wins('Charlie')
    }).toThrow(Error)

    expect(() => {
      exampleSystem.get_player_losses('Charlie')
    }).toThrow(Error)

    expect(() => {
      exampleSystem.get_player_draws('Charlie')
    }).toThrow(Error)

    expect(() => {
      exampleSystem.record_match('Alice', 'Charlie')
    }).toThrow(Error)
  })
})
