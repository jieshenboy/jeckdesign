#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
command pattern

make things in black box, using a command can deal with the troubles.
"""

import os

verbose = True


class RenameFile:
    """rename"""

    def __init__(self, path_src, path_dest):
        self.src = path_src
        self.dest = path_dest

    def execute(self):
        if verbose:
            print('[renaming "{}" to "{}"]'.format(self.src, self.dest))

        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile:
    """create file"""

    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='\n')


def delete_file(path):
    if verbose:
        print("deleting file '{}'".format(path))
    os.remove(path)


def main():
    orig_name = 'file1'
    new_name = 'file2'
    commands = []

    for cmd in CreateFile(orig_name), ReadFile(
            orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)

    [c.execute() for c in commands]

    answer = input('reverser the executed commands? [y/n]')

    if answer not in 'yY':
        print("The result is {}".format(new_name))
        exit()
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            pass


if __name__ == "__main__":
    main()
