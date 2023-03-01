from project.battle_field import BattleField
from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player import player_repository
from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player import Player
from project.player.player_repository import PlayerRepository


class Controller:
    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

    def add_player(self, type: str, username: str):
        if type == "Beginner":
            self.player_repository.add(Beginner(username))
            return f"Successfully added player of type Beginner with username: {username}"
        elif type == "Advanced":
            self.player_repository.add(Advanced(username))
            return f"Successfully added player of type Advanced with username: {username}"

    def add_card(self, type: str, name: str):
        if type == "Magic":
            self.card_repository.add(MagicCard(name))
            return f"Successfully added card of type MagicCard with name: {name}"
        elif type == "Trap":
            self.card_repository.add(TrapCard(name))
            return f"Successfully added card of type TrapCard with name: {name}"


    def add_player_card(self, username: str, card_name: str):
        for a_player in self.player_repository.players:
            if a_player.username == username:
                for a_card in self.card_repository.cards:
                    if a_card.name == card_name:
                        a_player.card_repository.add(a_card)

    def fight(self, attack_name: str, enemy_name: str):
        for a_player in self.player_repository.players:
            if a_player.username == attack_name:
                for sec_player in self.player_repository.players:
                    if sec_player.username == enemy_name:
                        BattleField.fight(a_player, sec_player)
                        return f"Attack user health {a_player.health} - Enemy user health {sec_player.health}"



    def report(self):
        result = ""
        for a_player in self.player_repository.players:
            result += f"Username: {a_player.username} - Health: {a_player.health} - Cards {a_player.card_repository.count}\n"
            for a_card in a_player.card_repository.cards:
                result += f"### Card: {a_card.name} - Damage: {a_card.damage_points}\n"
        return result

# controller = Controller()
# controller.add_player("Beginner", "Test1")
# controller.add_player("Beginner", "Test2")
# print(controller.fight("Test1", "Test2"))
# controller.player_repository = PlayerRepository()
# controller.card_repository = CardRepository()
# player1 = Beginner("Test")
# print(controller.add_player("Beginner", "Test"))
# print(controller.player_repository.players)
# controller.add_player("Beginner", "Test1")
# controller.add_player("Beginner", "Test2")
# controller.add_card("Magic", "Test_Card_Magic")
# controller.add_card("Trap", "Test_Card_Trap")
# controller.add_player_card("Test1", "Test_Card_Magic")
# controller.add_player_card("Test2", "Test_Card_Trap")
# print(controller.report())