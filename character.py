from weapons import fists

class Character:
    race = "Human"
    
    
    def __init__(self, name: str, health: int,):
        self.name = name
        self.health = health
        self.health_max = health
        
        self.weapon = fists
    
    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f"{self.name} dealth {self.weapon.damage} damage to {target.name}")
        
class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
        
class Enemy(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)
        