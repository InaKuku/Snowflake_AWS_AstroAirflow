from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(TestCase):

    def setUp(self):
        self.card_repo = CardRepository()
        self.count = 0
        self.cards = []

    def test_init(self):
        self.assertEqual(0, self.count)
        self.assertEqual([], self.cards)

    def test_add_cart(self):
        card1 = MagicCard("Test")
        self.card_repo.add(card1)
        self.assertEqual(1, len(self.card_repo.cards))
        self.assertEqual(1, self.card_repo.count)

    def test_add_existing_cart_raises(self):
        card1 = MagicCard("Test")
        card1 = MagicCard("Test")
        self.card_repo.add(card1)
        with self.assertRaises(ValueError) as ex:
            self.card_repo.add(card1)
        self.assertEqual("Card Test already exists!", str(ex.exception))

    def test_remove(self):
        card1 = MagicCard("Test")
        self.card_repo.add(card1)
        self.assertEqual(1, self.card_repo.count)
        self.card_repo.remove("Test")
        self.assertEqual([], self.card_repo.cards)
        self.assertEqual(0, self.card_repo.count)

    def test_remove_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.card_repo.remove("")
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_find(self):
        card1 = MagicCard("Test")
        self.card_repo.add(card1)
        self.assertEqual(card1, self.card_repo.find("Test"))

if __name__ == '__main__':
    main()