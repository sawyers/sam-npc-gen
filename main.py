import random
import textwrap
from tinydb import TinyDB, Query

wrapper = textwrap.TextWrapper(width=60)
db = TinyDB("./legends.json")


class char:
    def __init__(self):
        self.data = []


def roll(roll, modify=0):
    (to_roll, size) = [int(s) for s in roll.split("d")]

    i = 1
    total = 0
    while i <= to_roll:
        total += random.randint(1, size)  # nosec
        i += 1
    total += modify
    if total < 0:
        total = 0
    return total


def base_stats():
    work_stats = {}
    stats_lst = ["str", "dex", "int", "con", "cha", "wis"]
    for i in stats_lst:
        work_stats[i] = roll("3d6")
    return work_stats


def char_race(roll, modify=0):
    table = db.table("101")
    result = Query()
    result = table.search((result.log <= roll) & (race.high >= roll))[0]


my_char = char()
my_char.stats = base_stats()
my_char.race, my_char.race_desc = char_race(roll("1d20"))
# my_char.culture, my_char.cmod = cmod()

# print("Race: %s\n" % my_char.race)
# print("Race Descriptions: \n\n\t%s\n" % wrapper.fill(text=my_char.race_desc))
print("Stats:")
for i in my_char.stats:
    tmp_stat_name = i.capitalize()
    tmp_stat_value = my_char.stats[i]
    print("\t{0} : {1}".format(tmp_stat_name, tmp_stat_value))
