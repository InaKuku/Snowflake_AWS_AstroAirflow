from unittest import TestCase, main
from project.hero import Hero

class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("HerTheBest", 10, 99.99, 0.01)
        self.enemy_hero = Hero("AnotherOne", 10, 99.99, 0.01)


    def test_init(self):
        self.assertEqual("HerTheBest", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(99.99, self.hero.health)
        self.assertEqual(0.01, self.hero.damage)

    def test_battle_against_himself(self):
        enemy_hero = Hero("HerTheBest", 10, 99.99, 0.01)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_negative_health(self):
        hero1 = Hero("Test", 10, -3, 7)
        with self.assertRaises(ValueError) as ex:
            hero1.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_with_enemy_hero_negative_health(self):
        enemy_hero = Hero("AnotherOne", 10, -3, 0.01)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight AnotherOne. He needs to rest", str(ex.exception))

    def test_battle_enemy_positive_health(self):
        self.hero.battle(self.enemy_hero)
        self.assertEqual(104.89, self.enemy_hero.health)
        self.assertEqual(99.89, self.hero.health)
        self.assertEqual(11, self.enemy_hero.level)
        self.assertEqual(5.01, self.enemy_hero.damage)
        self.assertEqual("You lose", self.hero.battle(self.enemy_hero))


    def test_battle_enemy_negative_health(self):
        enemy_hero1 = Hero("Enemy_Some", 1, 0.01, 5.5)
        self.assertEqual("You win", self.hero.battle(enemy_hero1))
        self.assertEqual(-0.09000000000000001, enemy_hero1.health)
        self.assertEqual(99.49, self.hero.health)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(5.01, self.hero.damage)

    def test_battle_hero_with_negative_health_enemy_negative_health(self):
        enemy_hero1 = Hero("Enemy_Some", 1, 0.01, 5.5)
        hero1 = Hero("Hero_Some", 1, 3, 9)
        self.assertEqual("Draw", hero1.battle(enemy_hero1))

    def test_hero_str(self):
        self.assertEqual("Hero HerTheBest: 10 lvl\nHealth: 99.99\nDamage: 0.01\n", str(self.hero))

if __name__ == "__main__":
    main()
