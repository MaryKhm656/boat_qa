from models.oar import Oar

def test_wear_of_oars_after_rowing():
    oar_1 = Oar(10, 'дерево')
    oar_1.start_rowing()
    oar_1.stop_rowing()
    assert oar_1.wear == 1

def test_efficiency_declines_with_wear():
    oar_1 = Oar(10, 'дерево', 5)
    assert oar_1.get_eff() == 0.5

def test_wear_variability_only_when_rowing_stops():
    oar_1 = Oar(10, 'дерево')
    assert oar_1.wear == 0
    oar_1.start_rowing()
    oar_1.start_rowing()
    assert oar_1.wear == 0
    oar_1.stop_rowing()
    assert oar_1.wear == 1