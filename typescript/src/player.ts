export interface PlayerStatistics {
  player?: string
  elo: number
  wins: number
  losses: number
  draws: number
  rank?: string
}

export default class Player implements PlayerStatistics {
  elo: number
  wins: number
  losses: number
  draws: number
  rank?: string

  constructor (elo: number) {
    this.elo = elo
    this.wins = 0
    this.losses = 0
    this.draws = 0
  }

  calculate_rank (): void {
    if (this.elo >= 2400) {
      this.rank = 'Grand Master'
    } else if (this.elo >= 2000) {
      this.rank = 'Master'
    } else if (this.elo >= 1850) {
      this.rank = 'Diamond'
    } else if (this.elo >= 1650) {
      this.rank = 'Platinum'
    } else if (this.elo >= 1500) {
      this.rank = 'Gold'
    } else if (this.elo >= 1300) {
      this.rank = 'Silver'
    } else if (this.elo >= 1100) {
      this.rank = 'Bronze'
    } else {
      this.rank = 'Iron'
    }
  }
}
