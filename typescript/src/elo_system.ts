import Player from './player'

export default class EloSystem {
  base_elo: number
  k_factor: number
  players: Map<string, Player>
  size = 0

  constructor(baseElo = 1000, kFactor = 32) {
    this.base_elo = baseElo
    this.k_factor = kFactor
    this.players = new Map()
  }

  /* Player Methods */

  add_player(name: string, elo?: number) {
    if (elo === undefined) elo = this.base_elo

    this.players.set(name, new Player(elo))
    this.size = this.players.size
  }

  remove_player(name: string) {
    const hasBeenDeleted = this.players.delete(name)

    if (!hasBeenDeleted) {
      throw Error(`KeyError: '${name}'`)
    }

    this.size = this.players.size
  }

  /* Elo Methods */

  set_elo(name: string, elo: number) {
    const player = this.players.get(name)

    if (!player) {
      throw Error(`KeyError: '${name}'`)
    }

    player.elo = elo
  }

  reset_elo(name: string) {
    const player = this.players.get(name)

    if (!player) {
      throw Error(`KeyError: '${name}'`)
    }

    player.elo = this.base_elo
  }

  add_elo(name: string, elo: number) {
    const player = this.players.get(name)

    if (!player) {
      throw Error(`KeyError: '${name}'`)
    }

    player.elo += elo
  }

  remove_elo(name: string, elo: number) {
    const player = this.players.get(name)

    if (!player) {
      throw Error(`KeyError: '${name}'`)
    }

    player.elo -= elo
  }

  /* Return Methods */

  get_player_elo(name: string) {
    const player = this.players.get(name)

    if (!player) {
      throw Error(`KeyError: '${name}'`)
    }

    return player.elo
  }

  get_player_wins(name: string) {
    const player = this.players.get(name)

    if (!player) {
      throw Error(`KeyError: '${name}'`)
    }

    return player.wins
  }

  get_player_losses(name: string) {
    const player = this.players.get(name)

    if (!player) {
      throw Error(`KeyError: '${name}'`)
    }

    return player.losses
  }

  get_player_draws(name: string) {
    const player = this.players.get(name)

    if (!player) {
      throw Error(`KeyError: '${name}'`)
    }

    return player.draws
  }

  /* Return List Methods */

  get_overall_list() {
    const players: Player[] = []

    this.players.forEach((stats, name) => {
      players.push({ ...stats, name })
    })

    return players.sort((player_a, player_b) => player_b.elo - player_a.elo)
  }

  get_players_with_elo(elo: number) {
    const players: string[] = []
    this.players.forEach((stats: Player, player: string) => {
      if (stats.elo === elo) {
        players.push(player)
      }
    })
    return players
  }

  get_players_with_wins(wins: number) {
    const players: string[] = []
    this.players.forEach((stats: Player, player: string) => {
      if (stats.wins === wins) {
        players.push(player)
      }
    })
    return players
  }

  get_players_with_losses(losses: number) {
    const players: string[] = []
    this.players.forEach((stats: Player, player: string) => {
      if (stats.losses === losses) {
        players.push(player)
      }
    })
    return players
  }

  get_players_with_draws(draws: number) {
    const players: string[] = []
    this.players.forEach((stats: Player, player: string) => {
      if (stats.draws === draws) {
        players.push(player)
      }
    })
    return players
  }

  /* Main Matching System */

  record_match(player_a: string, player_b: string, winner?: string) {
    const playerA = this.players.get(player_a)
    const playerB = this.players.get(player_b)

    if (!playerA) {
      throw Error(`KeyError: '${playerA}'`)
    }

    if (!playerB) {
      throw Error(`KeyError: '${playerB}'`)
    }

    const ratingsA = 10 ** (playerA.elo / 400)
    const ratingsB = 10 ** (playerB.elo / 400)
    const expectedScoreA = ratingsA / (ratingsA + ratingsB)
    const expectedScoreB = ratingsB / (ratingsA + ratingsB)

    let score_a: number
    let score_b: number

    if (winner === player_a) {
      score_a = 1
      score_b = 0
      playerA.wins += 1
      playerB.losses += 1
    } else if (winner === player_b) {
      score_a = 0
      score_b = 1
      playerA.losses += 1
      playerB.wins += 1
    } else {
      score_a = 0.5
      score_b = 0.5
      playerA.draws += 1
      playerB.draws += 1
    }

    playerA.elo += Math.floor(this.k_factor * (score_a - expectedScoreA))
    playerB.elo += Math.floor(this.k_factor * (score_b - expectedScoreB))

    playerA.elo = Math.max(playerA.elo, 0)
    playerB.elo = Math.max(playerB.elo, 0)
  }
}
