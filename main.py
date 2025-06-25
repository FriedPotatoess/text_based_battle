from character import Hero, Enemy
from weapons import short_bow

hero = Hero(name="Goku", health= 100,)
enemy = Enemy(name="Frieza", health=100, weapon=short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    
    
    input()