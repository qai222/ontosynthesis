from owlready2 import ObjectProperty, TransitiveProperty, Thing, FunctionalProperty, AllDisjoint

from ontosynthesis.ontology.base import ONTOLOGY

with ONTOLOGY:
    """
    define the bench top ontology here, it will be used to define the state of a workstation/platform
    """


    class HardwareUnit(Thing):
        pass


    class Consumable(HardwareUnit):
        pass


    class Device(HardwareUnit):
        pass


    AllDisjoint([Consumable, Device])


    class held_by(ObjectProperty, TransitiveProperty):
        domain = [HardwareUnit]
        range = [HardwareUnit]


    class holds(ObjectProperty, TransitiveProperty):
        domain = [HardwareUnit]
        range = [HardwareUnit]
        inverse_property = held_by


    class directly_held_by(held_by, FunctionalProperty):
        domain = [HardwareUnit]
        range = [HardwareUnit]


    class directly_holds(holds):
        domain = [HardwareUnit]
        range = [HardwareUnit]
        inverse_property = directly_held_by

    # class UnitHolder(Device):
    #     equivalent_to = [Device & ]
