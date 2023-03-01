class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name):
        for plr in self.__players:
            if player_name == plr.name:
                return self.__players.pop(self.__players.index(plr))
        return f"Player {player_name} not found"
