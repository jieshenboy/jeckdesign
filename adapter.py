#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
适配器：两个不兼容的模式兼容。
adapt two interface to using one model
"""


class Synthesizer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthersizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '{} the human'.format(self.name)

    def speak(self):
        return 'says hello'


class Computer:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Adapter:

    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print('{}  {}'.format(str(i), i.execute()))


if __name__ == "__main__":
    main()
