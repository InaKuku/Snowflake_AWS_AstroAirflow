from project.card.card import Card
from project.card.magic_card import MagicCard


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        for a_card in self.cards:
             if a_card.name == card.name:
                raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == "":
            raise ValueError("Card cannot be an empty string!")
        for a_card in self.cards:
            if a_card.name == card:
                self.cards.remove(a_card)
                self.count -= 1

    def find(self, name: str):
        for a_card in self.cards:
            if a_card.name == name:
                return a_card

# card_repo = CardRepository()
# card1 = MagicCard("Test")
# card_repo.add(card1)
# print(card_repo.cards)