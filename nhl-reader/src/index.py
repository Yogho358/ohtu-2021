from playerReader import PlayerReader
from playerStats import PlayerStats


def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

    # response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # #print(response)

    # players = []

    # for player_dict in response:
    #     player = Player(
    #         player_dict['name'],
    #         player_dict['nationality'],
    #         player_dict['assists'],
    #         player_dict['goals'],
    #         player_dict['penalties'],
    #         player_dict['team'],
    #         player_dict['games']

    #     )
    #     if player.nationality == "FIN":
    #         players.append(player)

    # print("Oliot:")

    # players.sort(key=lambda player: player.score,reverse=True)

    # for player in players:
    #     print(player)


if __name__ == "__main__":
    main()
