from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestController(TestCase):

    def setUp(self) -> None:
        self.controller = Controller()
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()
        player1 = Beginner("Test")

    def test_add_player_beginner(self):
        self.controller.add_player("Beginner", "Test")
        self.assertEqual(1, len(self.controller.player_repository.players))
        for player in self.controller.player_repository.players:
            self.assertEqual("Test", player.username)
            self.assertEqual(Beginner, type(player))

    def test_add_player_advanced(self):
        self.assertEqual("Successfully added player of type Advanced with username: Test", self.controller.add_player("Advanced", "Test"))

    def test_add_card_magic(self):
        self.assertEqual("Successfully added card of type MagicCard with name: Test", self.controller.add_card("Magic", "Test"))

    def test_add_card_trap(self):
        self.assertEqual("Successfully added card of type TrapCard with name: Test", self.controller.add_card("Trap", "Test"))

    def test_add_card_to_player_repository(self):
        self.controller.add_player("Advanced", "Test")
        self.controller.add_card("Magic", "Test_Card")
        self.controller.add_player_card("Test", "Test_Card")
        for player in self.controller.player_repository.players:
            self.assertEqual(1, len(player.card_repository.cards))

    def test_fight(self):
        self.controller.add_player("Beginner", "Test1")
        self.controller.add_player("Beginner", "Test2")
        self.assertEqual("Attack user health 90 - Enemy user health 90", self.controller.fight("Test1", "Test2"))

    def test_report(self):
        self.controller.add_player("Beginner", "Test1")
        self.controller.add_player("Beginner", "Test2")
        self.controller.add_card("Magic", "Test_Card_Magic")
        self.controller.add_card("Trap", "Test_Card_Trap")
        self.controller.add_player_card("Test1", "Test_Card_Magic")
        self.controller.add_player_card("Test2", "Test_Card_Trap")
        self.assertEqual("Username: Test1 - Health: 50 - Cards 1\n### Card: Test_Card_Magic - Damage: 5\nUsername: Test2 - Health: 50 - Cards 1\n### Card: Test_Card_Trap - Damage: 120", self.controller.report())

if __name__ == '__main__':
    main()