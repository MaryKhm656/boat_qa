from models.anchor import Anchor
from models.oar import Oar
from models.boat import Boat

oar_1 = Oar(25.5, 'дерево')
oar_2 = Oar(25.5, 'дерево')

anchor_1 = Anchor(120, 25.25)

my_boat = Boat('дерево', 25.25, 2, anchor=anchor_1, oars=(oar_1, oar_2))

my_boat.start_rowing()

print(my_boat.get_speed())

oar_1 = Oar(10, 'дерево', wear=2)
oar_2 = Oar(11, 'дерево')
boat_1 = Boat('дерево', 30, 2, oars={oar_1, oar_2})
boat_1.start_rowing()
print(boat_1.get_speed())