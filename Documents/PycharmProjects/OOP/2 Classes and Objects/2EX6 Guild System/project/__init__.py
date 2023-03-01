from project.player import Player
from project.guild import Guild

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Shield Break", 20))
print(player.add_skill("Some Skill", 50))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
second_player = Player("Tommy", 100, 100)
print(second_player.player_info())
print(guild.assign_player(second_player))
print(guild.guild_info())
second_guild = Guild("GPT")
third_player = Player("Mark", 20, 70)
print(third_player.add_skill("Some Skill", 50))
print(second_guild.guild_info())
