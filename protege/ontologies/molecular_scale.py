
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
Ion = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000077")
# An ion is an atomic or molecular particle having a net electric charge. [IUPAC]
    
Anion = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000161")
# An anion (-) is an ion with more electrons than protons, giving it a net negative charge (since electrons are negatively charged and protons are positively charged). [Wikipedia]
    
Cation = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000189")
# A cation (+) is an ion with fewer electrons than protons, giving it a positive charge. [Wikipedia]
    
Nucleus = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000226")
# The positively charged central portion of an atom, excluding the orbital electrons. [IUPAC]
    
Electron = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000418")
# Elementary particle not affected by the strong force having a spin quantum number 1/2, a negative elementary charge and a rest mass of 0.000 548 579 903(13) u. [IUPAC]
    
Proton = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001023")
# A proton is a nuclear particle of charge number +1, spin quantum number of 1/2 and rest mass of 1.00727647012 u. [IUPAC]
    
Neutron = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001027")
# A neutron is a nuclear particle of zero charge, spin quantum number 1/2 and a mass of 1.00866490414 u. [IUPAC]
    
Atom = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001028")
# An atom is a smallest particle still characterizing a chemical element. It consists of a nucleus of a positive charge carrying almost all its mass (more than 99.9%) and Z electrons determining its size. [IUPAC]
    
MolecularEntityQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000252")
# A molecular quality is a chemical quality which inheres in a molecular entity, a single molecule, atom, ion, radical etc. [Allotrope]
    
MolecularMass_molecularQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000256")
# Molecular mass is a molecular quality inhered in a molecular entity that expresses its mass relative to 1/12 of the mass of an unbound neutral atom of carbon-12 in its nuclear and electronic ground state and at rest. [Allotrope]
    
MolecularFormula_molecularQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000263")
# A molecular formula is a molecular quality that inheres in a molecular entity by the relative amount of component atoms. [Allotrope]
    
ElectronEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000264")
# Electron energy is the translational energy that electrons acquire when accelerated in an electric field. [IUPAC]
    
IsotopicDistribution_molecularQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000265")
# Isotopic distribution is a molecular quality inhered in a molecule by the distribution of different isotopes in the molecule. [Allotrope]
    
ChemicalShift_molecularQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000319")
# The fractional variation of the resonance frequency of a nucleus in nuclear magnetic resonance (NMR) spectroscopy in consequence of its magnetic environment. [IUPAC]
    
IonFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001857")
# An ion facet is a molecular facet that is about some ion. [Allotrope]
    
ChargeState = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001859")
# Charge state is a facet that is about the electrical charge of an ion. It is single or multiple and positive or negatively charged. [Allotrope]
    
MolecularEntityFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001951")
# A molecular entity facet is a facet that is about some molecular entity such as atoms, ions or molecules. [Allotrope]
    
MolecularFormula = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001952")
# A molecular formula is a molecular entity facet which identifies each constituent element by its chemical symbol and indicates the number of atoms of each element found in each discrete molecular entity of that compound. [CHEMINF]
    
Water_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_15377")
# An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms. [CHEBI]
    
Dioxygen_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_15379")
# An elemental molecule consisting of two bivalently-bonded oxygen atoms. [Allotrope]
    
Ammonia_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_16134")
# An azane that consists of a single nitrogen atom covelently bonded to three hydrogen atoms. [CHEBI]
    
Methane_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_16183")
# A one-carbon compound in which the carbon is attached by single bonds to four hydrogen atoms. [CHEBI]
    
CarbonDioxide_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_16526")
# A one-carbon compound with formula CO2 in which the carbon is attached to each oxygen atom by a double bond. [CHEBI]
    
CarbonMonoxide_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_17245")
# A one-carbon compound in which the carbon is joined only to a single oxygen. [CHEBI]
    
NitrateIon = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_17632")
# A nitrogen oxoanion formed by loss of a proton from nitric acid. [CHEBI]
    
Dinitrogen_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_17997")
# An elemental molecule consisting of two trivalently-bonded nitrogen atoms. [CHEBI]
    
Ethene_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_18153")
# A compound consisting of two bivalently-bonded carbon atoms, each bonded to two hydrogen atoms. [Allotrope]
    
Dihydrogen_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_18276")
# An elemental molecule consisting of two hydrogens joined by a single bond. [CHEBI]
    
MolecularEntity = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_23367")
# Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical, radical ion, complex, conformer etc., identifiable as a separately distinguishable entity. [IUPAC]
    
Molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_25367")
# A molecule is a polyatomic molecular entity that is an electrically neutral entity consisting of more than one atom. [Allotrope]
    
Ozone_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_25812")
# An elemental molecule with formula O3. [CHEBI]
    
Polyol_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_26191")
# A compound that contains two or more hydroxy groups.. [CHEBI]
    
Acetylene_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_27518")
# A compound consisting of two trivalently-bonded carbon atoms, each bonded to a hydrogen atom. [Allotrope]
    
Photon = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_30212")
# A photon is a particle of zero charge, zero rest mass, spin quantum number 1, energy hν and momentum hν/c (h is the Planck constant, ν the frequency of radiation and c the speed of light), carrier of electromagnetic force. [IUPAC]
    
Nucleon = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_33253")
# A nucleon is either a proton or a neutron. [Wikipedia]
    
Helium_atom = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_33681")
# An atom of the chemical element Helium. [Allotrope]
    
Lepton = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_36338")
# Lepton is a fermion that does not experience the strong force (strong interaction). [CHEBI]
    
Baryon = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_36339")
# Baryon is a fermion that does experience the strong force (strong interaction). [CHEBI]
    
Fermion = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_36340")
# Particle of half-integer spin quantum number following Fermi-Dirac statistics. [CHEBI]
    
Boson = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_36341")
# A boson is a particle that follows Bose–Einstein statistics. [Wikipedia]
    
SubatomicParticle = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_36342")
# A subatomic particle is a material that is below the scale of an atom. [Allotrope]
    
NuclearParticle = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_36347")
# A nuclear particle is a nucleus or any of its constituents in any of their energy states. [CHEBI]
    
Argon_atom = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_49474")
# An atom of the chemical element Argon. [Allotrope]
    
Isocyanate_molecule = onto.search_one(iri="http://purl.obolibrary.org/obo/CHEBI_53212")
# Organonitrogen compounds that are derivatives of isocyanic acid; compounds containing the isocyanate functional group ‒N=C=O (as opposed to the cyanate group, -O-C≡N). [CHEBI]
    
Affinity = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002070")
# Affinity is a molecular quality that arises from the molecular attraction exerted between two atoms or compounds. [PATO]
    
Polarity_molecularQuality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002186")
# Polarity is a  molecular quality that inheres in a molecular entity by virtue of whether or not the molecular entity has a separation of electric charge which leads to the molecule having an electric dipole. [PATO]
    
ElectricCharge_molecularQuality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002193")
# Electric charge is a molecular quality that inheres in a molecular entity by virtue of the overall electric charge of the molecule, which is due to a comparison between the total number of electrons and the total number of protons. [PATO]
    
NeutralCharge = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002194")
# Neutral charge is a quality which inheres in a molecular entity by virtue of the molecular entity possessing the same amount of electrons overall as protons, thus having an overall neutral charge. [PATO]
    
PositiveCharge = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002195")
# Positive charge is a quality which inheres in a molecular entity by virtue of the molecular entity possessing more protons overall than electrons, thus having an overall positive charge. [PATO]
    
NegativeCharge = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002196")
# Negative charge is a quality which inheres in a molecular entity by virtue of the molecular entity possessing more electrons overall than protons, thus having an overall negative charge. [PATO]
    