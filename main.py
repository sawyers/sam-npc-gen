#!/usr/bin/env python3
"""
Learning project to have better standards of writing python
"""
import random
import textwrap
from tinydb import TinyDB, Query

wrapper = textwrap.TextWrapper(width=60)


class generator:
    # db = TinyDB("./data/legends.json")

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
