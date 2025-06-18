from oar import Oar
from anchor import Anchor
from wearable import Wearable

class Boat(Wearable):
    
    def __init__(
            self,
            material: str,
            size: float,
            seats: int,
            wear: float = 0,
            anchor: Anchor | None = None,
            oars: set[Oar] | None = None
    ):
        super().__init__(wear)
        self.material = material
        self.size = size
        self.seats = seats
        self.anchor = anchor
        self.oars = oars
        
    def __str__(self):
        return (f"Лодка. Материал: {self.material}, Размер: {self.size}, Сидения: {self.seats}\n"
                f"Якорь: {'Нет' if self.anchor is None else self.anchor}\n"
                f"Весла: {'Нет' if self.oars is None else self.oars}\n"
                f"Износ: {self.wear}/10")
    
    def add_anchor(self, anchor: Anchor):
        self.anchor = anchor
        
    def add_oar(self, oar: Oar):
        self.oars.add(oar)
        
    def drop_anchor(self):
        if self.anchor:
            self.anchor.drop_anchor()
            
    def raise_anchor(self):
        if self.anchor and not self.anchor.is_dropped:
            self.anchor.raise_anchor()
            
    def can_move(self):
        if self.oars is None:
            return False
        if self.anchor.is_dropped or self.anchor is None or self.anchor.wear >= 10:
            return False
        for oar in self.oars:
            if oar.wear >= 10:
                return False
        return True
    
    def start_rowing(self):
        if self.can_move():
            for oar in self.oars:
                oar.start_rowing()
                
    def stop_rowing(self):
        if self.can_move():
            for oar in self.oars:
                oar.stop_rowing()
                
    def is_moving(self):
        if not self.can_move():
            return False
        return any(oar.is_rowing for oar in self.oars)
    
    def get_speed(self):
        if not self.is_moving():
            return 0
        active_oars = [oar for oar in self.oars if oar.is_rowing]
        eff = [oar.get_eff() for oar in active_oars]
        return sum(eff) / len(eff)