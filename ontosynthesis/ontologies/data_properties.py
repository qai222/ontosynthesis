from owlready2 import DataProperty, FunctionalProperty

from ontosynthesis.ontologies.base import ONTO

with ONTO:
    # https://owlready2.readthedocs.io/en/v0.44/properties.html#data-property
    class has_value(DataProperty, FunctionalProperty):
        python_name = "has_value"
        range = [str, float, int, bool]


    class has_value_json_string(has_value):
        python_name = "has_value_json_string"
        range = [str]
