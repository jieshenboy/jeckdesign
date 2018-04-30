#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as etree
import json
from constants import JDATA, XDATA


class JSONConnector:
    """Connector json"""

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self) -> JDATA:
        return self.data


class XMLConnector:
    """Connect XML"""

    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self) -> XDATA:
        return self.tree


def connector_facory(filepath) -> [XMLConnector or JSONConnector]:
    """Connect XML or Json"""
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath) -> [XDATA or JDATA]:
    """deal with abnormal"""
    factory = None
    try:
        factory = connector_facory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main() -> None:
    """ run  main"""
    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    # find liar's firstName、price、iphone number
    liars = xml_data.findall(
        ".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('price: ${}'.format(liar.find('lastName').text))
        [print('iphone number ({}):'.format(p.attrib['type']), p.text)
         for p in liar.find('phoneNumbers')]
    print("\n")

    # fund the donut's name, price, tooping
    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type']))
         for t in donut['topping']]


if __name__ == "__main__":
    """run go"""
    main()
