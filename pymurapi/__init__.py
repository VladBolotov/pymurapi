from pymurapi import api
from pymurapi import simulator
from pymurapi import auv
from pymurapi.usv import Usv

_mur_object = None


def mur_init():
    import sys
    global _mur_object
    if _mur_object is None:
        if sys.platform == 'win32':
            sim = simulator.Simulator()
            sim.prepare()
            _mur_object = sim
            return _mur_object
        else:
            sub = auv.Auv()
            sub.prepare()
            _mur_object = sub
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
