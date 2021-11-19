from playerReader import PlayerReader

class PlayerStats:
    def __init__(self,reader:PlayerReader):
        self.reader = reader
        self.players = self.reader.get_players()
        
    def top_scorers_by_nationality(self, nationality):
        self.players.sort(key = lambda player: player.score, reverse = True)
        return filter(lambda player: player.nationality == nationality, self.players)
        