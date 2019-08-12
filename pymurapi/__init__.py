from pymurapi import api
from pymurapi import simulator
from pymurapi import auv


def mur_init():
    import sys
    if sys.platform == 'win32':
        sim = simulator.Simulator()
        sim.prepare()
        return sim
    else:
        sub = auv.Auv()
        sub.prepare()
        return sub
