from __future__ import annotations

import json
from typing import Type

from owlready2 import Thing, default_world
from owlready2 import ThingClass, DataProperty, ObjectProperty, get_ontology, InverseFunctionalProperty, \
    FunctionalProperty, Property


# from ontosynthesis.resource import afo
# ONTO.imported_ontologies.append(afo.onto)
# # Note: you need afo.owx to use this, see `ontologies/afo/afo.md`

from ontosynthesis.resource import soo

# # TODO if I import soo to ONTO I don't get to save soo classes from ONTO
# ONTO = get_ontology("http://ontosynthesis.org/ontosynthesis.owl")
# ONTO.imported_ontologies.append(soo.onto)
ONTO = soo.onto

with ONTO:
    class has_value(DataProperty):
        python_name = 'has_value'


    class has_value_functional(has_value, FunctionalProperty):
        python_name = "has_value_functional"


    class has_value_inverse_functional(has_value, InverseFunctionalProperty):
        python_name = "has_value_inverse_functional"


    class has_value_bijective(has_value, InverseFunctionalProperty, FunctionalProperty):
        python_name = "has_value_bijective"


def create_individual(
        cls: ThingClass,
        label: str | None = None,
        label_as_name: bool = False,
        json_data = None,
):
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
            ind_lab = f"{label}"
            if label_as_name:
                ind = cls(name=ind_lab)
            else:
                ind = cls()
        else:
            ind = cls()
            # TODO not very sure about this...
            ind_suffix = ind.iri.split("#")[-1]
            cls_suffix = cls.iri.split("#")[-1]
            index = ind_suffix[len(cls_suffix):]
            ind_lab = f"{cls_label}__{index}"
        ind.label.append(ind_lab)

        create_relation_data(ind, has_value_functional, json.dumps(json_data))
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

def inspect_individual(thing: Thing, print_label=True):
    for prop in thing.get_properties():
        objs = get_property(thing, prop)
        if not isinstance(objs, list):
            objs = [objs, ]
        for value in objs:
            if isinstance(value, str):
                print("self - %s -> %s" % (prop.python_name, value))
            else:
                if print_label:
                    print("self - %s -> %s" % (prop.python_name, value.label[0]))
                else:
                    print("self - %s -> %s" % (prop.python_name, value))

def inspect_individual_inverse(thing: Thing, print_label=True):
    for sub, prop in thing.get_inverse_properties():
        if print_label:
            print("%s - %s -> self" % (sub.label[0], prop.python_name))
        else:
            print("%s - %s -> self" % (sub, prop.python_name))

    # # or use sparql
    # q = f"""
    #        SELECT ?x ?y
    #        {{ <{thing.iri}> ?x ?y . }}
    # """
    # r = list(default_world.sparql(q))
    # for x, y in r:
    #     try:
    #         print(x.label, y.label)
    #     except AttributeError:
    #         print(x, y)


def get_property_inverse(obj: Thing, pred: Type[Property]):
    q = f"""
           SELECT ?x
           {{ ?x <{pred.iri}> <{obj.iri}> . }}
    """
    r = list(default_world.sparql(q))
    return r[0]

def get_data(thing):
    d = get_property(thing, has_value_functional)
    if d is None:
        return None
    return json.loads(d)
