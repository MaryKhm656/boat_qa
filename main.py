from models.anchor import Anchor
from models.oar import Oar
from models.boat import Boat

oar_1 = Oar(25.5, 'дерево')
oar_2 = Oar(25.5, 'дерево')

anchor_1 = Anchor(120, 25.25)

my_boat = Boat('дерево', 25.25, 2, anchor=anchor_1, oars=(oar_1, oar_2))

my_boat.start_rowing()
my_boat.start_rowing()

print(my_boat.get_speed())
print(my_boat)