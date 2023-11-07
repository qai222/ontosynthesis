from owlready2 import ObjectProperty, TransitiveProperty, AllDisjoint, Thing, FunctionalProperty

from ontosynthesis.ontology.base import ONTOLOGY

with ONTOLOGY:
    """
    define the bench top ontology here, it will be used to define the state of a workstation/platform
    """

    class HardwareUnit(Thing):
        pass


    class held_by(ObjectProperty, TransitiveProperty):
        python_name = "held_by"
        domain = [HardwareUnit]
        range = [HardwareUnit]


    # class holds(ObjectProperty, TransitiveProperty):
    #     python_name = "holds"
    #     domain = [HardwareUnit]
    #     range = [HardwareUnit]
    #     inverse_property = held_by


    class directly_held_by(held_by, FunctionalProperty):
        python_name = "directly_held_by"
        domain = [HardwareUnit]
        range = [HardwareUnit]


    # class directly_holds(holds):
    #     python_name = "directly_holds"
    #     domain = [HardwareUnit]
    #     range = [HardwareUnit]
    #     inverse_property = directly_held_by


    class Consumable(HardwareUnit):
        pass


    class Device(HardwareUnit):
        pass


    AllDisjoint([Consumable, Device])
