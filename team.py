class Team:
def __init__(self, name):
    ''' Initialize your team with its team name and an empty list of heroes
    '''
    self.name = name
    self.heroes = list()

def remove_hero(self, name):
  '''Remove hero from heroes list.
  If Hero isn't found return 0.
  '''
  foundHero = False
  # loop through each hero in our list
  for hero in self.heroes:
    # if we find them, remove them from the list
    if hero.name == name:
      self.heroes.remove(hero)
      # set our indicator to True
      foundHero = True
  # if we looped through our list and did not find our hero,
  # the indicator would have never changed, so return 0
if not foundHero:
    return 0

def view_all_heroes(self):
   for x in range(len(self.heroes)):
        print self.heroes[x],
    pass

def add_hero(self, hero)
    self.heroes.append('')
  pass

def attack(self, other_team):
    ''' Battle each team against each other.'''

    living_heroes = list()
    living_opponents = list()

    for hero in self.heroes:
      living_heroes.append(hero)

    for hero in other_team.heroes:
      living_opponents.append(hero)

    while len(living_heroes) > 0 and len(living_opponents)> 0:
      # TODO: Complete the following steps:
      # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
      # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
      # 3) update the list of living_heroes and living_opponents
      # to reflect the result of the fight
