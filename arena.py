from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: None
        team_two: None
    '''
    # TODO: create instance variables named team_one and team_two that
    # will hold our teams.
  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?  ")
    max_damage = input(
      "What is the max damage of the ability?  ")

    return Ability(name, max_damage)

   def create_weapon(self):
    '''Prompt user for Weapon information
        return Weapon with values from user input.
    '''
    # TODO: This method will allow a user to create a weapon.
    # Prompt the user for the necessary information to create a new weapon object.
    # return the new weapon object.
        name = input("What is the weapon name?")
        max_damage = input("What is the max damage of the weapon?")
        return weapon(name, max_damage)
    pass
    def create_armor(self):
    '''Prompt user for Armor information
      return Armor with values from user input.
    '''
    # TODO:This method will allow a user to create a piece of armor.
    #  Prompt the user for the necessary information to create a new armor object.
    #  return the new armor object with values set by user.
    name = input("What is the armor name? ")
    max_block = input("What is the max defense of the armor?")
        return armor(name, max_block)
      pass
    def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        item = self.create_ability()
        self.hero.append(abilities)
       elif add_item == "2":
         item = self.create_weapon()
         self.hero.append(weapon)
        elif add_item == "3":
         item = self.create_armor()
          self.hero.append(armor)
    return hero

      # build_team_one is provided to you
  def build_team_one(self):
    '''Prompt the user to build team_one '''
    # This method should allow a user to create team one.
    # Prompt the user for the number of Heroes on team one
    # call self.create_hero() for every hero that the user wants to add to team one.
    # Add the created hero to team one.
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  # Now implement build_team_two
  #HINT: If you get stuck, look at how build_team_one is implemented
  def build_team_two(self):
    '''Prompt the user to build team_two'''
    numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
    for i in range(numOfTeamMembers):
        hero = self.create_hero()
        self.team_one.add_hero(hero)
    pass

 def team_battle(self):
        '''Battle team_one and team_two together.'''

           team_one = list()
           team_two = list()

           for hero in self.team_one:
               team_one.append(hero)

           for hero in self.team_two:
               team_two.append(hero)

           while len(team_one) > 0 and len(team_two)> 0:
               if random.choice(team_one, team_two)
               return team_one.fight(team_two)
               return len.remove(team_one, team_two)
  def show_stats(self):
    '''Prints team statistics to terminal.'''
    # TODO: This method should print out battle statistics
    # including each team's average kill/death ratio.
    # Required Stats:
    #     Show surviving heroes.
    #     Declare winning team
    #     Show both teams average kill/death ratio.
    # Some help on how to achieve these tasks:
    # TODO: for each team, loop through all of their heroes,
    # and use the is_alive() method to check for alive heroes,
    # printing their names and increasing the count if they're alive.
    #
    # TODO: based off of your count of alive heroes,
    # you can see which team has more alive heroes, and therefore,
    # declare which team is the winning team
    #
    # TODO for each team, calculate the total kills and deaths for each hero,
    # find the average kills and deaths by dividing the totals by the number of heroes.
    # finally, divide the average number of kills by the average number of deaths for each team

    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    # This is how to calculate the average K/D for Team One
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

    # TODO: Now display the average K/D for Team Two

    # Here is a way to list the heroes from Team One that survived
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    #TODO: Now list the heroes from Team Two that survived

if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
