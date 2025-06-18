from wearable import Wearable

class Oar(Wearable):
    
    def __init__(self, size: float, material: str, wear: float = 0):
        super().__init__(wear)
        self.size = size
        self.material = material
        self.is_rowing = False
        
    def __str__(self):
        return f"Весло. Материал: {self.material}, Размер: {self.size}, Износ: {self.wear}/10"
    
    def get_eff(self):
        if self.wear >= 10:
            return 0
        elif self.wear <=0:
            return 1
        else:
            return 1 - self.wear / 10
        
    def start_rowing(self):
        self.is_rowing = True
        
    def stop_rowing(self):
        self.is_rowing = False