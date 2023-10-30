from owlready2 import DataProperty, FunctionalProperty, InverseFunctionalProperty

from ontosynthesis.ontology_state.base import ONTOLOGY_STATE

with ONTOLOGY_STATE:
    # https://owlready2.readthedocs.io/en/v0.44/properties.html#data-property
    class has_value(DataProperty):
        python_name = "has_value"
        range = [str, float, int, bool]


    class has_value_functional(has_value, FunctionalProperty):
        python_name = "has_value_functional"


    class has_value_inverse_functional(has_value, InverseFunctionalProperty):
        python_name = "has_value_inverse_functional"


    class has_value_bijective(has_value, InverseFunctionalProperty, FunctionalProperty):
        python_name = "has_value_bijective"


    class has_value_json_string(has_value_functional):
        python_name = "has_value_json_string"


    range = [str]
