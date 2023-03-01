from unittest import TestCase, main

from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(TestCase):

    def setUp(self):
        self.pl_repo = PlayerRepository()
        self.count = 0
        self.players = []

    def test_init(self):
        self.assertEqual(0, self.pl_repo.count)
        self.assertEqual([], self.pl_repo.players)

    def test_add_player(self):
        player1 = Beginner("Test")
        self.pl_repo.add(player1)
        self.assertEqual(1, len(self.pl_repo.players))
        self.assertEqual(1, self.pl_repo.count)

    def test_add_existing_player(self):
        player1 = Beginner("Test")
        self.pl_repo.add(player1)
        with self.assertRaises(ValueError) as ex:
            self.pl_repo.add(player1)
        self.assertEqual("Player Test already exists!", str(ex.exception))

    def test_remove_player(self):
        player1 = Beginner("Test")
        self.pl_repo.add(player1)
        self.assertEqual(1, self.pl_repo.count)
        self.pl_repo.remove("Test")
        self.assertEqual(0, self.pl_repo.count)
        self.assertEqual([], self.pl_repo.players)

    def test_remove_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
           self.pl_repo.remove("")
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_find(self):
        player1 = Beginner("Test")
        self.pl_repo.add(player1)
        self.assertEqual(player1, self.pl_repo.find("Test"))

if __name__ == '__main__':
    main()