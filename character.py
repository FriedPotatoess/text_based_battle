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
        
        
        