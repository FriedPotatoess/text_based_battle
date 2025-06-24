class Weapons:
    def __init__(self, name: str, weapon_type:str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_Type = weapon_type
        self.damage = damage
        self.value = value
        
        
        
iron_sword = Weapons(name="Iron Sword", weapon_type="sharp", damage=5, value=10)
short_bow = Weapons(name="Short Bow", weapon_type="range", damage=4, value=8)
fists = Weapons(name="Fists", weapon_type="blunt", damage=2, value=0)
