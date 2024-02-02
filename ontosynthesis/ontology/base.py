from __future__ import annotations

from typing import Type, Any

from loguru import logger
from owlready2 import (Thing, ThingClass, Property)
from owlready2 import (get_ontology, ObjectProperty, TransitiveProperty, DataProperty,
                       FunctionalProperty, InverseFunctionalProperty)

ONTOLOGY = get_ontology("http://ontosynthesis.org/main.owl")
# TODO separate lab and recipe

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


def create_individual(cls: ThingClass, name=None) -> Thing:
    """
    helper function to create a NamedIndividual in the master ontology
    """
    with ONTOLOGY:
        if name is not None:
            if ONTOLOGY[name] is not None:
                logger.warning(f"skip creating: {cls} there already exists: {ONTOLOGY[name]} as {ONTOLOGY[name].is_a}")
            ind = cls(name=name)
        else:
            ind = cls()
        return ind


def create_relation(sub: Thing, pred: Type[ObjectProperty], obj: Any, ) -> None:
    with ONTOLOGY:
        if issubclass(pred, FunctionalProperty):
            setattr(sub, pred.python_name, obj)
        else:
            getattr(sub, pred.python_name).append(obj)


def get_property(sub: Thing, pred: Type[Property], indirect=False):
    if indirect:
        p = "INDIRECT_" + pred.python_name
    else:
        p = pred.python_name
    return getattr(sub, p)
