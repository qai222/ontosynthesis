from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Type
from uuid import uuid4

from owlready2 import DataProperty, Thing
from pydantic import BaseModel

from protege import ontologies as onto


def str_uuid() -> str:
    return str(uuid4())


class OsThing(ABC, BaseModel):
    identifier: str = ""
    iri: str | None = None

    @property
    def onto_instance(self):
        assert self.iri is not None
        return onto.onto.search_one(iri=self.iri)

    @abstractmethod
    def create_ontology(self) -> Thing:
        pass

    def model_post_init(self, *args) -> None:
        # add uuid if not specified
        if self.identifier == "":
            self.identifier = str_uuid()

        with onto.onto:
            instance = self.create_ontology()

        self.iri = instance.iri


def create_ontology_instance(onto_cls: Type, name: str | None = None):
    onto_name = f"{onto_cls.__name__}: {name}"
    if name is None:
        return onto_cls()
    else:
        return onto_cls(name=onto_name)


with onto.onto:
    class has_string_value(DataProperty):
        range = [str]


    class has_numeric_value(DataProperty):
        range = [float, int]
