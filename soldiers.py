import random
 
class Unit:
    def __init__(self, id, team):
        self.id = id
        self.team = team


class Hero(Unit):
    lvl = 0
 
    def lvl_up(self, lvl):
        self.lvl += lvl
 
 
class Soldier(Unit):
    def follow(self, hero):
        print(f"Soldier with id: {self.id} follow to the {hero} hero")
 
 
hero_1 = Hero("First", 1)
hero_2 = Hero("Second", 2)
team_1 = []
team_2 = []
for i in range(int(input("How much soldiers you want?: "))):
    x = round(random.randint(0,1))
    if x < 0.5:
        i = Soldier(x, 1)
        team_1.append(i)
    else:
        i = Soldier(x, 2)
        team_2.append(i)
print("Number of soldiers of the first hero:", len(team_1))
print("Number of soldiers of the second hero:", len(team_2))

if (len(team_1)) > (len(team_2)):
    hero_1.lvl_up(1)
    i = random.choice(team_1)
    print("First hero level:", hero_1.lvl)
    i.follow(hero_1.id)
else:
    hero_2.lvl_up(1)
    i = random.choice(team_2)
    print("Second hero level:", hero_2.lvl)
    i.follow(hero_2.id)