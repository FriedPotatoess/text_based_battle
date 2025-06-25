from character import Hero, Enemy
from weapons import short_bow, iron_sword

hero = Hero(name="Goku", health= 100,)
hero.equip(iron_sword)
enemy = Enemy(name="Frieza", health=100, weapon=short_bow)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    
    hero.health_bar.draw()
    enemy.health_bar.draw()
    
    
    input()