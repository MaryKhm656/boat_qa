from models.oar import Oar
from models.anchor import Anchor
from models.boat import Boat

def test_create_boat_without_oars():
    boat_1 = Boat('дерево', 30, 2)
    assert boat_1.can_move() == False
    
def test_create_boat_with_bad_anchor():
    anchor_1 = Anchor(365, 100, 10)
    boat_1 = Boat('дерево', 30, 2, anchor=anchor_1)
    assert boat_1.can_move() == False
    
def test_move_boat_without_oars():
    boat_1 = Boat('дерево', 30, 2)
    boat_1.start_rowing()
    assert boat_1.is_moving() == False

def test_successful_rowing():
    oar_1 = Oar(10, 'дерево')
    boat_1 = Boat('дерево', 30, 2, oars={oar_1})
    boat_1.start_rowing()
    assert boat_1.get_speed() == 1.0
    
def test_added_oar_after_create_boat():
    boat_1 = Boat('дерево', 30, 2)
    assert boat_1.can_move() == False
    oar_1 = Oar(10, 'дерево')
    boat_1.add_oar(oar_1)
    assert boat_1.can_move() == True


def test_is_moving_method():
    oar_1 = Oar(10, 'дерево')
    boat_1 = Boat('дерево', 30, 2, oars={oar_1})
    boat_1.start_rowing()
    assert boat_1.is_moving() == True
    
def test_speed_for_two_oars():
    oar_1 = Oar(10, 'дерево', wear=2)
    oar_2 = Oar(11, 'дерево')
    boat_1 = Boat('дерево', 30, 2, oars={oar_1, oar_2})
    boat_1.start_rowing()
    assert boat_1.get_speed() == 0.9