from pymurapi import api
from pymurapi import simulator
from pymurapi import auv

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
            mur_init.mur_object = sub
            return _mur_object
    else:
        return _mur_object
