from owlready2 import ObjectProperty, TransitiveProperty, AllDisjoint, Thing

from ontosynthesis.ontology_state.base import ONTOLOGY_STATE

with ONTOLOGY_STATE:
    class HardwareUnit(Thing):
        pass


    class held_by(ObjectProperty, TransitiveProperty):
        python_name = "held_by"
        domain = [HardwareUnit]
        range = [HardwareUnit]


    class Consumable(HardwareUnit):
        pass


    class Device(HardwareUnit):
        pass


    AllDisjoint([Consumable, Device])
