#!/usr/bin/env python3
"""
Learning project to have better standards of writing python
"""

import random
import textwrap
from tinydb import TinyDB, Query

wrapper = textwrap.TextWrapper(width=60)
db = TinyDB("data/legends.json")


genders = ["Female", "Male"]
stats_lst = ["str", "dex", "int", "con", "cha", "wis"]


def roll(to_roll, high, modifier=0):
    """ because adding #nosec everwhere would be a drag"""
    i = 1
    total = 0
    while i <= to_roll:
        total += random.randint(1, high)  # nosec
        i += 1
    total += modifier
    return total


def race_search():
    """lookup against table 101 with optional table 101b"""
    race_roll = roll(1, 20)
    my_race = ""
    my_desc = ""

    if race_roll == 20:
        table = db.table("101a")
        race_roll = roll(1, 10)
    else:
        table = db.table("101")

    result = Query()
    result = table.search((result.low <= race_roll) & (result.high >= race_roll))[0]

    return result["race"], result["desc"]

class NpcCard(object):
    gender = ''
    race = ''
    race_desc = ''
    attributes = {}
    
    def __init__(self):
        self.gender = genders[roll(1, len(genders), -1)]
        for i in stats_lst:
            self.attributes[i] = roll(3, 6)
        self.race, self.race_desc = race_search()
    
    def print(self):
        card = '''\
        Race: {}
        Racial description: {}
        Gender: {}

            Str: {}
            Dex: {}
            Con: {}
            Int: {}
            Wis: {}
            Cha: {}

        Background:

        '''.format(self.race, self.race_desc, self.gender, self.attributes['str'], self.attributes['dex'], 
            self.attributes['con'], self.attributes['int'], self.attributes['wis'], self.attributes['cha'])

        print(textwrap.dedent(card))


if __name__ == "__main__":
    print("Starting NPC maker")
    NPC = NpcCard()
    NPC.print()

