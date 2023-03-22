#!/usr/bin/env python3
"""
Learning project to have better standards of writing python
"""

import random
import textwrap
import logging
from tinydb import TinyDB, Query

<<<<<<< HEAD
<<<<<<< HEAD
wrapper = textwrap.TextWrapper(width=60)


class generator:
    # db = TinyDB("./legends.json")
=======
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

=======
logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)

>>>>>>> origin/main
wrapper = textwrap.TextWrapper()
db = TinyDB("data/legends.json")
genders = ["Female", "Male"]
stats_lst = ["str", "dex", "int", "con", "cha", "wis"]
<<<<<<< HEAD
>>>>>>> 9bb8c4a6fb0fe88e4b9ea5efe76ecbd69bfca972

    def __init__(self):
        genders = ["Female", "Male"]
        self.gender = genders[random.randint(0, 1)]
      
        self.db = TinyDB("./legends.json")

    def add_stat(self, stat_name):
        setattr(self, stat_name, random.randint(3, 18))

    def gender(self):
        genders = ["Female", "Male"]
        # self.gender = genders[random.randint(0, 1)]
        self.gender = self.add_stat('test')

<<<<<<< HEAD
    def race(self):
        race_roll = random.randint(1, 20)

        if race_roll == 20:
            table = self.db.table("101a")
            race_roll = random.randint(1, 10)
        else:
            table = self.db.table("101")

        result = Query()
        result = table.search((result.low <= race_roll)
                              & (result.high >= race_roll))[0]

        detented_text = textwrap.dedent(result["desc"].strip())

        self.race = result["race"]
        self.race_desc = textwrap.fill(detented_text, width=70)

    def culture(self):
        cu_roll = random.randint(1, 10)
        table = self.db.table("102")
        result = Query()
        result = table.search((result.low <= cu_roll)
                              & (result.high >= cu_roll))[0]

        detented_text = textwrap.dedent(result["desc"].strip())
        desc = textwrap.fill(detented_text, width=70)

        self.culture = result["culture"]
        self.culture_desc = desc
        self.culture_mod = result["cumod"]
=======
>>>>>>> origin/main

    def social(self):
        soc_roll = random.randint(1, 100) + int(self.culture_mod)
        table = self.db.table("103")
        result = Query()
        result = table.search((result.low <= soc_roll)
                              & (result.high >= soc_roll))[0]

        detented_text = textwrap.dedent(result["desc"].strip())
        desc = textwrap.fill(detented_text, width=70)

        self.social = result["social"],
        self.social_desc = desc
        self.social_mod = result["somod"]

    def trait(self):
        trait_roll = random.randint(1, 100)

        if trait_roll <= 50:
            self.trait = "No special personality trait"

        if 51 <= trait_roll <= 65:
            table = self.db.table("318B")
        elif 66 <= trait_roll <= 80:
            table = self.db.table("647")
        else:
            table = self.db.table("648")

        spec_trait = random.randint(2, 20)

        result = Query()
        result = table.search((result.roll == spec_trait))[0]
        self.trait = result["result"]


char = generator()

stats_lst = ["Str", "Dex", "Int", "Con", "Cha", "Wis"]

for stat in stats_lst:
    char.add_stat(stat)

char.race()
char.culture()
char.social()
char.trait()

print(char.__dict__)
=======
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
<<<<<<< HEAD

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


=======

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


>>>>>>> origin/main
if __name__ == "__main__":
    logging.info("Starting NPC maker")
    NPC = NpcCard()
    NPC.print()
<<<<<<< HEAD
>>>>>>> 9bb8c4a6fb0fe88e4b9ea5efe76ecbd69bfca972
=======
>>>>>>> origin/main
