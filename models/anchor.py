from models.wearable import Wearable

class Anchor(Wearable):
    
    def __init__(self, weight: float, size: float, wear: float = 0):
        super().__init__(wear)
        self.weight = weight
        self.size = size
        self.is_dropped = False
        
    def __str__(self):
        return f"Якорь. Вес: {self.weight}кг, Размер: {self.size}м, Износ: {self.wear}/10"
    
    def drop_anchor(self):
        self.is_dropped = True
        
    def raise_anchor(self):
        self.is_dropped = False
        self.wear += 1