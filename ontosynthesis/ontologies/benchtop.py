from owlready2 import ObjectProperty, TransitiveProperty, AllDisjoint, Thing

from ontosynthesis.ontologies.base import ONTO

with ONTO:
    class HardwareUnit(Thing):
        pass


    class held_by(ObjectProperty, TransitiveProperty):
        domain = [HardwareUnit]
        range = [HardwareUnit]


    class Consumable(HardwareUnit):
        pass


    class Device(HardwareUnit):
        pass


    AllDisjoint([Consumable, Device])
