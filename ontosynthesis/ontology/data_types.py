from __future__ import annotations

import json

from owlready2 import declare_datatype
from pydantic import BaseModel

from ontosynthesis.ontology.base import ONTOLOGY

"""
custom pydantic data types declared to be used as ranges for data properties
"""


class Amount(BaseModel):
    unit: str
    value: float

    @staticmethod
    def parser(json_string: str):
        return Amount(**json.loads(json_string))

    @staticmethod
    def unparser(amount: Amount):
        return amount.model_dump_json()

    def __hash__(self):
        return hash(self.model_dump_json())


class Compound(BaseModel):
    chemical_identifier: str
    amount: Amount

    @staticmethod
    def parser(json_string: str):
        return Compound(**json.loads(json_string))

    @staticmethod
    def unparser(compound: Amount):
        return compound.model_dump_json()

    def __hash__(self):
        return hash(self.model_dump_json())


declare_datatype(Amount, f"{ONTOLOGY.base_iri}#datatype-{Amount.__name__}", Amount.parser, Amount.unparser)
declare_datatype(Compound, f"{ONTOLOGY.base_iri}#datatype-{Compound.__name__}", Compound.parser, Compound.unparser)
