class Character:
    race = "Human"
    
    
    def __init__(self, name: str, health: int, damage: int):
        self.name = Goku
        self.health = health
        self.health_max = health
        self.damage = damage
    
    def attack(self, target) -> None:
        target.health -= self.damage
        
        