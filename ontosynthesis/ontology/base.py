from __future__ import annotations

from owlready2 import (get_ontology, ObjectProperty, TransitiveProperty, DataProperty,
                       FunctionalProperty, InverseFunctionalProperty)

ONTOLOGY = get_ontology("http://ontosynthesis.org/ontology.owl")

with ONTOLOGY:
    """
    define general properties here
    """


    class has_part(ObjectProperty, TransitiveProperty):
        pass


    class has_value(DataProperty):
        range = [str, float, int, bool]


    class has_value_functional(has_value, FunctionalProperty):
        pass


    class has_value_inverse_functional(has_value, InverseFunctionalProperty):
        pass


    class has_value_bijective(has_value, InverseFunctionalProperty, FunctionalProperty):
        pass
