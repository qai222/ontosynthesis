from __future__ import annotations

from typing import Type

from owlready2 import Thing
from owlready2 import ThingClass, DataProperty, ObjectProperty, get_ontology

from ontosynthesis.resource import afo

ONTO = get_ontology("http://ontosynthesis.org/ontosynthesis.owl")
ONTO.imported_ontologies.append(afo.onto)

with ONTO:
    has_value = ONTO.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000690")
    has_value.python_name = "has_value"


def create_individual(cls: ThingClass):
    with ONTO:
        ind = cls()
        # TODO not very sure about this...
        ind_suffix = ind.iri.split("#")[-1]
        cls_suffix = cls.iri.split("#")[-1]
        index = ind_suffix[len(cls_suffix):]

        lab = f"{list(cls.label)[0]} ({index})"
        ind.label.append(lab)


def create_relation(sub: Thing, pred: Type[ObjectProperty], obj: Thing, ) -> None:
    with ONTO:
        getattr(sub, pred.python_name).append(obj)


def create_relation_data(sub: Thing, pred: Type[DataProperty], obj: int | float | str) -> None:
    with ONTO:
        if obj is not None:
            getattr(sub, pred.python_name).append(obj)
