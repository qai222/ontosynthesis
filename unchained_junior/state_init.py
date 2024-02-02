from loguru import logger
from owlready2 import AllDisjoint, default_world, sync_reasoner

from ontosynthesis import ontology as os
from ontosynthesis.ontology import ONTOLOGY, create_individual, create_relation, ObjectProperty, FunctionalProperty, directly_held_by
from ontosynthesis.platforms.unchained_junior import create_platform
from ontosynthesis.ontology.data_types import Compound, Amount

with ONTOLOGY:
    class Slot(os.HardwareUnit):
        pass


    class Plate(os.HardwareUnit):
        pass


    class Deck(os.HardwareUnit):
        pass


    class Arm1(os.HardwareUnit):
        pass


    class Arm2(os.HardwareUnit):
        pass


    class ArmPlatform(os.HardwareUnit):
        pass


    class Vial(os.Consumable):
        pass


    class SolidVial(Vial):
        pass


    class PdpTip(os.Consumable):
        pass


    class Needle(os.HardwareUnit):
        pass


    class PlateGripper(os.HardwareUnit):
        pass


    class SvHead(os.HardwareUnit):
        pass


    class PdpHead(os.HardwareUnit):
        pass


    AllDisjoint([Slot, Plate, Arm1, Arm2, ArmPlatform, Vial, PdpTip, Needle, PlateGripper, SvHead, PdpHead])


    class on_top_of(ObjectProperty, FunctionalProperty):
        pass


def create_compound(material_identifier: str, amount_value: float, amount_unit: str):
    amount = Amount(unit=amount_unit, value=amount_value)
    compound = Compound(chemical_identifier=material_identifier, amount=amount)
    return compound


def create_material(compounds: list[Compound]):
    m = create_individual(os.MaterialEntity)
    for c in compounds:
        create_relation(m, os.has_ingredient, c)
    return m



def get_holding_slot(ind):
    query = f"""
        SELECT ?o
        WHERE {{
        <{ind.iri}> <{directly_held_by.iri}>+ ?o .
        ?o a <{Slot.iri}>
        }}
    """
    r = list(default_world.sparql(query))
    return r[0][0]


def get_chain_property_values(ind, pred, is_sub=True):
    if is_sub:
        query = f"""
            SELECT ?o
            WHERE {{
            <{ind.iri}> <{pred.iri}>+ ?o
            }}
        """
    else:
        query = f"""
        SELECT ?o
        WHERE {{
        ?o <{pred.iri}>+ <{ind.iri}> 
        }}
    """
    print(query)
    r = list(default_world.sparql(query))
    return [i for sublist in r for i in sublist]


def operation__pick_up_simple(sub: os.HardwareUnit, obj: os.HardwareUnit):
    arm = Arm2.instances()[0]
    logger.info(f"intend to pick up object: {obj}")
    logger.info(f"using: {arm}")
    # where is the object?
    holding_slot = get_holding_slot(obj)
    logger.info(f"the object: {obj} is found in the Slot: {holding_slot}")
    # if move the platform
    arm_platform = ArmPlatform.instances()[0]
    if arm_platform.on_top_of != holding_slot:
        logger.info(f"move {arm_platform} from: {arm_platform.on_top_of} to: {holding_slot}")
        arm_platform.on_top_of = holding_slot
    else:
        logger.info(f"skip moving as {arm_platform} is already on top of: {holding_slot}")

    logger.info(f"the object: {obj} is lifted from its direct holder: {obj.directly_held_by}")
    obj.directly_held_by = sub
    logger.info(f"the object: {obj} is now directly held by: {obj.directly_held_by}")


def operation__pick_up(obj: os.HardwareUnit, ):
    arm = Arm2.instances()[0]
    already_holds = get_chain_property_values(arm, os.directly_held_by, is_sub=False)
    logger.info(f"the arm already holds: {already_holds}")
    if obj in already_holds:
        logger.info(f"the object: {obj} already picked up, this operation is skipped!")
        return

    assert obj.directly_held_by, f"cannot pick up: {obj} that is not directly held by anything!"
    logger.info(f"the object: {obj} is directly held by: {obj.directly_held_by}")

    # compatibility
    if SolidVial in obj.is_a:
        # TODO sv vial is actually allowed
        raise RuntimeError("the object is a Vial, this is not allowed")
    elif Plate in obj.is_a:
        logger.info(f"picking up a {Plate.__name__}")
        required_head_class = PlateGripper
    elif SolidVial in obj.is_a:
        logger.info(f"picking up a {SolidVial.__name__}")
        required_head_class = SvHead
    elif PlateGripper in obj.is_a:
        logger.info(f"picking up a {PlateGripper.__name__}")
        required_head_class = None
    elif SvHead in obj.is_a:
        logger.info(f"picking up a {SvHead.__name__}")
        required_head_class = None
    else:
        # TODO other situations, ex. PdpHead, PdpTip
        raise NotImplementedError

    if required_head_class is None:
        logger.info("no head required for this object, but the arm should directly hold nothing")
        if len(already_holds):
            logger.info("the arm already holds something, proceed to put them down")
            # TODO implement
        else:
            operation__pick_up_simple(arm, obj)
            return
    else:
        required_head = None
        for u in arm.INDIRECT_directly_holds:
            if required_head_class in u.is_a:
                required_head = u
                logger.info("required head is already attached")
                break
        if required_head is None:
            logger.info(f"need to first pick up a required head of class: {required_head_class}")
            required_head = required_head_class.instances()[0]  # TODO more selection rules
            operation__pick_up(required_head)
        if len(required_head.INDIRECT_directly_holds):
            logger.info("the head already holds something, proceed to put it down")
            # TODO implement
        operation__pick_up_simple(required_head, obj)



create_platform()
# sync_reasoner(infer_property_values=True)

# v0 = Vial.instances()[0]
p0 = Plate.instances()[0]
# p1 = Plate.instances()[2]
ONTOLOGY.save("before_operation.owl", format="rdfxml")
operation__pick_up(p0)
# # operation__pick_up(p1)
ONTOLOGY.save("after_operation.owl", format="rdfxml")
# # sync_reasoner(infer_property_values=True)
