#!/usr/bin/env python3
"""
Learning project to have better standards of writing python
"""

import random
import textwrap
import logging
from tinydb import TinyDB, Query

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

wrapper = textwrap.TextWrapper()
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

    detented_text = textwrap.dedent(result["desc"].strip())
    desc = textwrap.fill(detented_text, width=70)
    return result["race"], desc


def base_culture():
    """Determine base culture"""
    cu_roll = roll(1, 10)
    table = db.table("102")
    result = Query()
    result = table.search((result.low <= cu_roll) & (result.high >= cu_roll))[0]

    detented_text = textwrap.dedent(result["desc"].strip())
    desc = textwrap.fill(detented_text, width=70)

    return result["culture"], desc, result["cumod"]


def base_social(cumod):
    """Determine social standing, impacted by culture level"""
    try:
        soc_roll = roll(1, 100) + int(cumod)
        table = db.table("103")
        result = Query()
        result = table.search((result.low <= soc_roll) & (result.high >= soc_roll))[0]
    except ValueError:
        logging.error("Somehow the cumod is not an integer")
        raise
    detented_text = textwrap.dedent(result["desc"].strip())
    desc = textwrap.fill(detented_text, width=70)

    return result["social"], desc, result["somod"]


def personal_trait():
    """Basic personality"""
    trait_roll = roll(1, 100)
    if trait_roll <= 50:
        return "No special personality trait"
    elif 51 <= trait_roll <= 65:
        table = db.table("318B")
    elif 66 <= trait_roll <= 80:
        table = db.table("647")
    else:
        table = db.table("648")

    spec_trait = roll(2, 20)

    result = Query()
    result = table.search((result.roll == spec_trait))[0]
    return result["result"]


class NpcCard(object):
    gender = ""
    race = ""
    race_desc = ""
    attributes = {}

    def __init__(self):
        self.gender = genders[roll(1, len(genders), -1)]
        for i in stats_lst:
            self.attributes[i] = roll(3, 6)
        self.race, self.race_desc = race_search()
        self.trait = personal_trait()
        self.culture, self.cu_desc, self.cumod = base_culture()
        self.socmod, self.socdesc, self.somod = base_social(self.cumod)

    def print(self):
        card = """\
Race: {}

Racial description:

{}

Gender: {}

    Str: {}
    Dex: {}
    Con: {}
    Int: {}
    Wis: {}
    Cha: {}

Background:

Personality: {}

Base Culture: {}
Base Culture description:

{}

Social Standing: {}
Social Description:

{}
        """.format(
            self.race,
            self.race_desc,
            self.gender,
            self.attributes["str"],
            self.attributes["dex"],
            self.attributes["con"],
            self.attributes["int"],
            self.attributes["wis"],
            self.attributes["cha"],
            self.trait,
            self.culture,
            self.cu_desc,
            self.socmod,
            self.socdesc,
        )

        print(textwrap.dedent(card))


if __name__ == "__main__":
    logging.info("Starting NPC maker")
    NPC = NpcCard()
    NPC.print()
