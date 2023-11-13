from player_reader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, country):
        def sort_by(player):
            return player.points
        
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by
        )

        def filterBy(player):
            if player.nationality == country:
                return True
            else:
                return False
        
        filtered_players = filter(filterBy, sorted_players)
        
        return filtered_players