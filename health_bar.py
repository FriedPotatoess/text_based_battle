import os

os.sytem("")

class HealthBar:
    def __init__(self, entity, length: int = 20, is_colored: bool = True,color: str = "") -> None:
        self.entity = entity
        self.lenght = lenght
        self.max_value = entity.health_max
        self.current_value = entity.health
        
        
        self.is_colored = is_colored
        self.color = color