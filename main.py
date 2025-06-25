from character import Hero, Enemy
from weapons import short_bow, iron_sword

hero = Hero(name="Goku", health= 100,)
hero.equip(iron_sword)
enemy = Enemy(name="Frieza", health=100, weapon=short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    
    hero.drop()
    input()