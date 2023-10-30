from __future__ import annotations

from typing import Type

from owlready2 import (Thing, ThingClass, DataProperty, ObjectProperty, FunctionalProperty, Property)

from ontosynthesis.ontology_state import ONTOLOGY_STATE


def create_individual(cls: ThingClass, label: str | None = None, label_as_name: bool = False):
    """
    helper function to create a NamedIndividual in the master ontology

    :param ontology:
    :param cls:
    :param label:
    :param label_as_name: if Ture, the name will be set to "<class_name>__<label>",
    use this to avoid creating multiple individuals
    :return:
    """
    with ONTOLOGY_STATE:
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


def create_relation(sub: Thing, pred: Type[ObjectProperty], obj: Thing, ) -> None:
    with ONTOLOGY_STATE:
        getattr(sub, pred.python_name).append(obj)


def create_relation_data(sub: Thing, pred: Type[DataProperty], obj: int | float | str) -> None:
    if obj is None:
        return
    with ONTOLOGY_STATE:
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
