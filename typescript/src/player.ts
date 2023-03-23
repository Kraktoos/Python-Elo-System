export default class Player {
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
    if (this.elo >= 2400) { this.rank = 'Grand Master' } else if (this.elo >= 2000) { this.rank = 'Master' } else if (this.elo >= 1850) { this.rank = 'Diamond' } else if (this.elo >= 1650) { this.rank = 'Platinum' } else if (this.elo >= 1500) { this.rank = 'Gold' } else if (this.elo >= 1300) { this.rank = 'Silver' } else if (this.elo >= 1100) { this.rank = 'Bronze' } else { this.rank = 'Iron' }
  }

  as_dict (): { elo: number, wins: number, losses: number, draws: number } {
    let dictionary = {
      elo: this.elo,
      wins: this.wins,
      losses: this.losses,
      draws: this.draws
    }

    if (this.rank == null) {
      const rank = { rank: this.rank }
      dictionary = { ...dictionary, ...rank }
    }

    return dictionary
  }
}
