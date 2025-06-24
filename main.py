from character import Hero, Enemy

hero = Hero(name="Goku", health= 100,)
enemy = Enemy(name="Frieza", health=100,)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")
    
    input()