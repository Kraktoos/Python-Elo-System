/*! SPDX-FileCopyrightText: 2023-2024 Samuel Wu
 *
 * SPDX-License-Identifier: MIT
 */

export default class Player {
  name?: string
  elo: number
  wins: number
  losses: number
  draws: number

  constructor(elo: number) {
    this.elo = elo
    this.wins = 0
    this.losses = 0
    this.draws = 0
  }
}
