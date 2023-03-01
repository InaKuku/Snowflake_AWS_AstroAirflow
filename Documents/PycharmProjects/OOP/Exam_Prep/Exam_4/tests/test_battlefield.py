from unittest import TestCase, main

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.controller import Controller
from project.player.beginner import Beginner
from project.player.player import Player


class TestBattlefield(TestCase):

    def setUp(self):
        self.battlef = BattleField()
        self.player1 = Beginner("Begi1")
        self.player2 = Beginner("Begi2")
        self.card1 = MagicCard("Magi1")
        self.card2 = MagicCard("Magi2")
        self.trap_card1 = TrapCard("Trapi1")
        self.trap_card2 = TrapCard("Trapi2")
        self.trap_card3 = TrapCard("Trapi3")
        self.trap_card4 = TrapCard("Trapi4")
        self.player1.card_repository.cards = [self.card1, self.trap_card1, self.trap_card2]
        self.player2.card_repository.cards = [self.card2, self.trap_card3, self.trap_card4]

    def test_after_first_fight(self):
        self.battlef.fight(self.player1, self.player2)
        self.player1.health = 145
        self.player2.health = 145

    def test_fight_negative_health_raises(self):
        player3 = Beginner("Test")
        player3.health = 1
        self.card1.damage_points = 300
        with self.assertRaises(ValueError) as ex:
            self.battlef.fight(self.player1, player3)
        self.assertEqual("Player's health bonus cannot be less than zero ", str(ex.exception))

    def test_zero_health_raises(self):
        self.player1.health = 0
        with self.assertRaises(ValueError) as ex:
            self.battlef.fight(self.player1, self.player2)
        self.assertEqual("Player is dead!", str(ex.exception))

if __name__ == '__main__':
    main()