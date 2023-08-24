
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
Solution = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000012")
# A solution is a homogeneous mixture composed of one phase where particles  are not visible to the naked eye and the solution does not scatter a light beam. [Allotrope]
    
PortionOfWater = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000105")
# Water is a transparent fluid which forms the world&apos;s streams, lakes, oceans and rain, and is the major constituent of the fluids of living things. [Wikipedia]
    
Suspension = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000442")
# A suspension is a heterogeneous mixture in which the solute particles do not dissolve but get suspended throughout the bulk of the medium. [Wikipedia]
    
Spray = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000494")
# A spray is a heterogeneous mixture where a small amount of liquid is dispersed into a gas. [Allotrope]
    
Emulsion = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001016")
# An is a colloid where the continuous phase is a liquid and the dispersed phase is a liquid. [Allotrope]
    
AssociationColloid = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001030")
# An association colloid is a homogeneous, non-structured substance composed of large molecules or ultramicroscopic suspended in a separate medium, which is largely comprised or reversible aggregations formed by the thermodynamics of molecular interactions. [Allotrope]
    
DispersionColloid = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001031")
# A dispersion colloid is a colloid that is a system in which particles of colloidal size of any nature (e.g. solid, liquid or gas) are dispersed in a continuous phase of a different composition (or state). [IUPAC]
    
Foam = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001032")
# A foam is a colloid where the continuous phase is a liquid and the dispersed phase is a gas. [Allotrope]
    
Gel = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001033")
# A gel is a colloid where the continuous phase is a solid and the dispersed phase is a liquid. [Allotrope]
    
HeterogeneousMixture = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001034")
# A heterogeneous mixture is a portion of mixed material that is not uniform in composition, but proportions of its components vary throughout the sample. [Wikipedia]
    
HomogeneousMixture = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001035")
# A homogeneous mixture is a portion of mixed material that has the same proportions of its components throughout a given sample. Homogeneous mixture can have a variable composition. [Wikipedia]
    
LiquidAerosol = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001036")
# A solid aerosol is an colloid where the continuous phase is a gas and the dispersed phase is a liquid. [Allotrope]
    
MolecularColloid = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001037")
# A molecular colloid is a type of colloid that consists of many molecules that combine to structures of colloidal size. [Allotrope]
    
PortionOfMixedMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001038")
# An portion of mixed material is a material entity that consists of different kinds of grains if you inspect it at a higher level of granularity. [Allotrope]
    
PortionOfPureSubstance = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001039")
# An portion of pure substance is a material entity that consists of one kind of grains if you inspect it at a higher level of granularity. [Allotrope]
    
Sol = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001041")
# A sol is a fluid colloidal system of two or more components. [IUPAC]
    
Colloid = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001044")
# A colloid is a homogeneous mixture in which one substance of microscopically dispersed insoluble particles is suspended throughout another substance. A colloid has a dispersed phase (the suspended particles) and a continuous phase (the medium of suspension). The molecules or polymolecular particles dispersed in a medium have at least in one direction a dimension roughly between 1 nanometer and 1 micrometer, or in a system discontinuities are found at distances of that order. [IUPAC]
    
PortionOfCompound = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001060")
# A portion of material that has grain only the same kind of molecules, ignoring minor impurities. [Allotrope]
    
PortionOfElement = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001061")
# A portion of material that has grain only the same kind of atoms, ignoring minor impurities. [Allotrope]
    
PortionOfBulkStuff = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001064")
# A portion of material that has grain some multi-molecular objects or particles. [Allotrope]
    
GasMixture = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001065")
# A gas mixture is a solution where the continuous phase is a gas and the dispersed phase is a gas. [Allotrope]
    
GasInSolidSolution = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001066")
# A gas in solid solution is a solution where the continuous phase is a solid and the dispersed phase is a gas. [Allotrope]
    
GasInLiquidSolution = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001067")
# A gas in liquid solution is a solution where the continuous phase is a liquid and the dispersed phase is a gas. [Allotrope]
    
LiquidInLiquidSolution = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001068")
# A liquid in liquid solution is a solution where the mixture phase is a liquid and the dispersed phase is a liquid. [Allotrope]
    
SolidInLiquidSolution = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001069")
# A solid in liquid solution is a solution where the continuous phase is a solid and the dispersed phase is a liquid. [Allotrope]
    
LiquidInSolidSolution = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001070")
# A liquid in solid solution is a solution where the continuous phase is a solid and the dispersed phase is a liquid. [Allotrope]
    
SolidInSolidSolution = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001071")
# A solid in solid solution is a solution where the continuous phase is a solid and the dispersed phase is a solid. [Allotrope]
    
SolidAerosol = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001076")
# A solid aerosol is an colloid where the continuous phase is a gas and the dispersed phase is a solid. [Allotrope]
    
SolidFoam = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001077")
# A solid foam is a colloid where the continuous phase is a solid and the dispersed phase is a gas. [Allotrope]
    
SolidSol = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001078")
# A solid sol is a colloid where the continuous phase is a solid and the dispersed phase is a solid. [Allotrope]
    
PortionOfSalt = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001105")
# A portion of salt is a portion of compound where the compound is composed of ions held together by electrostatic forces termed ionic bonding. [Wikipedia]
    
PortionOfSilverNitrate = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001106")
# A portion of silver nitrate is a portion of salt composed of silver (1+) and nitrate ions. [Allotrope]
    
PortionOfMaterial = onto.search_one(iri="http://purl.obolibrary.org/obo/CHMO_0000993")
# An independent material continuant that is self-connected and retains its identity over time. [CHMO]
    