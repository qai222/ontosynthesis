from __future__ import annotations

import copy
import math
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field

from ontosynthesis.base import create_relation, create_individual, ONTO
from ontosynthesis.resource import soo

"""
create owl description for a reaction
"""

F1_Filter = create_individual(
    soo.Filter, label="F1-Filter", label_as_name=True,
    json_data={"made of": "celite"}
)
Rotavap = create_individual(soo.RotaryEvaporatingModule, label="Rotavap1", label_as_name=True)
SvHopper = create_individual(soo.SolidTransporterModule, label="Junior-SvHopper", label_as_name=False)
Z1LiquidTransporter = create_individual(soo.LiquidTransporterModule, label="Junior-Z1LiquidModule", label_as_name=False)
Z2LiquidTransporter = create_individual(soo.LiquidTransporterModule, label="Junior-Z2LiquidModule", label_as_name=False)


def str_uuid() -> str:
    return str(uuid4())


class MaterialAmount(BaseModel):
    amount_unit: str
    amount_value: float
    details: str = ""

    def __mul__(self, other: float):
        if other == 0:
            return None
        return MaterialAmount(amount_unit=self.amount_unit, amount_value=self.amount_value * other,
                              details=self.details)

    def __add__(self, other: MaterialAmount):
        assert self.amount_unit == other.amount_unit
        if other == 0:
            return self
        return MaterialAmount(amount_unit=self.amount_unit, amount_value=self.amount_value + other.amount_value,
                              details=self.details)

    def __hash__(self):
        return hash((self.amount_value, self.amount_unit))

    def __eq__(self, other: MaterialAmount):
        return (self.amount_value, self.amount_unit) == (other.amount_value, other.amount_unit)

    def __gt__(self, other: MaterialAmount):
        return self.as_tuple().__gt__(other.as_tuple())


class MaterialContainer(BaseModel):
    identifier: str = Field(default_factory=str_uuid)
    made_of: str = 'glass'
    max_capacity: MaterialAmount

    def model_post_init(self, __context: Any) -> None:
        create_individual(soo.MaterialContainer, label=self.identifier, label_as_name=True, json_data=self.model_dump())

    @property
    def individual(self):
        return ONTO.search_one(iri=get_iri_from_identifier(self.identifier))


# define continuents
C1_Reactor = MaterialContainer(
    max_capacity=MaterialAmount(amount_unit="mL", amount_value=10)
)
C2_Vessel = MaterialContainer(
    max_capacity=MaterialAmount(amount_unit="mL", amount_value=20)
)
C3_Vessel = MaterialContainer(
    max_capacity=MaterialAmount(amount_unit="mL", amount_value=20)
)
ReactorStirrer = create_individual(soo.MagneticStirrerModule, label="Junior-ReactorStirrer")
HumanHands = create_individual(soo.MaterialTransporterModule, label="HumanHands")


def get_iri_from_identifier(identifier: str):
    return f"{ONTO.base_iri}{identifier}"


class PortionOfMaterial(BaseModel):
    identifier: str = Field(default_factory=str_uuid)

    composition: dict[str, MaterialAmount] = dict()

    state_of_matter: list[str] = []

    is_contained_by: MaterialContainer

    def teleporting(self, container: MaterialContainer) -> PortionOfMaterial:
        return PortionOfMaterial(composition=copy.deepcopy(self.composition),
                                 state_of_matter=copy.deepcopy(self.state_of_matter), is_contained_by=container)

    @property
    def individual(self):
        return ONTO.search_one(iri=get_iri_from_identifier(self.identifier))

    def __mul__(self, other: float) -> PortionOfMaterial:
        assert other <= 1
        composition = copy.deepcopy(self.composition)
        for k in composition:
            composition[k] *= other
        init_data = {k: v for k, v in self.model_dump().items() if k != 'identifier'}
        init_data['composition'] = composition
        prod = PortionOfMaterial(**init_data)
        return prod

    def __add__(self, other: PortionOfMaterial):
        if not other:
            return self
        assert self.is_contained_by.identifier == other.is_contained_by.identifier
        prod_composition = dict()
        for k in other.composition.keys():
            if k in self.composition.keys():
                prod_composition[k] += other.composition[k]
            else:
                prod_composition[k] = other.composition[k]
        init_data = {k: v for k, v in self.model_dump().items() if k != 'identifier'}
        init_data['composition'] = prod_composition
        prod = PortionOfMaterial(**init_data)
        return prod

    def model_post_init(self, __context: Any) -> None:
        pom = create_individual(soo.PortionOfMaterial, label=self.identifier, label_as_name=True,
                                json_data=self.model_dump())
        create_relation(pom, soo.is_contained_by,
                        ONTO.search_one(iri=get_iri_from_identifier(self.is_contained_by.identifier)))


def create_inventory_material(chemical_label: str, state_of_matter: str) -> PortionOfMaterial:
    # cid = CompoundIdentifier(identifier_type='chemical label', identifier_value=chemical_label)
    cid = f'chemical label: {chemical_label}'
    if state_of_matter == 'SOLID':
        camt = MaterialAmount(amount_unit='mg', amount_value=1000)
    else:
        camt = MaterialAmount(amount_unit='mL', amount_value=1000)
    imat_container = MaterialContainer(max_capacity=camt * 5)
    imat = PortionOfMaterial(composition={cid: camt}, state_of_matter=[state_of_matter], is_contained_by=imat_container)
    return imat


def create_inventory_materials() -> dict[str, soo.PortionOfMaterial]:
    _chemical_info = """
    | R1    | 143426-50-0 | triazolybenzenemethanol | 1.0 eq  |
    | R2    | 2564-83-2   | TEMPO                   | 0.2 eq  |
    | R3    | 3240-34-4   | BAIB                    | 2.25 eq |
    | S1    | 75-09-2     | DCM                     | -       |
    | S2    | 7732-18-5   | water                   | -       |
    | S3    | ? | methanol | - |
    """
    # | P     | 162848-16-0 | product acid            | 2.25 eq |
    inventory_materials = dict()
    for line in _chemical_info.strip().split("\n"):
        label, cas, name = [_s.strip() for _s in line.split('|')[1:-2]]
        if label.startswith("R"):
            som = 'SOLID'
        else:
            som = 'LIQUID'
        inventory_materials[label] = create_inventory_material(label, som)
    return inventory_materials


def create_addition(
        source_pom: PortionOfMaterial,
        target_container: MaterialContainer,
        already_there: PortionOfMaterial = None,
        transfer_ratio: float = 1.0,
        realized_by: soo.FunctionalModule = None,
):
    addition = create_individual(soo.CombiningMaterials)
    create_relation(addition, soo.has_material_input, source_pom.individual)

    transferred_composition = {k: v * transfer_ratio for k, v in source_pom.composition.items()}
    if already_there is not None:
        create_relation(addition, soo.has_material_input, already_there.individual)
        combined_composition = copy.deepcopy(already_there.composition)
        for k in transferred_composition:
            if k not in combined_composition:
                combined_composition[k] = transferred_composition[k]
            else:
                combined_composition[k] += transferred_composition[k]
    else:
        combined_composition = transferred_composition

    m_output = PortionOfMaterial(
        state_of_matter=source_pom.state_of_matter,
        is_contained_by=target_container,
        composition=combined_composition,
    )
    create_relation(addition, soo.has_material_output, m_output.individual)
    if realized_by:
        create_relation(addition, soo.is_realized_by, realized_by)
    return addition, [source_pom, already_there], m_output


def create_mixing(m_input: PortionOfMaterial, m_output: PortionOfMaterial):
    mixing = create_individual(soo.MixingWithAgitation,
                               json_data={"stirring rate": "500 rpm", "lasting time": "24 hrs"})
    create_relation(mixing, soo.is_realized_by, ReactorStirrer)
    create_relation(mixing, soo.has_material_input, m_input.individual)
    create_relation(mixing, soo.has_material_output, m_output.individual)
    return mixing, m_input, m_output


if __name__ == '__main__':
    INVENTORY_MATERIALS = create_inventory_materials()
    R1_to_be_added = INVENTORY_MATERIALS['R1'] * 0.005
    R2_to_be_added = INVENTORY_MATERIALS['R2'] * 0.005
    R3_to_be_added = INVENTORY_MATERIALS['R3'] * 0.005
    step1, (source_pom, already_there), m_output = create_addition(source_pom=R1_to_be_added,
                                                                   target_container=C1_Reactor,
                                                                   realized_by=SvHopper)
    step2, (_, _), m_output = create_addition(source_pom=R2_to_be_added, target_container=C1_Reactor,
                                              realized_by=SvHopper,
                                              already_there=m_output)
    step3, (_, _), m_output = create_addition(source_pom=R3_to_be_added, target_container=C1_Reactor,
                                              realized_by=SvHopper,
                                              already_there=m_output)

    S1_to_be_added = INVENTORY_MATERIALS['S1'] * 0.005
    S2_to_be_added = INVENTORY_MATERIALS['S2'] * 0.005
    step4, (_, _), m_output = create_addition(source_pom=S1_to_be_added, target_container=C1_Reactor,
                                              realized_by=Z1LiquidTransporter, already_there=m_output)
    step5, (_, _), m_output = create_addition(source_pom=S2_to_be_added, target_container=C1_Reactor,
                                              realized_by=Z2LiquidTransporter, already_there=m_output)

    # TODO how to represent unknown amount components?
    raw_reaction_mixture_after_reaction = PortionOfMaterial(
        composition={
            "Product": MaterialAmount(amount_unit="UNKNOWN", amount_value=math.inf),
            "IMPURITY": MaterialAmount(amount_unit="UNKNOWN", amount_value=math.inf),
        },
        state_of_matter=["UNKNOWN"], is_contained_by=C1_Reactor
    )

    step6, _, m_output = create_mixing(m_output, raw_reaction_mixture_after_reaction)

    step8, (_, _), m_output = create_addition(source_pom=m_output, target_container=C2_Vessel, realized_by=HumanHands)

    step9 = create_individual(soo.RotaryEvaporation)
    step9.is_a.append(soo.EndpointControlledProcess)
    create_relation(step9, soo.is_realized_by, Rotavap)
    m_input = m_output
    create_relation(step9, soo.has_separation_input, m_input.individual)
    m_output = m_input * 0.9  # magic to create a new pom
    create_relation(step9, soo.has_separation_output, m_output.individual)

    step10_methanol = INVENTORY_MATERIALS['S3'] * 0.01
    step10, (_, _), m_output = create_addition(step10_methanol, target_container=C2_Vessel, already_there=m_output,
                                               realized_by=Z1LiquidTransporter)

    m_input = m_output
    m_output = m_input * 1.0  # magic for a new pom
    step11, _, m_output = create_mixing(m_input, m_output)
    step11.is_a.append(soo.EndpointControlledProcess)

    # step 12 = 12 & 13
    step12 = create_individual(soo.Filtering)
    step12.is_a.append(soo.EndpointControlledProcess)
    m_input = m_output
    create_relation(step12, soo.is_realized_by, F1_Filter)
    create_relation(step12, soo.has_separation_input, m_input.individual)

    m_output = m_input.teleporting(C3_Vessel)
    # TODO note separation should have at least 2 outputs
    create_relation(step12, soo.has_material_output, m_output.individual)

    # TODO we skip step 14 and 15 as I'm not sure we shall call it a washing or filtering process
    step16 = create_individual(soo.RotaryEvaporation)
    step16.is_a.append(soo.EndpointControlledProcess)
    create_relation(step16, soo.is_realized_by, Rotavap)
    m_input = m_output
    create_relation(step16, soo.has_separation_input, m_input.individual)
    m_output = m_input * 0.9  # magic to create a new pom
    create_relation(step16, soo.has_separation_output, m_output.individual)

    create_relation(step16, soo.is_preceded_by, step12)
    create_relation(step12, soo.is_preceded_by, step11)
    create_relation(step11, soo.is_preceded_by, step10)
    create_relation(step10, soo.is_preceded_by, step9)
    create_relation(step9, soo.is_preceded_by, step8)
    create_relation(step8, soo.is_preceded_by, step6)
    create_relation(step6, soo.is_preceded_by, step5)
    create_relation(step5, soo.is_preceded_by, step4)
    create_relation(step4, soo.is_preceded_by, step3)
    create_relation(step3, soo.is_preceded_by, step2)
    create_relation(step2, soo.is_preceded_by, step1)

    # # run reasoner
    # from owlready2 import sync_reasoner
    # sync_reasoner(infer_property_values=True)
    ONTO.save("alcohol_oxidation.owl", format="rdfxml")
