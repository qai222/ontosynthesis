from __future__ import annotations
from owlready2 import Thing

from ontosynthesis.base import OsThing, create_ontology_instance, has_numeric_value, has_string_value
from protege import ontologies as onto


with onto.onto:

    class CompoundIdentifier(OsThing):
        type: str
        value: str

        def create_ontology(self):
            identifier = create_ontology_instance(onto_cls=onto.MaterialIdentifier, name=self.value)
            identifier.is_a.append(onto.ChemicalName)
            identifier_class = create_ontology_instance(onto_cls=onto.Classification, name=self.type)
            identifier_class.classifies.append(identifier)
            return identifier

    class Amount(OsThing):
        unit: str
        value: float

        def create_ontology(self) -> Thing:
            amount = create_ontology_instance(onto_cls=onto.AmountOfSubstance)
            return amount

    class ReactionInput(OsThing):

        compounds: list[Compound]

        state_of_matter: str

        mixture_description: str

        def create_ontology(self) -> Thing:
            pass


    class Compound(OsThing):

        compound_identifier: CompoundIdentifier
        amount: Amount

        def create_ontology(self) -> Thing:
            compound = create_ontology_instance(onto_cls=onto.PortionOfCompound, name=self.identifier)
            self.compound_identifier.onto_instance.identifies.append(compound)
            self.amount.onto_instance.describes.append(compound)
            return compound

        def __add__(self, other: Compound):

            return Compound()




    class Container(OsThing):

        type: str

        def create_ontology(self) -> Thing:
            container_type = create_ontology_instance(onto_cls=onto.ContainerType, name=self.type)
            container = create_ontology_instance(onto_cls=onto.Container, name=self.identifier)
            container_type.classifies.append(onto.Container)
            return container

    class


    ci1 = CompoundIdentifier(type="SMILES", value="CC")
    ci2 = CompoundIdentifier(type="SMILES", value="CCCC")



    for i in onto.onto.individuals():
        print(i)


    #
    # from owlready2 import Thing
    # for i in Thing.instances():
    #     print(i.name, i.iri)
    # #
    # #
    # #
    # # class Compound(OsBaseClass):
    # #
    # #     identifiers: str
    # #
    # #     amount: float
    # #
    # #     amount_unit: str
    # #
    # #     def create_ontology_instances(self) -> None:
    # #
    # #         chemical_name = create_ontology_instance(onto_cls=onto.ChemicalName, name=self.chemical_name)
    # #         chemical_name.is_a.append()
    # #
    # #         portion_of_compound = create_ontology_instance(onto_cls=onto.PortionOfMaterial, name=self.identifier)
    # #
    # #         chemical_name.describes.append(portion_of_compound)
    # #
    # #         compound_amount = onto.AmountOfSubstance
    # #
    # #
    # #
    # # c = Compound(chemical_name="NaCl", amount=1.0, amount_unit="g")
    # # print([*onto.describes.get_relations()])
