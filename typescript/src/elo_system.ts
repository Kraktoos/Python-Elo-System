/*! SPDX-FileCopyrightText: 2023 Samuel Wu
 *
 * SPDX-License-Identifier: MIT
 */

import Player, { type PlayerStatistics } from './player'

export interface MatchRecord {
  winner: string
  loser: string
  draw?: boolean
}

export default class EloSystem {
  base_elo: number
  k_factor: number
  rankings: boolean
  players: Map<string, Player>

  constructor({ baseElo = 1000, kFactor = 32, rankings = false } = {}) {
    this.base_elo = baseElo
    this.k_factor = kFactor
    this.rankings = rankings
    this.players = new Map<string, Player>()
  }

  /* Player Methods */

  add_player(player: string, elo?: number) {
    if (elo === undefined) elo = this.base_elo

    this.players.set(player, new Player(elo))

    if (this.rankings) this.players.get(player)!.calculate_rank()
  }

  remove_player(player: string) {
    this.players.delete(player)
  }

  /* Elo Methods */

  set_elo(player: string, elo: number) {
    this.players.get(player)!.elo = elo

    if (this.rankings) this.players.get(player)!.calculate_rank()
  }

  reset_elo(player: string) {
    this.players.get(player)!.elo = this.base_elo

    if (this.rankings) this.players.get(player)!.calculate_rank()
  }

  add_elo(player: string, elo: number) {
    this.players.get(player)!.elo += elo

    if (this.rankings) this.players.get(player)!.calculate_rank()
  }

  remove_elo(player: string, elo: number) {
    this.players.get(player)!.elo -= elo

    if (this.rankings) this.players.get(player)!.calculate_rank()
  }

  /* Return Methods */
  get_player_elo(player: string) {
    return this.players.get(player)!.elo
  }

  get_player_rank(player: string): string | undefined {
    return this.players.get(player)!.rank
  }

  get_player_wins(player: string) {
    return this.players.get(player)!.wins
  }

  get_player_losses(player: string) {
    return this.players.get(player)!.losses
  }

  get_player_draws(player: string) {
    return this.players.get(player)!.draws
  }

  get_player_count() {
    return this.players.size
  }

  /* Return List Methods */

  get_overall_list() {
    const players: PlayerStatistics[] = []
    this.players.forEach((stats: Player, player: string) => {
      players.push({ player, ...stats })
    })

    return players.sort(
      (a: PlayerStatistics, b: PlayerStatistics) => b.elo - a.elo
    )
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

  get_players_with_rank(rank: string) {
    const players: string[] = []
    this.players.forEach((stats: Player, player: string) => {
      if (stats.rank === rank) {
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

  record_match({ winner, loser, draw = false }: MatchRecord) {
    const playerA = this.players.get(winner)!
    const playerB = this.players.get(loser)!

    const ratingsA = 10 ** (playerA.elo / 400)
    const ratingsB = 10 ** (playerB.elo / 400)
    const expectedScoreA = ratingsA / (ratingsA + ratingsB)
    const expectedScoreB = ratingsB / (ratingsA + ratingsB)

    if (draw) {
      playerA.draws += 1
      playerB.draws += 1
      playerA.elo += Math.floor(this.k_factor * (0.5 - expectedScoreA))
      playerB.elo += Math.floor(this.k_factor * (0.5 - expectedScoreB))
    } else {
      playerA.wins += 1
      playerB.losses += 1
      playerA.elo += Math.floor(this.k_factor * (1 - expectedScoreA))
      playerB.elo += Math.floor(this.k_factor * (0 - expectedScoreB))
    }

    playerA.elo = Math.max(playerA.elo, 0)
    playerB.elo = Math.max(playerB.elo, 0)
  }
}
