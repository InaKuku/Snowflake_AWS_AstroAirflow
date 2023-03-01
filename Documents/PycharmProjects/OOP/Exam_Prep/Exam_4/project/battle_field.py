# from collections import deque

from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:

    @staticmethod
    def fight(attacker: Player, enemy: Player):
        att_total_health_point = 0
        enemy_total_health_point = 0
        if attacker.is_dead:
            raise ValueError("Player is dead!")
        if enemy.is_dead:
            raise ValueError("Player is dead!")
        if type(attacker) == Beginner:
            attacker.health += 40
            for a_card in attacker.card_repository.cards:
                a_card.damage_points += 30
        if type(enemy) == Beginner:
            enemy.health += 40
            for a_card in enemy.card_repository.cards:
                a_card.damage_points += 30
        for a_card in attacker.card_repository.cards:
            att_total_health_point += a_card.health_points
        for a_card in enemy.card_repository.cards:
            enemy_total_health_point += a_card.health_points
        attacker.health += att_total_health_point
        enemy.health += enemy_total_health_point
        for card in attacker.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            enemy.take_damage(card.damage_points)
            break

        for card in enemy.card_repository.cards:
            if attacker.is_dead or enemy.is_dead:
                return
            attacker.take_damage(card.damage_points)
            break

        # if len(attacker.card_repository.cards) > 0 and len(enemy.card_repository.cards) > 0:
        #     att_queue = deque(attacker.card_repository.cards)
        #     enemy_queue = deque(enemy.card_repository.cards)
        #     is_Dead = False
        #     while not attacker.is_dead or not enemy.is_dead:
        #         for a_card in att_queue:
        #             enemy.health -= a_card.damage_points
        #             att_queue.rotate(-1)
        #             if enemy.is_dead:
        #                 is_Dead = True
        #                 break
        #             else:
        #                 for a_card in enemy_queue:
        #                     attacker.health -= a_card.damage_points
        #                     enemy_queue.rotate(-1)
        #                     if attacker.is_dead:
        #                         is_Dead = True
        #                         break
        #                     break
        #             break
        #         if is_Dead:
        #             break


# player1 = Beginner("Begi1")
# player2 = Beginner("Begi2")
# player2.health = 1
# card1 = MagicCard("Magi1")
# card1.damage_points = 300
# card2 = MagicCard("Magi2")
# trap_card1 = TrapCard("Trapi1")
# trap_card2 = TrapCard("Trapi2")
# trap_card3 = TrapCard("Trapi3")
# trap_card4 = TrapCard("Trapi4")
# player1.card_repository.cards = [card1, trap_card1, trap_card2]
# player2.card_repository.cards = [card2, trap_card3, trap_card4]
# BattleField.fight(player1, player2)
# print(player1.health)
# print(player2.health)
