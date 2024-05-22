from pymurapi import simulator
from pymurapi.usv import Usv

_mur_object = None
AUV = "AUV"
USV = "USV"

def auv_init():
    global _mur_object
    if _mur_object is None:
        sim = simulator.Simulator()
        sim.prepare()
        _mur_object = sim
        return _mur_object
    else:
        return _mur_object


def usv_init():
    global _mur_object
    if _mur_object is None:
        sub = Usv()
        sub.prepare()
        _mur_object = sub
        return _mur_object
    else:
        return _mur_object


_init_switcher = {
    AUV: auv_init,
    USV: usv_init
}


def mur_init(vehicle_type=AUV):
    global _init_switcher
    try:
        return _init_switcher[vehicle_type]()
    except KeyError as e:
        print("Bad vehicle type in mur_init", e)
        exit(-1)
