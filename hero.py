#lab 6| xiaopeng
import random
from ability import Ability
from armor import Armor
from team import Team

class Hero:
    def __init__(self,name,starting_health=100):
        self.name=name
        self.starting_health=starting_health
        self.current_health= starting_health
        self.abilities=[]
        self.armors=[]
        self.kills=0
        self.deaths=0

    '''
    def battle(self,opponent):
        print(random.choice([self.name, opponent.name]))
    '''
            
    
    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        print(total_damage)
        return total_damage
    
    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block=0
        for armor in self.armors:
            total_block+=armor.block()
        print(total_block)
        return total_block

    def take_damage(self, damage):
        blocked = self.defend()
        actual_damage = max(damage - blocked,0)
        self.current_health -= actual_damage
        if self.current_health<0:
            self.current_health=0
        return actual_damage
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1
    
    def battle(self, opponent):
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
        else:
            while self.current_health > 0 and opponent.current_health > 0:
                opponent.take_damage(self.attack())
                

                if opponent.current_health <= 0:
                  print(self.name + " won!")
                  self.add_kill()
                  opponent.add_death()
                  break
            
                self.take_damage(opponent.attack())

                if self.current_health <= 0:
                  print(opponent.name + " won!")
                  opponent.add_kill()
                  self.add_death()
                  break

if __name__=="__main__":
    my_hero = Hero("spider-man",150)
    print(my_hero.name)
    print(my_hero.current_health)
    my_opponent = Hero("captain America", 200)
    my_opponent.add_ability(Ability("I can do this all day",100))
    my_hero.add_ability(Ability("fire web",100))
    print(my_hero.abilities)
    my_hero.battle(my_opponent)
    team = Team("Avengers")
    hero1 = Hero("Spider-Man","iron-man")
    hero2 = Hero("Captain America","black panther")
    team.add_hero(hero1)
    team.add_hero(hero2)
    team.view_all_heroes()

    
        


