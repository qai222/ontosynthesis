from __future__ import annotations

from owlready2 import ObjectProperty, Thing, AllDisjoint, DataProperty

from ontosynthesis.ontology import data_types
from ontosynthesis.ontology.base import ONTOLOGY, has_part
from ontosynthesis.ontology.benchtop import HardwareUnit

with ONTOLOGY:
    """
    define the chemical ontology here, it will be used to define the substances on a workstation/platform
    note it depends on bench top ontology
    """


    class MaterialEntity(Thing):
        pass


    class SolidMaterial(MaterialEntity):
        pass


    class LiquidMaterial(MaterialEntity):
        pass


    AllDisjoint([SolidMaterial, LiquidMaterial])


    class chemically_quantified_by(DataProperty):
        domain = [MaterialEntity]
        range = [data_types.Compound]


    class is_made_of(has_part):
        """
        A is_made_of B means A is made by **directly** mixing B with at least one other material entity

        a subproperty of a transitive property can be non-transitive, this has been fixed in owlready2, see
        http://owlready.306.s1.nabble.com/subproperty-of-a-transitive-property-is-always-transitive-td3248.html
        """
        domain = [MaterialEntity]
        range = [MaterialEntity]


    class contained_by(ObjectProperty):
        """ assuming all chemicals are contained """
        domain = [MaterialEntity]
        range = [HardwareUnit]


    class contains(ObjectProperty):
        domain = [HardwareUnit]
        range = [MaterialEntity]
        inverse_property = contained_by


    class ChemicalContainer(HardwareUnit):
        equivalent_to = [HardwareUnit & contains.min(1, MaterialEntity)]
