
class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if not player in self.players:
            if player.guild == "Unaffiliated":
                self.players.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {self.name}"
            else:
                return f"Player {player.name} is in another guild."

        else:
            return f"Player {player.name} is already in the guild."

    def kick_player(self, player_name):
        for plr in self.players:
            if plr.name == player_name:
                self.players.remove(plr)
                plr.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = ""
        result += f"Guild: {self.name}\n"
        for plr in self.players:
            result += f"{plr.player_info()}\n"
        return result

