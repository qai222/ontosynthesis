from __future__ import annotations

from owlready2 import ObjectProperty, Thing, DataProperty, AllDisjoint, FunctionalProperty

from ontosynthesis.ontology.base import ONTOLOGY, has_part
from ontosynthesis.ontology.benchtop import HardwareUnit
from ontosynthesis.ontology.chemical import MaterialEntity

with ONTOLOGY:
    """
    define the recipe ontology here, it describes the general, interoperable operation graph
    usually adapted from an Ord.Reaction record
    """


    class MaterialTransform(Thing):
        pass


    class has_material_input(ObjectProperty):
        domain = [MaterialTransform]
        range = [MaterialEntity]


    class has_material_output(ObjectProperty):
        domain = [MaterialTransform]
        range = [MaterialEntity]


    class is_preceded_by(ObjectProperty):
        domain = [MaterialTransform]
        range = [MaterialTransform]


    class Operation(Thing):
        pass


    class preceded_by(ObjectProperty):
        domain = [Operation]
        range = [Operation]


    class has_material_cost(ObjectProperty):
        domain = [Operation]
        range = [MaterialEntity]


    class has_temporal_cost(DataProperty):
        domain = [Operation]
        range = [float]


    class FunctionalModule(Thing):
        equivalent_to = [Thing & has_part.min(1, HardwareUnit)]


    class can_be_realized_by(ObjectProperty):
        domain = [Operation]
        range = [FunctionalModule]


    class is_realized_by(ObjectProperty, FunctionalProperty):
        domain = [Operation]
        range = [FunctionalModule]


    class MaterialAddition(Operation):
        pass


    class MaterialMixing(Operation):
        pass


    class MaintainingTemperature(Operation):
        pass


    AllDisjoint([MaterialAddition, MaterialMixing, MaintainingTemperature])
