from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        for a_player in self.players:
            if a_player.username == player.username:
                raise  ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1


    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        for a_player in self.players:
            if a_player.username == player:
                self.players.remove(a_player)
                self.count -= 1

    def find(self, username: str):
        for a_player in self.players:
            if a_player.username == username:
                return a_player


