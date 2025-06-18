from models.anchor import Anchor

def test_drop_and_raise_anchor():
    anchor_1 = Anchor(200, 100)
    assert anchor_1.is_dropped == False
    anchor_1.drop_anchor()
    assert anchor_1.is_dropped == True
    anchor_1.raise_anchor()
    assert anchor_1.is_dropped == False