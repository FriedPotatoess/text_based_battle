from character import character

hero = character(name="goku", health=100, damage=5)
enemy = character(name="Frieza", health=100, damage=3)

while True:
    hero.attack(enemy)
    enemy.attack(hero)
    
    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")