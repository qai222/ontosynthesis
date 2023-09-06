from __future__ import annotations

from ontosynthesis.base import create_relation, create_individual, create_relation_data, has_value_bijective, \
    has_value_functional
from ontosynthesis.resource import afo
from ontosynthesis.resource.ord_betterproto import *


def adapt_compound_identifier(compound_identifier: CompoundIdentifier) -> afo.MaterialIdentifier:
    """
    create individuals/relations given a `CompoundIdentifier`

    :param compound_identifier:
    :return:
    """
    identifier = create_individual(afo.MaterialIdentifier)
    if compound_identifier.type.name == CompoundIdentifierType.SMILES:
        identifier.is_a.append(afo.SmilesMolecularStructure)
    elif compound_identifier.type.name == CompoundIdentifierType.INCHI:
        identifier.is_a.append(afo.InchiMolecularStructure)
    elif compound_identifier.type.name == CompoundIdentifierType.NAME:
        identifier.is_a.append(afo.ChemicalName)

    create_relation_data(identifier, has_value_functional, compound_identifier.value)

    return identifier


def adapt_amount(amount: Amount) -> afo.AmountOfSubstance:
    """
    create individuals/relations given a `Amount`

    :param amount:
    :return:
    """
    one_of_field, one_of_message = betterproto.which_one_of(amount, group_name="kind")
    one_of_message: Mass | Volume | Moles

    amount = create_individual(afo.AmountOfSubstance, )
    quantity_kind = create_individual(afo.QuantityKind, label=one_of_field, label_as_name=True)
    unit = create_individual(afo.UnitOfMeasure, label=one_of_message.units.name, label_as_name=True)

    create_relation(amount, afo.has_quantity_kind, quantity_kind)
    create_relation(amount, afo.has_unit, unit)

    create_relation_data(amount, has_value_functional, one_of_message.value)
    create_relation_data(quantity_kind, has_value_bijective, one_of_field)
    create_relation_data(unit, has_value_bijective, one_of_message.units.name)

    return amount


def adapt_compound(compound: Compound | ProductCompound) -> afo.PortionOfCompound:
    # TODO phase

    portion_of_compound = create_individual(afo.PortionOfCompound)

    for ci in compound.identifiers:
        identifier = adapt_compound_identifier(ci)
        create_relation(identifier, afo.identifies, portion_of_compound)

    if isinstance(compound, Compound):
        amount = adapt_amount(compound.amount)
        amount_quality = create_individual(afo.AmountOfSubstance_quality)
        create_relation(portion_of_compound, afo.has_quality, amount_quality)
        create_relation(amount_quality, afo.quantified_by, amount)

    role = create_individual(afo.SynthesisRole, label=ReactionRoleType(compound.reaction_role).name, label_as_name=True)
    create_relation(portion_of_compound, afo.has_role, role)
    create_relation_data(role, has_value_bijective, ReactionRoleType(compound.reaction_role).name)

    return portion_of_compound


def adapt_reaction_input_or_output(rio: ReactionInput | ReactionOutcome) -> afo.ChemicalMixture | afo.PortionOfCompound:
    # TODO phase
    # TODO reaction_input has no amount field, use crudecompound to represent ex. a grignard reagent

    if isinstance(rio, ReactionInput):
        cs = rio.components
    elif isinstance(rio, ReactionOutcome):
        cs = rio.products
    else:
        raise TypeError

    if len(cs) == 1:
        compound = adapt_compound(cs[0])
        return compound
    else:
        mixture = create_individual(afo.ChemicalMixture)
        for c in cs:
            compound = adapt_compound(c)
            create_relation(mixture, afo.has_ingredient, compound)
        return mixture


def adapt_reaction(reaction: Reaction):
    # a synthesis process is a combination of
    # 1. addition of reaction input to reactor
    # 2. maintaining reaction condition
    # they can overlap temporally
    #
    # it does not include
    # 3. reaction input preparation ex. making stock solution, premix

    reactor = create_individual(afo.Reactor)

    # reaction inputs
    reaction_inputs = sorted(list(reaction.inputs.values()), key=lambda x: x.addition_order)
    total_material_input = create_individual(afo.ChemicalMixture)
    addition_processes = []
    for ri in reaction_inputs:
        mixture_input = adapt_reaction_input_or_output(ri)
        create_relation(total_material_input, afo.has_ingredient, mixture_input)

        addition_process = create_individual(afo.Adding_material)
        addition_device = create_individual(afo.TransferringDevice)
        source_container = create_individual(afo.Container)
        addition_duration = create_individual(afo.Duration)  # TODO add addition time

        create_relation(addition_process, afo.has_target_start_location, source_container)
        create_relation(addition_process, afo.has_duration, addition_duration)
        create_relation(addition_process, afo.has_target_end_location, reactor)
        create_relation(addition_process, afo.has_participant, mixture_input)
        create_relation(addition_process, afo.has_participant, addition_device)

        addition_processes.append(addition_process)

    # TODO assuming no concurrent addition for now
    for i in range(len(addition_processes) - 1):
        create_relation(addition_processes[i], afo.precedes, addition_processes[i + 1])

    # actual reaction
    actual_reaction_process = create_individual(afo.ChemicalReaction_molecular)
    mixture_output = adapt_reaction_input_or_output(reaction.outcomes[-1])  # TODO only the last
    duration = create_individual(afo.ReactionDuration)
    temperature = create_individual(afo.Temperature)
    create_relation_data(duration, has_value_functional, reaction.outcomes[-1].reaction_time.value)  # TODO unit
    create_relation_data(temperature, has_value_functional, reaction.conditions.temperature.setpoint.value)  # TODO unit
    create_relation(actual_reaction_process, afo.has_description, duration)
    create_relation(actual_reaction_process, afo.has_description, temperature)
    create_relation(actual_reaction_process, afo.has_participant, reactor)
    create_relation(actual_reaction_process, afo.has_material_input, total_material_input)
    create_relation(actual_reaction_process, afo.has_material_output, mixture_output)
    create_relation(addition_processes[-1], afo.precedes, actual_reaction_process)

    synthesis_process = create_individual(afo.Synthesis)
    create_relation(synthesis_process, afo.has_proper_part, actual_reaction_process)
    for p in addition_processes:
        create_relation(synthesis_process, afo.has_proper_part, p)
    return synthesis_process
