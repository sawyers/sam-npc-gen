import random
import json 
import textwrap

class char:
  def __init__(self):
    self.data = []

def roll(rolls,size):
  i = 1
  total = 0
  while i <= rolls: 
    total += random.randint(1,size)
    i += 1
  return total

def base_stats():
  work_stats = {}
  tmp_stats = ['str','dex','int','con','cha','wis']
  for i in tmp_stats:
    work_stats[i] = roll(3,6)
  return work_stats

def char_race():
  test = roll(1,20)

  if 1 <= test <= 14:
    race = 'human'
  elif 15 <= test <= 16:
    race = 'elf'
  elif 17 == test:
    race = 'dwarf'
  elif 18 == test:
    race = 'halfling'
  elif 19 == test:
    race = 'half elf'
  else:
    sub_race = roll(1,10)
    if 1 <= sub_race <= 3:
      race = 'beastman'
    elif 4<= sub_race <= 5:
      race = 'reptileman'
    elif 6 == sub_race:
      race = 'orc'
    else:
      race = 'half-orc'

  for i in data['tbl_101']:
    if (i['race'] == race ):
      desc = i['desc']
  
  return race, desc

def cmod():
  test = roll(1,10)

  if 1 == test:
    level = 'primitive'
    cmod = -3
    native = 'wilderness'
  elif 2 <= test <= 3:
    level = 'nomad'
    cmod = 0
    native = 'wilderness'
  elif 4 <= test <= 6:
    level = 'barbarian'
    cmod = 2
    native = 'wilderness'
  elif 7 <= test <= 9:
    level = 'civilized'
    cmod = 5
    native = 'wilderness'
  else:
    level = 'civilized-decadent'
    cmod = 7
    native = 'wilderness'
  
#-----------------------
with open('legends.dat', "r") as f:
  data = json.load(f)
f.close() 

wrapper = textwrap.TextWrapper(width=60)

my_char = char()
my_char.stats = base_stats()
my_char.race, my_char.race_desc = char_race()
my_char.culture, my_char.cmod = cmod()

print("Race: %s\n" % my_char.race)
print("Race Descriptions: \n\n\t%s\n" % wrapper.fill(text=my_char.race_desc))
print("Stats:")
for i in my_char.stats:
  tmp_stat_name = i.capitalize()
  tmp_stat_value = my_char.stats[i]
  print("\t{0} : {1}".format(tmp_stat_name, tmp_stat_value))
  
