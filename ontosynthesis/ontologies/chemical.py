from __future__ import annotations

from owlready2 import ObjectProperty, FunctionalProperty, Thing, AllDisjoint

from ontosynthesis.ontologies.base import ONTO, has_part
from ontosynthesis.ontologies.benchtop import HardwareUnit
from ontosynthesis.ontologies.data_properties import has_value_json_string

with ONTO:
    class MaterialInformation(Thing):
        is_a = [has_value_json_string.exactly(1, str)]


    class MaterialEntity(Thing):
        pass


    class MaterialIdentifier(MaterialInformation):
        pass


    class MaterialAmount(MaterialInformation):
        pass


    class SolidMaterial(MaterialEntity):
        pass


    class LiquidMaterial(MaterialEntity):
        pass


    class described_by(ObjectProperty):
        domain = [MaterialEntity]
        range = [MaterialInformation]


    class identified_by(ObjectProperty, FunctionalProperty):
        domain = [MaterialEntity]
        range = [MaterialIdentifier]


    class quantified_by(ObjectProperty, FunctionalProperty):
        domain = [MaterialEntity]
        range = [MaterialAmount]


    class MaterialPortion(MaterialEntity):
        equivalent_to = [
            MaterialEntity &
            identified_by.exactly(1, MaterialIdentifier) &
            quantified_by.exactly(1, MaterialAmount)
        ]


    class has_ingredient(has_part):
        """
        A has_ingredient B means A is made by **directly** mixing B with at least one other compound

        a subproperty of a transitive property can be non-transitive, this has been fixed in owlready2, see
        http://owlready.306.s1.nabble.com/subproperty-of-a-transitive-property-is-always-transitive-td3248.html
        """
        range = [MaterialIdentifier]


    class contained_by(ObjectProperty):
        """ assuming all chemicals are contained """
        domain = [MaterialPortion]
        range = [HardwareUnit]


    AllDisjoint([MaterialEntity, MaterialInformation])
    AllDisjoint([MaterialIdentifier, MaterialAmount])
    AllDisjoint([SolidMaterial, LiquidMaterial])
