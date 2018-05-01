#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
coping model

for example: coping book
"""
import copy
from collections import OrderedDict


class Book:

    def __init__(self, name, authors, price, **rest):
        self.name = name
        self.authors = authors
        self.price = price
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict
