import EloSystem from '../src/elo_system'

describe('Elo System with Ranking', () => {
  let rankedSystem: EloSystem

  beforeEach(() => {
    rankedSystem = new EloSystem({ rankings: true })

    rankedSystem.add_player('Alice')
  })

  it('Ranking', () => {
    expect(rankedSystem.get_overall_list()).toEqual([
      {
        player: 'Alice',
        elo: 1000,
        wins: 0,
        losses: 0,
        draws: 0,
        rank: 'Iron',
      },
    ])
  })

  it('Ranked Elo Methods', () => {
    rankedSystem.add_elo('Alice', 300)
    expect(rankedSystem.get_player_rank('Alice')).toStrictEqual('Silver')

    rankedSystem.remove_elo('Alice', 200)
    expect(rankedSystem.get_player_rank('Alice')).toStrictEqual('Bronze')

    rankedSystem.reset_elo('Alice')
    expect(rankedSystem.get_player_rank('Alice')).toStrictEqual('Iron')
  })

  it('Get Methods', () => {
    expect(rankedSystem.get_players_with_rank('Iron')).toEqual(['Alice'])
  })

  const cases = [
    { elo: 1500, rank: 'Gold' },
    { elo: 1650, rank: 'Platinum' },
    { elo: 1850, rank: 'Diamond' },
    { elo: 2000, rank: 'Master' },
    { elo: 2400, rank: 'Grand Master' },
  ]
  it.each(cases)('All Ranks', ({ elo, rank }) => {
    rankedSystem.set_elo('Alice', elo)
    expect(rankedSystem.get_player_rank('Alice')).toStrictEqual(rank)
  })
})
