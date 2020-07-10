#!/usr/bin/env python3
"""
Learning project to have better standards of writing python
"""

import random
import textwrap
from tinydb import TinyDB, Query

wrapper = textwrap.TextWrapper(width=60)
db = TinyDB("./legends.json")


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


race, desc = race_search()

print("Race: {0}\n".format(race))
print("Race Descriptions: \n\n{0}\n".format(wrapper.fill(text=desc)))
print("Gender: {0}\n".format(genders[roll(1, len(genders), -1)]))
print("Stats:")
for i in stats_lst:
    print("\t{0}:\t{1}".format(i.capitalize(), roll(3, 6)))


#     print("\t{0} : {1}".format(tmp_stat_name, tmp_stat_value))
