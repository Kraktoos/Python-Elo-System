from elo_system.elo_system import EloSystem


def main():
    elo = EloSystem(base_elo=1200, k=42, rankings=True)

    elo.add_player("John", 2100)
    elo.add_player("Marcus", 1400)
    elo.add_player("CasualTryhard")
    elo.add_player("AnotherCasualTryhard")

    print(elo.get_player_elo("Marcus"))

    print(elo.get_overall_list())

    elo.record_match("John", "Marcus", winner="Marcus")

    print(elo.get_overall_list())

    elo.record_match("John", "CasualTryhard", winner="CasualTryhard")

    print(elo.get_overall_list())

    elo.record_match("CasualTryhard", "AnotherCasualTryhard",
                     winner="AnotherCasualTryhard")

    print(elo.get_overall_list())

    print(elo.get_player_rank("CasualTryhard"))

    print(elo.get_player_count())

    print(elo.get_players_with_rank("Bronze"))

    elo.remove_elo("Marcus", 100)

    print(elo.get_player_elo("Marcus"))


if __name__ == "__main__":
    main()
