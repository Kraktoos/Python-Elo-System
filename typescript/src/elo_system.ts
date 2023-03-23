import Player from './player'

interface MatchRecord { winner: string, loser: string, draw: boolean }

type PlayerStatistics = {
  elo: number
  wins: number
  losses: number
  draws: number
  player: string
}

export type PlayerList = Array<PlayerStatistics>

export default class EloSystem {
  base_elo: number
  k_factor: number
  rankings: boolean
  players: Record<string, Player>

  constructor (baseElo = 1000, kFactor = 32, { rankings = false } = {}) {
    this.base_elo = baseElo
    this.k_factor = kFactor
    this.rankings = rankings
    this.players = {}
  }

  /* Player Methods */

  add_player (player: string, elo?: number): void {
    if (elo == null) elo = this.base_elo

    this.players[player] = new Player(elo)

    if (this.rankings) this.players[player].calculate_rank()
  }

  remove_player (player: string): void {
    // eslint-disable-next-line @typescript-eslint/no-dynamic-delete
    delete this.players[player]
  }

  /* Elo Methods */

  set_elo (player: string, elo: number): void {
    this.players[player].elo = elo

    if (this.rankings) this.players[player].calculate_rank()
  }

  reset_elo (player: string): void {
    this.players[player].elo = this.base_elo
  }

  add_elo (player: string, elo: number): void {
    this.players[player].elo += elo

    if (this.rankings) this.players[player].calculate_rank()
  }

  remove_elo (player: string, elo: number): void {
    this.players[player].elo -= elo

    if (this.rankings) this.players[player].calculate_rank()
  }

  /* Return Methods */
  get_player_elo (player: string): number {
    return this.players[player].elo
  }

  get_player_rank (player: string): string | undefined {
    return this.players[player].rank
  }

  get_player_wins (player: string): number {
    return this.players[player].wins
  }

  get_player_losses (player: string): number {
    return this.players[player].losses
  }

  get_player_draws (player: string): number {
    return this.players[player].draws
  }

  get_player_count (): number {
    return Object.keys(this.players).length
  }

  /* Return List Methods */

  get_overall_list (): PlayerList {
    return Object.entries(this.players).map((player: [string, Player]) => {
      return { player: player[0], ...player[1].as_dict() }
    }).sort((a: PlayerStatistics, b: PlayerStatistics) => b.elo - a.elo)
  }

  get_players_with_elo (elo: number): string[] {
    const players = []
    for (const [player, stats] of Object.entries(this.players)) {
      if (stats.elo === elo) {
        players.push(player)
      }
    }
    return players
  }

  get_players_with_rank (rank: string): string[] {
    const players = []
    for (const [player, stats] of Object.entries(this.players)) {
      if (stats.rank === rank) {
        players.push(player)
      }
    }
    return players
  }

  get_players_with_wins (wins: number): string[] {
    const players = []
    for (const [player, stats] of Object.entries(this.players)) {
      if (stats.wins === wins) {
        players.push(player)
      }
    }
    return players
  }

  get_players_with_losses (losses: number): string[] {
    const players = []
    for (const [player, stats] of Object.entries(this.players)) {
      if (stats.losses === losses) {
        players.push(player)
      }
    }
    return players
  }

  get_players_with_draws (draws: number): string[] {
    const players = []
    for (const [player, stats] of Object.entries(this.players)) {
      if (stats.draws === draws) {
        players.push(player)
      }
    }
    return players
  }

  /* Main Matching System */

  record_match ({ winner, loser, draw = false }: MatchRecord): void {
    const playerA = this.players[winner]
    const playerB = this.players[loser]

    const ratingsA = 10 ** (playerA.elo / 400)
    const ratingsB = 10 ** (playerB.elo / 400)
    const expectedScoreA = ratingsA / (ratingsA + ratingsB)
    const expectedScoreB = ratingsB / (ratingsA + ratingsB)

    if (draw) {
      playerA.draws += 1
      playerB.draws += 1
      this.add_elo(winner, Math.floor(this.k_factor * (0.5 - expectedScoreA)))
      this.add_elo(loser, Math.floor(this.k_factor * (0.5 - expectedScoreB)))
    } else {
      playerA.wins += 1
      playerB.losses += 1
      this.add_elo(winner, Math.floor(this.k_factor * (1 - expectedScoreA)))
      this.add_elo(loser, Math.floor(this.k_factor * (0 - expectedScoreB)))
    }
  }
}
