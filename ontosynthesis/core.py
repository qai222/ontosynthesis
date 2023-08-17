from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

with onto:

    class Hardware(Thing):
        pass

    class Material(Thing):
        pass

    class Compound(Material):
        pass

    class consists_of(ObjectProperty, Material >> Compound):
        pass

    class SolidMaterial(Material):
        pass

    class LiquidMaterial(Material):
        pass

    class Transferor(Hardware):
        pass

    class can_transfer(ObjectProperty, Transferor >> Material):
        pass

    class SolidTransferor(Transferor):
        equivalent_to = [Transferor & can_transfer.some(SolidMaterial)]


    class Container(Hardware):
        pass

    class Vial(Container):
        pass

    class can_contain(ObjectProperty, Container >> Material):
        pass

    class is_made_of(ObjectProperty, Hardware >> Material):
        pass

    class Process(Thing):
        pass

    class is_used_by(ObjectProperty, Hardware >> Process):
        pass

    class is_input_of(ObjectProperty, Material >> Process):
        pass

    class is_output_of(ObjectProperty, Material >> Process):
        pass


v1 = Vial()
v2 = Vial()
glass = Material("GLASS")
v1.is_made_of.append(glass)
if glass not in v1.is_made_of:
    v1.is_made_of.append(glass)
print(v1.get_properties())
print(v1.is_made_of)