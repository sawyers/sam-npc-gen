import random
import json
import textwrap


class char:
    def __init__(self):
        self.data = []


def roll(roll, modify=0):
    (to_roll, size) = [int(s) for s in roll.split("d")]

    i = 1
    total = 0
    while i <= to_roll:
        total += random.randint(1, size)
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


# -----------------------
# with open('legends.dat', "r") as f:
#  data = json.load(f)
# f.close()

wrapper = textwrap.TextWrapper(width=60)

my_char = char()
my_char.stats = base_stats()
# my_char.race, my_char.race_desc = char_race()
# my_char.culture, my_char.cmod = cmod()

# print("Race: %s\n" % my_char.race)
# print("Race Descriptions: \n\n\t%s\n" % wrapper.fill(text=my_char.race_desc))
print("Stats:")
for i in my_char.stats:
    tmp_stat_name = i.capitalize()
    tmp_stat_value = my_char.stats[i]
    print("\t{0} : {1}".format(tmp_stat_name, tmp_stat_value))
