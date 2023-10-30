from __future__ import annotations

from owlready2 import ObjectProperty, FunctionalProperty, Thing, AllDisjoint

from ontosynthesis.ontology_state.base import ONTOLOGY_STATE, has_part
from ontosynthesis.ontology_state.benchtop import HardwareUnit
from ontosynthesis.ontology_state.data_properties import has_value_json_string

with ONTOLOGY_STATE:
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
        python_name = "described_by"
        domain = [MaterialEntity]
        range = [MaterialInformation]


    class identified_by(ObjectProperty, FunctionalProperty):
        python_name = "identified_by"
        domain = [MaterialEntity]
        range = [MaterialIdentifier]


    class quantified_by(ObjectProperty, FunctionalProperty):
        python_name = "quantified_by"
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
        python_name = "has_ingredient"
        range = [MaterialIdentifier]


    class contained_by(ObjectProperty):
        """ assuming all chemicals are contained """
        python_name = "contained_by"
        domain = [MaterialPortion]
        range = [HardwareUnit]


    AllDisjoint([MaterialEntity, MaterialInformation])
    AllDisjoint([MaterialIdentifier, MaterialAmount])
    AllDisjoint([SolidMaterial, LiquidMaterial])
