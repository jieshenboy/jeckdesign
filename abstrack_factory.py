#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This doc is for to learnning th abstrack_factory, by this way ,you can using a model to deal with the differents work
if these work have a same stream.
for example: a game designed for two users, ones are adult, and other is not.
"""


class Frog:
    """This is frog"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(
            '{} the Frog encounters {} and {}!'.format(
                self,
                obstacle,
                obstacle.action()))


class Bug:
    """eat bug"""

    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWord:
    """Forg Word"""

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t---------Frog World ---------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    """Wizar"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(
            '{} the Wizard battles against {} and  {} !'.format(
                self,
                obstacle,
                obstacle.action()))


class Ork:
    """ork"""

    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizarWorld:
    """wizar world"""

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t---------Wizard World ---------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    """running model"""

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input('Welcome {}. How old are you ? '.format(name))
        age = int(age)
    except ValueError as err:
        print("Age {} is invalid, please try again ...".format(age))
        return (False, age)
    return (True, age)


def main():
    name = input("Hello, What's your name ?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWord if age < 18 else WizarWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == "__main__":
    main()
