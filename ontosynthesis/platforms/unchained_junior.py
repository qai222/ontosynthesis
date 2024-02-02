from owlready2 import AllDisjoint

from ontosynthesis.ontology import (
    ONTOLOGY, ObjectProperty, FunctionalProperty, create_individual, create_relation, HardwareUnit, Consumable,
    directly_held_by
)

with ONTOLOGY:
    class Vial(Consumable):
        pass


    class Plate(HardwareUnit):
        pass


    class Deck(HardwareUnit):
        pass


    class Slot(HardwareUnit):
        pass


    class Arm1(HardwareUnit):
        pass


    class Arm2(HardwareUnit):
        pass


    class ArmPlatform(HardwareUnit):
        pass


    class PdpTip(Consumable):
        pass


    class Needle(HardwareUnit):
        pass


    class PlateGripper(HardwareUnit):
        pass


    class SvHead(HardwareUnit):
        pass


    class PdpHead(HardwareUnit):
        pass


    AllDisjoint([Slot, Plate, Arm1, Arm2, ArmPlatform, Vial, PdpTip, Needle, PlateGripper, SvHead, PdpHead])


    class on_top_of(ObjectProperty, FunctionalProperty):
        domain = [ArmPlatform]
        range = [Slot]


def create_deck(deck_name: str, num_of_plate_slots=3):
    deck = create_individual(Deck, deck_name)
    for i in range(num_of_plate_slots):
        plate_slot = create_individual(Slot)
        create_relation(plate_slot, directly_held_by, deck)
    return deck


def create_plate(vial_occupation: int = 8, tip_occupation: int = 0):
    plate = create_individual(Plate)
    assert vial_occupation * tip_occupation == 0, "a plate cannot hold both vials and tips!"
    for j in range(vial_occupation):
        vial = create_individual(Vial)
        create_relation(vial, directly_held_by, plate)
    for j in range(tip_occupation):
        tip = create_individual(PdpTip)
        create_relation(tip, directly_held_by, plate)
    return plate


def create_platform(
        slot_occupation=(1, 0, 0, 1, 1, 1),
        vial_occupations=(8, 0, 0, 8, 8, 0),
        tip_occupations=(0, 0, 0, 0, 0, 30),
):
    # off deck
    off_deck = create_individual(Deck, "OffDeck", )
    for i in range(3):
        plate_slot = create_individual(Slot, f"{off_deck.name}-{i}")
        create_relation(plate_slot, directly_held_by, off_deck)
        if slot_occupation[i]:
            plate = create_plate(vial_occupations[i], tip_occupations[i])  # plate index == slot index
            create_relation(plate, directly_held_by, plate_slot)

    # deck 1 (wash bay)
    deck_1 = create_individual(Deck, "Deck-1")
    wash_bay = create_individual(Slot, "WashBay")
    create_relation(wash_bay, directly_held_by, deck_1)

    # deck 2 (2-3)
    deck2 = create_individual(Deck, "Deck-2")
    for i in range(3, 6):
        plate_slot = create_individual(Slot, f"forPlate-{i}")
        create_relation(plate_slot, directly_held_by, deck2)
        if slot_occupation[i]:
            plate = create_plate(vial_occupations[i], tip_occupations[i])  # plate index == slot index
            create_relation(plate, directly_held_by, plate_slot)

    # deck 3 (4-5)
    deck3 = create_individual(Deck, "Deck-3")
    sv_head_slot = create_individual(Slot, "forSvHead")
    create_relation(sv_head_slot, directly_held_by, deck3)
    sv_head = create_individual(SvHead)
    create_relation(sv_head, directly_held_by, sv_head)
    for i in range(12):
        sv_vial = create_individual(Vial, f"Sv-{i}")
        sv_vial_slot = create_individual(Slot, f"forSv-{i}")
        create_relation(sv_vial, directly_held_by, sv_vial_slot)
        create_relation(sv_vial_slot, directly_held_by, deck3)
    for i in range(3):
        pdp_head_slot = create_individual(Slot, f"forPdpHead-{i}")
        pdp_head = create_individual(PdpHead, f"PdpHead-{i}")
        create_relation(pdp_head_slot, directly_held_by, deck3)
        create_relation(pdp_head, directly_held_by, pdp_head_slot)

    # deck 4 (6-8)
    deck4 = create_individual(Deck, "Deck-4", )
    balance = create_individual(Slot, "Balance", )
    create_relation(balance, directly_held_by, deck4)

    # deck 5 (9-10)
    deck5 = create_individual(Deck, "Deck-5", )
    gripper_slot = create_individual(Slot, "forGripper", )
    create_relation(gripper_slot, directly_held_by, deck5)
    gripper = create_individual(PlateGripper, "Gripper", )
    create_relation(gripper, directly_held_by, gripper_slot)

    # deck 6 (11)
    deck6 = create_individual(Deck, "Deck-6", )
    tip_disposal = create_individual(Slot, "TipDisposal", )
    create_relation(tip_disposal, directly_held_by, deck6)

    # robot arms
    arm_platform = create_individual(ArmPlatform, )
    arm_1 = create_individual(Arm1, "Arm-1", )
    arm_2 = create_individual(Arm2, "Arm-2", )
    create_relation(arm_1, directly_held_by, arm_platform)
    create_relation(arm_2, directly_held_by, arm_platform)
    create_relation(arm_platform, on_top_of, wash_bay)
    # needles on z1
    for i in range(6):
        needle = create_individual(Needle, f"Needle-{i}", )
        create_relation(needle, directly_held_by, arm_1)

# deck = create_deck("lalal")
# print(deck.directly_holds[0].get_properties())
