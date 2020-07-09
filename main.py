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
    table = db.table("101")
    result = Query()
    result = table.search((result.low <= race_roll) & (result.high >= race_roll))
    print(result)
    return my_race, my_desc


print("Gender: %s\n" % genders[roll(1, len(genders), -1)])
race, desc = race_search()


# def base_stats():

#     work_stats = {}
#     stats_lst = ["str", "dex", "int", "con", "cha", "wis"]
#     for i in stats_lst:
#         work_stats[i] = roll("3d6")
#     return work_stats


# my_char.race, my_char.race_desc = char_race(roll("1d20"))
# # my_char.culture, my_char.cmod = cmod()

# # print("Race: %s\n" % my_char.race)
# # print("Race Descriptions: \n\n\t%s\n" % wrapper.fill(text=my_char.race_desc))
# print("Stats:")
# for i in my_char.stats:
#     tmp_stat_name = i.capitalize()
#     tmp_stat_value = my_char.stats[i]
#     print("\t{0} : {1}".format(tmp_stat_name, tmp_stat_value))
