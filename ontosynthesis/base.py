from __future__ import annotations

from typing import Type

from owlready2 import Thing
from owlready2 import ThingClass, DataProperty, ObjectProperty, get_ontology, InverseFunctionalProperty, \
    FunctionalProperty, Property

from ontosynthesis.resource import afo

ONTO = get_ontology("http://ontosynthesis.org/ontosynthesis.owl")
ONTO.imported_ontologies.append(afo.onto)

with ONTO:
    has_value = ONTO.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000690")
    has_value.python_name = "has_value"


    class has_value_functional(has_value, FunctionalProperty):
        python_name = "has_value_functional"


    class has_value_inverse_functional(has_value, InverseFunctionalProperty):
        python_name = "has_value_inverse_functional"


    class has_value_bijective(has_value, InverseFunctionalProperty, FunctionalProperty):
        python_name = "has_value_bijective"


def create_individual(cls: ThingClass, label: str | None = None, label_as_name: bool = False):
    """
    helper function to create a NamedIndividual in the master ontology

    :param cls:
    :param label:
    :param label_as_name: if Ture, the name will be set to "<class_name>__<label>",
    use this to avoid creating multiple individuals
    :return:
    """
    with ONTO:
        cls_label = list(cls.label)[0]
        if label is not None:
            ind_lab = f"{cls_label}__{label}"
            if label_as_name:
                ind = cls(name=ind_lab)
        else:
            ind = cls()
            # TODO not very sure about this...
            ind_suffix = ind.iri.split("#")[-1]
            cls_suffix = cls.iri.split("#")[-1]
            index = ind_suffix[len(cls_suffix):]
            ind_lab = f"{cls_label}__{index}"
        ind.label.append(ind_lab)
        return ind

        # # include label in iri
        # if label is None:
        #     ind = cls()
        #     ind_suffix = ind.iri.split("#")[-1]
        #     cls_suffix = cls.iri.split("#")[-1]
        #     index = ind_suffix[len(cls_suffix):]
        #     lab = f"{list(cls.label)[0]}__{index}"
        # else:
        #     lab = f"{list(cls.label)[0]}__{label}"
        #     ind = cls(name=lab)
        # ind.label.append(lab)
        # return ind


def create_relation(sub: Thing, pred: Type[ObjectProperty], obj: Thing, ) -> None:
    with ONTO:
        getattr(sub, pred.python_name).append(obj)


def create_relation_data(sub: Thing, pred: Type[DataProperty], obj: int | float | str) -> None:
    if obj is None:
        return
    with ONTO:
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
