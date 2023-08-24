
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
Reactor = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000153")
# A reactor is a container for controlling a biological or chemical reaction or process. [Allotrope]
    
Vial = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000329")
# A vial is a small vessel or bottle. [Allotrope]
    
TemperatureControlledChamber = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000350")
# A temperature controlled chamber is a chamber or enclosed space in which a temperature can be controlled and set to a specific value. [Allotrope]
    
Reservoir = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000378")
# The reservoir is a container that stores solutions. [Allotrope]
    
OpticalSpectrometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000466")
# A piece of apparatus used to measure a spectrum by illumination with light. [Allotrope]
    
Spectrometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000857")
# A piece of apparatus used to measure a spectrum. [CHMO]
    
ControlledLabReactor = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001519")
# A controlled lab reactor is a reactor that maintains temperature and other reaction parameters and has measuring devices. [Allotrope]
    
OpticalDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001745")
# An optical device is a device that creates, manipulates, or measures electromagnetic radiation. [Wikipedia]
    
SeparationColumn = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002165")
# A separation column is a separation device of columnar shape where the separation occurs inside the column. [Allotrope]
    
Probe = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002248")
# A probe is a device designed to reach into a location for remote manipulating or sensing. [NCI]
    
SampleMeasurementInterface = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002253")
# A sample measurement interface is a connecting device through which measurements are captured. [Allotrope]
    
DissolutionVessel = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002272")
# A dissolution vessel is a container used in a dissolution. [Allotrope]
    
VialContainer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002278")
# A vial container is a container that has the function to contain vials. [Allotrope]
    
ToSeparateMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000031")
# A material separation function is a function that increases the resolution between two or more material entities. The  to distinction between the entities is usually based on some associated physical quality. [OBI]
    
ToFilterMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000049")
# A filter function is a function to prevent the flow of certain entities based on a quality or qualities of the entity while allowing entities which have different qualities to pass through. [OBI]
    
MaterialFunction = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000076")
# A material function is a type of function that is realized in a process that has material entity as input and/or output. [Allotrope]
    
ToRemoveMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000144")
# To remove material is the function to remove material. [NIST]
    
Dye = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000085")
# A dye is a material that has the function to change the color of material. [Allotrope]
    
Gas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000154")
# A gas is an airlike material that expands freely to fill any space available. It can be transported in compressed gas cylinders and acts as a gas upon release at normal temperatures and pressure. [Allotrope]
    
Solid = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000386")
# A solid is a substance that is in the solid material state. [Allotrope]
    
Fluid = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000394")
# A fluid is a substance that continually deforms (flows) under an applied shear stress. Fluids are a subset of the phases of matter and include liquids, gases, plasmas and, to some extent, plastic solids. [Wikipedia]
    
SupercriticalFluid = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000401")
# A supercritical fluid is a gas whose temperature and pressure are above the critical temperature and critical pressure. In this state, the distinction between liquid and gas disappears. [Wikipedia]
    
Liquid = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000403")
# A liquid is a nearly incompressible fluid that conforms to the shape of its container but retains a (nearly) constant volume independent of pressure. [Wikipedia]
    
Plasma = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000404")
# Plasma is a state of matter in which an ionized gaseous substance becomes highly electrically conductive to the point that long-range electric and magnetic fields dominate the behavior of the matter. [Wikipedia]
    
Particle_physics = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000435")
# A particle in the physical sciences is a small localized object to which can be ascribed physical properties. [Wikipedia]
    
SolidHeterogeneousMixture = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001042")
# A solid heterogeneous mixture is a heterogeneous mixture in solid state. [Allotrope]
    
Dispersion = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001079")
# A dispersions is a heterogeneous mixture that is comprising more than one phase where at least one of the phases consists of finely divided phase domains, often in the colloidal size range, dispersed throughout a continuous phase. [IUPAC]
    
OrganizationalEntity = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001090")
# An organizational entity is a person, group or organization that is defined by some social contract between humans. [Allotrope]
    
ChemicalSubstance = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001097")
# A chemical substance is a portion of material that is matter of constant composition best characterized by the entities (molecules, formula units, atoms) it is composed of. [IUPAC]
    
ChemicalMixture = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001099")
# A portion of chemical mixture is a chemical substance that is composed of chemical substances. [Allotrope]
    
HydrogenGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001112")
# Hydrogen gas is a gas that is composed of hydrogen molecules. [Allotrope]
    
OxygenGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001113")
# Oxygen gas is a gas that is composed of dioxygen molecules. [Allotrope]
    
NitrogenGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001114")
# Nitrogen gas is a gas that is composed of dinitrogen molecules. [Allotrope]
    
HeliumGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001115")
# Helium gas is a gas that is composed of helium atoms. [Allotrope]
    
CarbonDioxideGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001116")
# Carbon dioxide gas is a gas that is composed of carbon dioxide molecules. [Allotrope]
    
AmmoniaGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001117")
# Ammonia gas is a gas that is composed of ammonia molecules. [Allotrope]
    
MethaneGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001118")
# Methane gas is a gas that is composed of methane molecules. [Allotrope]
    
MaterialFlow = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001122")
# A material flow is a material that is an aggregate of granular objects that steadily and continuously move along a path. [Allotrope]
    
IonFlow = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001123")
# A ion flow is a material flow where ions transport electric charges in an electromagnetic field. [Allotrope]
    
Bubble = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001125")
# A bubble is a small round portion of one substance in another, usually gas in a liquid. [Wikipedia]
    
OzoneGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001126")
# Ozone gas is a gas that is composed of ozone molecules. [Allotrope]
    
EtheneGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001127")
# Ethene gas is a gas that is composed of ethene molecules. [Allotrope]
    
AcetyleneGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001128")
# Acetylene gas is a gas that is composed of acetylene molecules. [Allotrope]
    
CarbonMonoxideGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001129")
# Carbon monoxide gas is a gas that is composed of carbon monoxide molecules. [Allotrope]
    
ArgonGas = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001130")
# Argon gas is a gas that is composed of argon atoms. [Allotrope]
    
LiquidNitrogen = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001131")
# Liquid nitrogen is a liquid that is composed of dinitrogen molecules. [Allotrope]
    
InformationProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000307")
# A process that affects, creates or destroys information content. [Allotrope]
    
NuclearMagneticResonanceAssay = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000759")
# A nuclear magnetic resonance assay is magnetic resonance assay that applies a technique which detects the response of nuclear spins to a perturbing magnetic field. [Allotrope]
    
SpectraCombination = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000801")
# Spectra combination is a data transformation that combines multiple spectra. [Allotrope]
    
Scanning = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001146")
# Scanning is measuring repeatedly or sweepingly. [Allotrope]
    
SamplePreparation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001159")
# Sample preparation is a planned preparation process that synthesizes, converts or changes a sample. [Allotrope]
    
MagneticResonanceAssay = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002211")
# A magnetic resonance assay is an assay that applies a technique which detects the response of spins to a perturbing magnetic field. [Allotrope]
    
SignalAveraging = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002662")
# Signal averaging is a process of combining spectra of repeated measurements in order to improve the signal-to-noise ratio. [Allotrope]
    
BackgroundMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002666")
# Background measurement is the process of determination of the base level of signals without presence of a sample. [Allotrope]
    
PressureMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002677")
# A measurement that targets the pressure of some material entity. [Allotrope]
    
PressureControl = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002832")
# A pressure control is a controlling process that controls pressure of some material. [Allotrope]
    
TemperatureControl = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002833")
# A temperature control is a controlling process that controls the temperature of some material. [Allotrope]
    
MaterialProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003275")
# A process that affects the physical qualities of materials or creates, destroys or converts materials. [Allotrope]
    
PressureProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003294")
# A pressure process profile is a quality process profile that tracks some pressure. [Allotrope]
    
TemperatureProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003300")
# Temperature profile is a quality process profile that tracks temperature. [Allotrope]
    
TransmittingEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003313")
# Transmitting energy is transferring an energy from one place to another. [Allotrope, NIST]
    
EnergeticProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003321")
# A process where an agent affects energy flowing in and out of a system or affecting the energetic state of materials. [Allotrope]
    
StoringMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003323")
# Storing material is the storing of material. [Allotrope]
    
StoringEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003324")
# Storing energy is the storing of energy. [Allotrope]
    
ChangingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003362")
# Changing is controlling a quality of the material in a predetermined and fixed manner. The identity of the material is maintained. [NIST]
    
InsertingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003398")
# A spatial processing of transferring material into a site. [Allotrope]
    
MentalProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003452")
# A physical process that occurs in the mind of a sentient being and is processing information. [Allotrope]
    
ChangingEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003467")
# Changing is controlling a quality of energy in a predetermined and fixed manner. [NIST]
    
TransportingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003469")
# Transporting is channeling by shifting, or conveying, a material from one place to another. [NIST]
    
SeparatingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003533")
# A separating of materials. [Allotrope]
    
RemovingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003574")
# A spatial process of removing a material from a site. [Allotrope]
    
DeliveringMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003575")
# Delivering material is the importing of material to a location or site. [Allotrope]
    
SequentialProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003691")
# A sequential process is a composite process that has sequential subprocesses as occurrent parts. The starts of all subprocesses occur in sequential order. The ends of all subprocesses occur at the end of the sequential process at the latest. [Allotrope]
    
SequentialAnalysisProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003692")
# A sequential analysis process is a planned sequential process that has analytical subprocesses as sequential occurrent parts. [Allotrope]
    
Adjusting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003703")
# Adjusting is a process of slightly changing something with the purpose to achieve an agreement with a set of specifications. [Allotrope]
    
StandardPreparation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003704")
# A sample preparation process is a planned process that prepares a portion of material for being used in a calibration standard role. [Allotrope]
    
ChemicalReaction_molecular = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003711")
# A chemical reaction is a process that results in the interconversion of chemical species. [IUPAC]
    
IonReaction = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003712")
# An ion reaction is a chemical reaction that has ion participants. [Allotrope]
    
CombiningMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003716")
# Combining material is a combing process that combines two or more materials in to a new material. [Allotrope]
    
DeviceProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003726")
# A device process is a planned process that realizes a function by a device or device system. [Allotrope]
    
RepeatedProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003727")
# A repeated process is a composite process that has occurrent parts of subprocesses following the same plan. [Allotrope]
    
Reporting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003729")
# Reporting is an information process that produces a report. [Allotrope]
    
Project = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003730")
# A project is a planned process that is undertaken or attempted to meet some requirement. [Allotrope]
    
ThermalEvent = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003736")
# A thermal event is an event where a significant change of some material quality occurs at a temperature of that material or that of its environment. [Allotrope]
    
Event = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003737")
# An event is an occurrent that is an accomplishment or an achievement. [Allotrope]
    
AdditionRateProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003741")
# An addition rate process profile is a rate process profile that is an occurrent part of an material addition process. [Allotrope]
    
VolumeProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003742")
# A volume process profile is a quality process profile that tracks some volume. [Allotrope]
    
Adding_material = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003743")
# Adding is loading material into a container where it is combined with existing material. [Allotrope]
    
MaterialFlowRateProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003744")
# A material flow rate process profile is a rate process profile that is the change of amount of material being transferred through an area. [Allotrope]
    
HeatTransferCoefficientProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003751")
# A heat transfer coefficient process profile is a rate process profile of the ratio of the heat flux and the thermodynamic driving force for the flow of heat. [Allotrope]
    
AngularVelocityProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003752")
# An angular velocity process profile is a quality process profile of how fast an object rotates or revolves relative to another point. [Wikipedia]
    
AreaProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003753")
# A volume process profile is a quality process profile that tracks some area. [Allotrope]
    
HeatingOrCoolingRateProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003755")
# A heating or cooling rate process profile is a rate process profile of the heating/cooling rate of an object. [Allotrope]
    
Hygroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003764")
# Hygroscopy is the phenomenon of attracting and holding water molecules via either absorption or adsorption from the surrounding environment. [Wikipedia]
    
HeatFlowProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003795")
# A heat flow process profile is a rate process profile that is the change in heat flow through a material entity. [Allotrope]
    
MassProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003796")
# A mass process profile is a quality process profile that tracks some mass. [Allotrope]
    
ConcentrationProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003797")
# A concentration process profile is a quality process profile that tracks some concentration. [Allotrope]
    
PhProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003798")
# A pH process profile is a quality process profile that tracks some pH. [Allotrope]
    
ConfigurationProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003801")
# A configuration process profile is a quality process profile that tracks the configuration of a system or device. [Allotrope]
    
LuminescenceProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003803")
# A luminescence process profile is a profile that quantifies the luminescence of a material entity over time. [Allotrope]
    
AreaScanning = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003804")
# Area scanning is scanning at positions defined by a two-dimensional pattern over an area. [Allotrope]
    
Read = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003805")
# A read is a process boundary within a measuring where a data about the measured object is captured. [Allotrope]
    
PolarityControl = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003810")
# Polarity control is a changing process that changes the polarity of some material. [Allotrope]
    
SampleIntroduction = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003813")
# A sample introduction is a loading of some sample into a system. [Allotrope]
    
CarryingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003815")
# Carrying is a state where a material entity, the carrier, supports the state of moving or keeping in place of another material or information. [Allotrope]
    
ChangingQualityState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003816")
# A changing quality state is a state where a material&apos;s quality is changing continuously. [Allotrope]
    
ConstantQualityState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003817")
# A constant quality state is a quality state where the quality does not change. [Allotrope]
    
ConstantQualityProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003818")
# A constant quality process profile is a quality process profile where the tracked  quality does not change. [Allotrope]
    
IncreasingQualityProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003819")
# An increasing quality process profile is a quality process profile where the tracked determinate quality is continuously increasing in magnitude. [Allotrope]
    
DecreasingQualityProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003820")
# An decreasing quality process profile is a quality process profile where the tracked determinate quality is continuously decreasing in magnitude. [Allotrope]
    
ChangingQualityProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003821")
# A changing quality process profile is a quality process profile where the tracked quality changes over time. [Allotrope]
    
ProperChangingQualityProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003822")
# A proper changing quality process profile is a changing process profile where the tracked quality at the start of the process is different from the tracked quality at the end of the process. [Allotrope]
    
Abrading = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003830")
# Abrading is a material process of scuffing, scratching, wearing down, marring, or rubbing away. [Wikipedia]
    
ParticleSize_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000026")
# Quality of an independent continuant which describes the dimensions of an individual particle. [Allotrope]
    
ParticleSizeAboveOneMicrometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000121")
# A particle size above one micrometer is a determinate quality of particle size that has a determinate magnitude of greater that one micrometer. Magnitude of particle size can be measured in different ways such as based on diameter of spherical objects. [Allotrope]
    
TemperatureConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000203")
# A temperature configuration is a device configuration of a temperature controlling or monitoring device, that controls or monitors the target temperature at the site of some system component. [Allotrope]
    
FlowRateConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000239")
# A flow rate configuration is a device configuration of a fluid controlling or monitoring device, that controls or monitors the flow rate at the site of some system component. [Allotrope]
    
ConcentrationRatioConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000240")
# A concentration ratio configuration is a device configuration of a fluid controlling or monitoring device, that controls or monitors the concentration ratio of a mixture at the site of some system component. [Allotrope]
    
VolumeConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000241")
# A volume configuration is a device configuration of a controlling or monitoring device, that controls or monitors the volume of some material at the site of some system component. [Allotrope]
    
PolarityConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000243")
# Polarity configuration is a device configuration that sets a specific detector or sensor response to be positive or negative to a reference state. [Allotrope]
    
CellPathLength_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000268")
# The cell path length is the length of the radiation path through the absorbing medium in a single-pass cell. [IUPAC]
    
EvacuationRate_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000276")
# An evacuation rate is a flow rate indicating the rate at which gas is removed from a chamber. [Allotrope]
    
MeasurementChamberFreeSpaceVolume_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000277")
# A measurement chamber free space volume (quality) is the volume within a sample measurement chamber that is not occupied by the sample. [Allotrope]
    
ParticleShape_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000311")
# A particle shape is a shape quality of a particle. [Allotrope]
    
ChordLength_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000313")
# A chord length is the length between any two points on the edge of a particle, with an upper bound of the diameter of the particle. [Allotrope]
    
CurrentConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000314")
# A current configuration is a device configuration of a current controlling or monitoring device, that controls or monitors the target electric current at the site of some system component. [Allotrope]
    
VoltageConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000315")
# A voltage configuration is a device configuration of a voltage controlling or monitoring device, that controls or monitors the target voltage at the site of some system component. [Allotrope]
    
PressureConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000337")
# A pressure configuration is a device configuration of a pressure controlling or monitoring device, that controls or monitors the target pressure at the site of some system component. [Allotrope]
    
IonCurrent_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000338")
# An ion current is a summary quality of an ion flow by virtue of the electrical charge of the ions. [Allotrope]
    
SamplingOrientation = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000343")
# Sampling orientation is a system configuration of a separation device that is the direction of separation relative to the movement of the sampled material in the device. [Allotrope]
    
VelocityConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000351")
# A velocity configuration is a device configuration of a controlling or monitoring device, that controls or monitors the velocity of some process at the site of some system component. [Allotrope]
    
DistanceConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000352")
# A distance configuration is a device configuration of a controlling or monitoring device, that controls or monitors the distance between of some materials at the site of some system component. [Allotrope]
    
PeakAssignmentTarget = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000024")
# The description of a chemical moiety or material that is assigned to a peak. [Allotrope]
    
WeighingResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000062")
# The weighing result is the result of a weighing process. [Allotrope]
    
Spectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000068")
# A spectrum is a data distribution function of a measured quantity in a spectroscopy against some experimental parameter. [Allotrope]
    
TemperatureMeasurementResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000120")
# A temperature measurement result is an assay result that is the output of a temperature measurement. [Allotrope]
    
AssayResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000207")
# The final outcome reported for a measured or computed quantity, after performing a measuring procedure including all sub procedures and evaluations. [IUPAC, Allotrope]
    
AbsorptionSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000222")
# An absorption spectrum is a data distribution function that plots the absorption of radiance as the function of frequency or wavelength. [Wikipedia]
    
TitrationResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000504")
# A titration result is the result of a titration. [Allotrope]
    
ChromatographyResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000523")
# A chromatography result is a result of a chromatography run. [Allotrope]
    
CapillaryElectrophoresisResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000525")
# The capillary electrophoresis result is the result of a process of capillary electrophoresis. [Allotrope]
    
Profile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000576")
# A profile is a data distribution function that is a function of time. [Allotrope]
    
MicroplateReaderMeasurementResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000628")
# The readout from a microplate reader measurement. [Allotrope]
    
Trend = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000634")
# A trend is the result of a process of trending. [Allotrope]
    
File = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000639")
# A file is a resource for storing information, which is available to a computer program and is usually based on some kind of durable storage. [Wikipedia]
    
Fingerprint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000700")
# A fingerprint is a type of or portion of spectrum that has a characteristic structure.  It can be used as a fingerprint for comparison to reference spectra. [Allotrope]
    
Distribution = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000733")
# A distribution is a collection of frequencies of results of a sample. Each frequency is number of occurrences within a given interval. The distribution can be expressed relatively to the width of the interval. [Allotrope]
    
ParticleSizingResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000745")
# A particle sizing result is the outcome of a process of particle sizing. [Allotrope]
    
SpectroscopyResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000754")
# Result of a spectroscopical measurement. [Allotrope]
    
OverlayOfScans = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000774")
# An overlay of scans is a graphic overlay of generated spectra for comparison. [Allotrope]
    
MethodFunctionSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000974")
# A function specification that specifies the ways of achievement. [Allotrope]
    
Count = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000984")
# A datum that has non-negative integer values that is about the number of discrete things. [Allotrope]
    
Analyst = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001116")
# Analyst is measurement metadata about the name or identifier of a person that has the role of an analyst in the measurement. [Allotrope]
    
SampleIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001118")
# Sample id is a measurement metadata that identifies a sample being measured. [Allotrope]
    
EquipmentSerialNumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001119")
# Equipment serial number is a serial number that identifies an equipment used in the measuring by its serial number. [Allotrope]
    
BatchIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001120")
# A batch identifier is an identifier that identifies a batch. [Allotrope]
    
MeasurementIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001121")
# Measurement id is measurement metadata that identifies the measuring run. [Allotrope]
    
SamplingSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001124")
# A sampling specification is an action specification of the way a sampling is done. [Allotrope]
    
PeakIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001164")
# A peak identifier is an identifier that identifies a peak. [Allotrope]
    
PeakMaximumPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001191")
# The peak maximum point is the data point of the peak with the largest ordinate value. [Allotrope]
    
TemperatureSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001255")
# A temperature setting is a setting that specifies some temperature configuration of a temperature controlling or monitoring device, that controls or monitors the target temperature at the site of some system component. [Allotrope]
    
ClassDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001278")
# A type datum is a classification datum that classifies a thing as an instance of an RDFS class. [Allotrope]
    
ConceptDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001279")
# A concept datum is a classification datum that classifies a thing by a SKOS concept. [Allotrope]
    
CodeClassificationDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001280")
# A classification datum that classifies things by a code in a codelist. [Allotrope]
    
RoleClassDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001509")
# A role class datum is a classification datum that classifies an entity by the role or contextual role class it plays in the context of the classification datum. [Allotrope]
    
SettingSnapshot = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001526")
# A setting snapshot is a setting for a specific point in time. [Allotrope]
    
DeviceMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001556")
# A device method is a plan specification that specifies how some process is to be executed on a device. [Allotrope]
    
AnalysisAssayResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001602")
# The analysis assay result is the assay result of an analysis assay. [Allotrope]
    
AnalysisAssayResultFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001603")
# An analysis assay result facet is a facet of an analysis assay result. [Allotrope]
    
VolumeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001658")
# A volume setting is a setting that specifies some volume configuration of a controlling or monitoring device, that controls or monitors the volume of some material at the site of some system component. [Allotrope]
    
ConcentrationRatioSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001659")
# A concentration ratio setting is a setting that specifies some concentration ratio configuration of a fluid controlling or monitoring device, that controls or monitors the concentration ratio of a mixture at the site of some system component. [Allotrope]
    
FlowRateSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001660")
# A flow rate setting is a setting that specifies some flow rate configuration of a fluid controlling or monitoring device, that controls or monitors the flow rate at the site of some system component. [Allotrope]
    
IntegrationTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001671")
# The integration time is the time when the integration of signals is done in a measurement system. [Allotrope]
    
NumberOfAverages = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001672")
# The number of averages is the number of individual values taken for calculating a mean value. [Allotrope]
    
NumberOfMeasurementAverages = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001673")
# The number of measurement averages is the number of averages of sub measurement results taken to produce an average measurement result. [Allotrope]
    
RepetitionSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001678")
# A repetition setting is a control setting that specifies the number of times an action is to be repeated. [Allotrope]
    
Flag_setting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001685")
# A flag is a setting that allows switching a configuration on or off. [Allotrope]
    
DataProcessingSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001696")
# A data processing setting is a setting that controls how a data processing process is executed by some system. [Allotrope]
    
MaterialIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001745")
# A material identifier is a identifier that identifies a material. [Allotrope]
    
DurationSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001815")
# A duration setting is a setting that specifies the duration of a planned process or the duration after which a situation should trigger. [Allotrope]
    
VolumeFraction = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001845")
# A volume fraction datum is a quality quantification facet that quantifies the volume of a constituent of a mixture divided by the sum of volumes of all constituents prior to mixing. [IUPAC]
    
MeasurementFunction = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001847")
# A measurement function is a mathematical function of quantities yielding for one or more input quantity value a corresponding unique output quantity value. [Allotrope]
    
UncPath = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001906")
# An UNC path is a file path for a file location in a network that is specified by the universal naming convention. [Allotrope]
    
MaximumOperatingTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001919")
# An upper temperature limit is a temperature alert setting that specifies the maximum temperature the system can operate with. [Allotrope]
    
MinimumOperatingTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001920")
# A lower temperature limit is a temperature alert setting that specifies the minimum temperature the system can operate with. [Allotrope]
    
FlowRatioSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001922")
# The flow ratio setting is a control setting that specifies the ratio of the flow going though the plumbing part (port of a divert valve, solvent channel) as part of a total flow. [Allotrope]
    
FlowRatio = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001923")
# Flow rate is a quality quantification facet that quantifies the ratio of the flow going though the plumbing part (port of a divert valve, solvent channel) as part of a total flow. [Allotrope]
    
FilePath = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001927")
# A file path is an identifier for a file in a file system or network. [Allotrope]
    
PosixPath = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001928")
# A POSIX path is a file path for a file location that is specified by the POSIX standard. [Allotrope]
    
DryingTemperatureSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001930")
# A drying temperature setting is a temperature setting that specifies the intended temperature of a drying process. [Allotrope]
    
PolaritySetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001967")
# Polarity setting is a control setting that specifies a polarity configuration of a specific detector or sensor response to be positive or negative to a reference state. [Allotrope]
    
RepeatedActionSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001972")
# An repeated action specification is an action specification that specifies a repeated activity. [Allotrope]
    
LaboratoryInformationManagementSoftware = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001974")
# A laboratory information management software is a software that is used for data management in laboratories. [Allotrope]
    
AssetManagementIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001976")
# An asset management identifier is an identifier that is registered within an asset / inventory management system that identifies an equipment. [Allotrope]
    
ExperimentalDataIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001977")
# An experiment data identifier is an identifier that identifies some experiment data. [Allotrope]
    
AnalyticalMethodIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001978")
# An analytical method identifier is an identifier that identifies the analytical method used in a measurement. [Allotrope]
    
AssayIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001979")
# An assay identifier is an identifier that identifies some assay (analysis). [Allotrope]
    
AssayComment = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001980")
# An assay comment is a comment about some aspect of an assay. [Allotrope]
    
SampleWeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001982")
# Sample weight is a quantification facet that quantifies the mass of a sample in an analysis. [Allotrope]
    
BalanceIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001986")
# A balance identifier is a measurement device identifier that identifies some balance. [Allotrope]
    
ContainerType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001987")
# Container type is a classification datum that classifies the type of container used. [Allotrope]
    
ReferenceIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001992")
# A reference identifier is an identifier that identifies some reference data that is being used as a comparator. [Allotrope]
    
ContainerStateDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001993")
# Container state description is a state facet that describes the state of the container used in the measurement run. [Allotrope]
    
CellPathLength = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001997")
# A cell path length is a quality quantification facet that quantifies the length of the radiation path through the absorbing medium in a single-pass cell. [Allotrope]
    
MeasurementDeviceIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002002")
# A measurement device identifier is an identifier that identifies some device designed for measurements. [Allotrope]
    
MeasurementMethodIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002003")
# A measurement method identifier is a method identifier that identifies some plan specification of a measurement. [Allotrope]
    
Reference = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002008")
# A reference is an information content entity that is referred to in another information content entity for the purpose of comparison. [Allotrope]
    
ExperimentIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002009")
# An experiment identifier is an identifier that identifies an experiment. [Allotrope]
    
ExperimentalData = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002010")
# Experiment data is a description of an experiment containing parameters and results of the experiment and metadata about the experiment. [Allotrope]
    
ExperimentResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002011")
# An experiment result is description, that is the data output of an experiment regarding its hypothesis. [Allotrope]
    
DeviceMethodIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002016")
# A device method identifier is an identifier that identifies the device method used in a process. [Allotrope]
    
DeviceIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002018")
# A device identifier is an identifier that identifies some device. [Allotrope]
    
AssayDataIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002019")
# An assay data identifier is an identifier that identifies some assay data. Assay data is a description of an assay containing parameters and results of the assay and metadata about the assay. [Allotrope]
    
AssayData = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002020")
# Assay data is a description of an assay containing parameters and results of the assay and metadata about the assay. [Allotrope]
    
TemporalIndex = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002033")
# A temporal index is an index that follows temporal order of the list items or the processes that the items are about. [Allotrope]
    
MethodIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002034")
# A method identifier is an identifier that identifies some plan specification (method, procedure) about some planned process. [Allotrope]
    
MeasurementMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002035")
# A measurement method is a plan specification that specifies a measurement. [Allotrope]
    
ExpiryTimePrescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002037")
# The expiry time prescription is a prescription about a material or information content entity that prescribes until what time it is allowed to be used for the stated purpose. [Allotrope]
    
ElectronicRecord = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002038")
# Electronic record is a document (any combination of text, graphics, data, audio, pictorial, or other information representation) in digital form that is created, modified, maintained, archived, retrieved, or distributed by a computer system. [FDA]
    
DatabaseRecord = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002039")
# A database record is an electronic record that is stored in a database. [Allotrope]
    
Database = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002040")
# A database is an organized collection of data, generally stored and accessed electronically from a computer system. Where databases are more complex they are often developed using formal design and modeling techniques. [Wikipedia]
    
DatabasePrimaryKey = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002041")
# A database primary key is an identifier of a database record. [Allotrope]
    
DeviceAcquisitionMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002045")
# A device acquisition method is a machine readable plan specification that specifies how the acquisition software of an instrument is to execute the instrument&apos;s portion of an analysis. [Allotrope]
    
FlowRateProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002051")
# A flow rate profile is a profile that quantifies the flow rate of a material entity over time. [Allotrope]
    
VolumeProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002052")
# A volume profile is a profile that quantifies the volume of a material entity over time. [Allotrope]
    
TemperatureProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002056")
# A temperature profile is a profile that quantifies the temperature of a material entity over time. [Allotrope]
    
DataCubeIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002059")
# A data cube identifier is an identifier for a data cube. A data cube is a multi-dimensional dataset conforming to the W3C DataCube specification (https://www.w3.org/TR/vocab-data-cube/). [Allotrope]
    
HeatTransferCoefficientProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002073")
# A heat transfer coefficient profile is a profile that quantifies over time the proportionality constant between the heat flux and the thermodynamic driving force for the flow of heat. [Wikipedia]
    
AngularVelocityProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002075")
# An angular velocity profile is a profile that quantifies over time how fast an object rotates or revolves relative to another point. [Wikipedia]
    
AreaProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002077")
# An area profile is a profile that quantifies over time the area of an object. [Allotrope]
    
SpecificHeatCapacity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002079")
# A specific heat capacity (datum) is a quality quantification facet that quantifies the amount of heat necessary to raise the temperature of one gram of a pure substance by one degree K. [Wikipedia]
    
HeatingOrCoolingRateProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002081")
# A heating or cooling rate profile is a profile that quantifies the heating/cooling rate of an object over time. [Allotrope]
    
SampleAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002082")
# A sample aggregate document is a document that is about an ordered collection of samples. [Allotrope]
    
SampleDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002083")
# A sample document is a document about a particular sample. [Allotrope]
    
RamanSpectroscopyResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002104")
# A Raman spectroscopy result is the result of a Raman spectroscopy. [Allotrope]
    
InfraredSpectroscopyResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002105")
# An infrared spectroscopy result is the result of an infrared absorption or transmission spectroscopy. [Allotrope]
    
DegassedSampleWeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002112")
# A degassed sample weight is the sample weight of a sample after it has gone through a degassing process. [Allotrope]
    
ReferenceMaterialDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002113")
# A reference material document is a document that encompasses the information associated with the reference material in an analysis. [Allotrope]
    
ReferenceMaterialIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002114")
# A reference material is an identifier that identifies some material with the role of reference material. [Allotrope]
    
MeasurementEndTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002124")
# A measurement end time is the date/time of the end of the measurement process. [Allotrope]
    
EvacuationRateSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002125")
# An evacuation rate setting is a control setting that controls the evacuation rate. [Allotrope]
    
EvacuationTimeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002126")
# An evacuation time setting is a control setting that controls the time when a chamber is to be evacuated. [Allotrope]
    
MeasurementChamberFreeSpaceVolume = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002127")
# A measurement chamber free space result is a quality quantification facet that quantifies the volume of a sample chamber not occupied by the sample. [Allotrope]
    
CumulativeCount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002132")
# A cumulative count (datum) is a count that has non-negative integer values that is about the cumulative number of discrete things. [Allotrope]
    
CalculationDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002141")
# A calculation description is a description that describes how a calculation was done. [Allotrope]
    
SampleTemperatureSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002148")
# A sample temperature setting is a temperature control setting to set the target temperature of the sample. [Allotrope]
    
SolventReservoirTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002160")
# A solvent reservoir temperature is a quantity facet that quantifies the temperature of the solvent reservoir. [Allotrope]
    
DataProcessingMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002175")
# A data processing method is a plan specification that specifies how data processing process is to be executed. [Allotrope]
    
SolventIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002177")
# A solvent identifier is an identifier denoting the solvent used in the experiment. [Allotrope]
    
DistributionDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002193")
# A distribution document is a document that encompasses the information associated with a distribution. [Allotrope]
    
CountFraction = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002197")
# The count fraction (datum) is a quality quantification facet that quantifies the fraction pertaining the number of object of a constituent divided by the total number of objects of all constituents in the object aggregate. [Allotrope]
    
SamplePreparationDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002202")
# A sample preparation description is a description of the sample preparation process. [Allotrope]
    
Deviation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002204")
# A deviation is a quantification facet that quantifies the absolute or relative difference of an observed value from another value. [Allotrope]
    
ArithmeticMean = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002208")
# The arithmetic mean is a descriptive statistic that is the sum of a collection of numbers divided by the number of numbers in the collection. [Wikipedia]
    
Median = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002209")
# The median is a descriptive statistic that denotes the value separating the higher half of a data sample, a population, or a probability distribution, from the lower half. [Wikipedia]
    
Variance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002210")
# The variance is a descriptive statistic that denotes the expectation of the squared deviation of a random variable from its mean. [Wikipedia]
    
Skewness = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002211")
# Skewness is a descriptive statistic that is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. The skewness value can be positive or negative, or undefined. [Wikipedia]
    
ImageDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002225")
# An image document is a document that encompasses the information associated with an image. [Allotrope]
    
MagnificationSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002226")
# A magnification setting is a setting that specifies the multiplicative optical apparent size manipulation being applied by an imaging device. [Allotrope]
    
StandardDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002228")
# A standard document is a document about a particular standard. [Allotrope]
    
ExperimentType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002229")
# An experiment type is a classification datum that classifies the type of experiment performed. [Allotrope]
    
AutomaticBaselineDeterminationEnabledSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002237")
# An automatic baseline determination enabled setting is an automation flag that controls whether baseline determination is automated or manual. [Allotrope]
    
WellLocationIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002240")
# A well location identifier is a local identifier that identifies the location of a well on the container in the scope of the container. [Allotrope]
    
SampleRoleType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002242")
# A sample role type is a classification datum that classifies samples by the type of  sample role in the experiment. [Allotrope]
    
NuclearMagneticResonanceResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002249")
# An nuclear magnetic resonance result is a result of an nuclear magnetic resonance assay. [Allotrope]
    
SlitWidthSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002252")
# A slit width setting is a setting that specifies the width of the opening of the slit. [Allotrope]
    
DetectorType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002253")
# A detector type is a classification datum that describes the detector type. [Allotrope]
    
BeamsplitterType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002254")
# A beamsplitter type is a classification datum that describes the beamsplitter type based on the compound used to split the light beam. [Allotrope]
    
NuclearMagneticResonanceSpectroscopyResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002255")
# An NMR spectroscopy result is a result of an NMR spectroscopy. [Allotrope]
    
MassSpectrometryResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002256")
# A mass spectrometry result is a result of a mass spectrometry. [Allotrope]
    
ReflectanceSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002281")
# A reflectance spectrum is a spectrum that plots the reflectance of radiance as the function of frequency or wavelength. [Allotrope]
    
ReflectanceSpectrumDataCube = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002282")
# A reflectance spectrum data cube is a data cube that represents a reflectance spectrum. [Allotrope]
    
AbsorptionSpectrumDataCube = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002283")
# An absorption spectrum data cube is a data cube that represents an absorption spectrum. [Allotrope]
    
TransmittanceSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002284")
# A transmittance spectrum is a spectrum that plots the transmittance of radiance as the function of frequency or wavelength. [Allotrope]
    
TransmittanceSpectrumDataCube = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002285")
# A transmittance spectrum data cube is a data cube that represents a transmittance spectrum. [Allotrope]
    
TimeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002288")
# A time setting is a setting the specifies a point in time when a process starts or ends. [Allotrope]
    
ReactionComponentList = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002290")
# A reaction component list is a document about an ordered collection of material entities with roles in a chemical reaction. [Allotrope]
    
ChemicalDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002291")
# A chemical document is a document that is about some chemical substance. [Allotrope]
    
ChemicalName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002292")
# A chemical name is the written name of a chemical substance that shows the names of each of its elements or subcompounds. [Allotrope]
    
ReactionComponentRoleType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002293")
# A reaction component role type is a classification datum that classifies the role of a chemical substance in a reaction. [Allotrope]
    
SmilesMolecularStructure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002295")
# A SMILES molecular structure is a molecular structure specified in Simplified Molecular Input Line Entry System (SMILES) line notation. [edamontology.org]
    
InchiMolecularStructure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002296")
# An InChI molecular structure is a molecular structure specified in IUPAC International Chemical Identifier (InChI) line notation. [edamontology.org]
    
InchikeyMolecularStructure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002297")
# An InChIKey molecular structure is a molecular structure specified as an InChIKey (hashed InChI), which is a fixed length (25 character) condensed digital representation of an InChI chemical structure specification. It uniquely identifies a chemical compound. An InChIKey identifier is not human- nor machine-readable but is more suitable for web searches than an InChI chemical structure specification. [edamontology.org]
    
AdditionDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002298")
# An addition description is a description about the process of adding a reaction component to a reaction. [Allotrope]
    
ProbeType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002299")
# A probe type is a classification datum that describes the type of probe used in a process. [Allotrope]
    
ProbeIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002300")
# A probe identifier is a measurement device identifier that identifies some probe. [Allotrope]
    
MolfileMolecularStructure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002308")
# A Molfile molecular structure is a molecular structure specified as an MDL Molfile. [edamontology.org]
    
CycleCount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002311")
# A cycle count is a count of the number of iterations of a repeated process. [Allotrope]
    
HeatFlowProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002312")
# A heat flow profile is a profile that quantifies the heat flow through a material entity over time. [Allotrope]
    
TotalSystemHeatFlowProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002313")
# A total system heat flow profile is a profile that quantifies the heat flow through a system over time. [Allotrope]
    
ReactionHeatFlowProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002314")
# A reaction heat flow profile is a profile that quantifies the heat flow through a material entity with the reaction mixture role over time. [Allotrope]
    
SourceCurrentSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002315")
# A source current setting is a current setting controlling the current supplied to a radiation source. [Allotrope]
    
CurrentSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002316")
# A current setting is a setting that specifies some current configuration of a current controlling or monitoring device, that controls or monitors the target electric current at the site of some system component. [Allotrope]
    
ElectronEnergySetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002317")
# An electron energy setting is a voltage setting controlling the voltage in a source to accelerate electrons to the specified eV kinetic energy. [Allotrope]
    
VoltageSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002318")
# A voltage setting is a setting that specifies some current configuration of a voltage controlling or monitoring device, that controls or monitors the target voltage at the site of some system component. [Allotrope]
    
AnalyteAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002319")
# An analyte aggregate document is a document about an ordered collection of analytes. [Allotrope]
    
AnalyteDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002320")
# An analyte document is a document that is about some analyte. [Allotrope]
    
RadiationSourceType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002324")
# A radiation source type is a classification datum that classifies the type of radiation source used in a process. [Allotrope]
    
ElectronicProjectRecord = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002331")
# An electronic project is a user-defined collection of methods, results, sign-offs, audit trails, custom fields, and raw data. [Allotrope]
    
ReportMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002332")
# A report method is a plan specification that serves as a template to organize the data, results, and method contents in a generated report. The report method is independent of any data that the report contains. [Allotrope]
    
PhProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002337")
# A pH profile is a profile that quantifies the pH of a material entity over time. [Allotrope]
    
StandardAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002338")
# A standard aggregate document is a document that is about an ordered collection of standards. [Allotrope]
    
MassProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002344")
# A mass profile is a profile that quantifies the mass of a material entity over time. [Allotrope]
    
PurgeGasFlowRateProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002345")
# A purge gas flow rate profile is a flow rate profile that quantifies the flow rate of gas with the role of purge gas being added to inert equipment over time. [Allotrope]
    
PurgeGasType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002346")
# A purge gas type is a classification datum that classifies the gas with the role of purge gas used in a rinsing process. [Allotrope]
    
PurgeGasFlowRateDataCube = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002347")
# A purge gas flow rate data cube is a data cube that represents the flow rate of gas with the role of purge gas over time. [Allotrope]
    
BackgroundDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002358")
# A background document is a document that encompasses the information associated with a background measurement. [Allotrope]
    
SpectrometerType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002364")
# A spectrometer type is a classification datum that classifies the type of spectrometer used in a process. [Allotrope]
    
ConcentrationProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002365")
# A concentration profile is a profile that quantifies the concentration of a material entity over time. [Allotrope]
    
AnalysisMaterialRoleType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002367")
# An analysis material role type is a classification datum that classifies the role of a portion of material in a reaction. [Allotrope]
    
AnalyteMolarRatio = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002368")
# An analyte molar ratio is a ratio quantification datum that quantifies the relative molar amount of an analyte to a reference entity. [Allotrope]
    
SamplePreparationAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002369")
# A sample preparation aggregate document is a document that aggregates sample preparation documents. [Allotrope]
    
SamplePreparationDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002370")
# A sample preparation document is a document about a sample preparation process. [Allotrope]
    
MeasurementAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002374")
# A measurement aggregate document is a document about a collection of measurement documents. [Allotrope]
    
MeasurementDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002375")
# A measurement document is a document that encompasses the information associated with a measurement. [Allotrope]
    
ApertureSizeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002389")
# An aperture size setting temperature setting is a control setting that specifies the size of the aperture opening. [Allotrope]
    
SampleMeasurementInterfaceType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002391")
# A sample measurement interface type is a classification datum that classifies the sample measurement interface used by a measuring process. [Allotrope]
    
ThermalConductivity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002392")
# A thermal conductivity is a quality quantification facet that quantifies the disposition to spontaneous transfer of thermal energy from a region of higher temperature to a region of lower temperature. [Allotrope]
    
TemperatureRate = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002393")
# A temperature rate is a quality quantification facet that quantifies the change in temperature over time in some material. [Allotrope]
    
EndPointDeterminationSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002397")
# An end point determination setting is a control setting that specifies the end point of an analysis. [Allotrope]
    
TemperatureProfileSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002401")
# A temperature program setting is a control setting that specifies the heating profile to use to achieve the desired temperature. [Allotrope]
    
RatioQuantificationFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002408")
# A ratio quantification datum is a quantification datum that quantifies the relative magnitude as a ratio of the magnitude of the subject to that of the reference entity. [Allotrope]
    
Apodization = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002410")
# Apodization is the name of a filter method used in some data apodization. [Allotrope]
    
ZeroFillingFactor = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002411")
# The factor of the size increase by time domain zero padding the Fourier transformation. [Allotrope]
    
PhaseCorrection = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002412")
# Phase correction is the name of a method for phase correction used to adjust FT spectra. [Allotrope]
    
ThermalConductance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002413")
# A thermal conductance is a quality quantification facet that quantifies the heat flow over time through a material of specific area and thickness. [Allotrope]
    
ProfileSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002414")
# A profile setting is a setting the specifies the change of a configuration of a system over time or a reaction to a change of a situation over time. [Allotrope]
    
ControlProfileSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002415")
# A control profile setting is a profile setting that specifies how a system&apos;s configuration is controlled over time. [Allotrope]
    
AdfConverterName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002419")
# An ADF converter name is a written name of some software used to convert data into the Allotrope Data Format. [Allotrope]
    
AdfConverterMethodIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002420")
# An ADF converter method identifier is an identifier identifying the method used by an ADF converter to convert a dataset into the Allotrope Data Format. [Allotrope]
    
AdfConverterVersion = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002421")
# An ADF converter version is a software version specifying the version of an ADF converter used to convert a dataset into the Allotrope Data Format. [Allotrope]
    
StartTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002422")
# A start time is a time that denotes the start of some process. [Allotrope]
    
EndTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002423")
# A end time is a time that denotes the end of some process. [Allotrope]
    
ContainerIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002425")
# A container identifier is an identifier that identifies some container. [Allotrope]
    
DataValidityAssessment = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002428")
# A data validity assessment is an assessment about the validity of some data for a specified purpose. [Allotrope]
    
DataValidityCode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002429")
# A data validity code is an code that indicates the validity of some data. [Allotrope]
    
FillDepth = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002436")
# A fill depth is a quality quantification facet quantifying the depth of material in a container. [Allotrope]
    
ResultValueSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002437")
# A result specification is a specification of acceptable limits for a result or set of results. [Allotrope]
    
MaterialSuitabilitySpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002438")
# A material suitability specification is a material specification defining acceptable limits for qualities or required functions or dispositions of some material to be suitable for a specified use case. [Allotrope]
    
SpecificationAssessment = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002439")
# A specification assessment is an assessment about whether some result conforms to a predefined specification. [Allotrope]
    
AbsoluteWaterContent = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002445")
# An absolute water content is a mass datum quantifying the absolute mass of water in a sample. [Allotrope]
    
WaterMassConcentration = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002447")
# A water mass concentration is a mass concentration quantifying the mass of water divided by the total volume of the mixture. [Allotrope]
    
WaterMassFraction = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002448")
# A water mass fraction is a mass fraction quantifying the mass of water divided by the total mass of all constituents in the mixture. [Allotrope]
    
ReadIntervalSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002454")
# A read interval setting is a control setting that specifies the duration between individual reads in a measurement. [Allotrope]
    
TotalMeasurementTimeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002455")
# A total measurement time setting is a control setting that specifies the aggregated duration of a series of measurements. [Allotrope]
    
VialLocationIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002464")
# A vial location identifier is a local identifier that identifies the location of a vial in the vial container in the scope of the vial container. [Allotrope]
    
ImageFormat = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002466")
# An image format is a classification datum classifying an image by the data format specification that its representation has. [Allotrope]
    
ImageHeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002467")
# An image height is the height of some image. [Allotrope]
    
ImageWidth = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002468")
# An image width is the horizontal length of some image. [Allotrope]
    
CondenserLensVoltageSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002469")
# A condenser lens voltage setting is voltage setting specifying the voltage of some condenser lens. [Allotrope]
    
IncidentRadiationAngle = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002475")
# An incident radiation angle is a quality quantification facet quantifying the angle between the beam of radiation and the surface of some sample it impacts. [Allotrope]
    
ExcitationWavelengthSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002479")
# An excitation wavelength setting is a control setting specifying the wavelength of the beam used for the excitation of the sample. [Allotrope]
    
Coordinate = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002485")
# A coordinate is a scalar as component of a vector or tuple in a coordinate system specifying a point in space. [Allotrope]
    
CartesianCoordinate = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002486")
# A Cartesian coordinate is a coordinate in a Cartesian coordinate system, that specifies each point uniquely in an n-dimensional Euclidean space . These coordinates are equal, up to sign, to distances from the point to n mutually perpendicular hyperplanes. [Allotrope, Wikipedia]
    
EmissionBandwidthSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002487")
# An emission bandwidth setting is a control setting that specifies the bandwidth of a particular signal to be emitted by a source. [Allotrope]
    
DetectorModelNumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002489")
# A detector model number is a model number that denotes some class of detectors. [Allotrope]
    
DetectorIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002490")
# A detector identifier is a measurement device identifier that identifies some detector. [Allotrope]
    
SampleVolumeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002492")
# A sample volume setting is a control setting specifying the volume of sample to be used in a measurement. [Allotrope]
    
FlushVolumeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002493")
# A flush volume setting is a control setting specifying the volume of material to be used to flush some device. [Allotrope]
    
DifferentialCount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002494")
# A differential count is a count that has non-negative integer values that is about the number of discrete things within a defined range. [Allotrope]
    
CumulativeParticleDensity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002495")
# A cumulative particle density is a scalar quantity datum that quantifies the number density of particles meeting a given criterion. [Allotrope]
    
DifferentialParticleDensity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002496")
# A differential particle density is a summary datum that quantifies the number density of particles within a specified range criterion. [Allotrope]
    
DataProcessingOmissionSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002497")
# A data processing omission setting is a data processing setting that marks whether the related dataset should be excluded from some data processing. [Allotrope]
    
DilutionFactorSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002498")
# A dilution factor setting is a control setting specifying some dilution factor. [Allotrope]
    
AreaScan = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002499")
# An area scan is a data distribution function over points of a defined area. [Allotrope]
    
PositionCode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002502")
# A position code is a code that indicates a position. [Allotrope]
    
MaterialSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002508")
# A material specification is a specification that specifies some qualities, roles or dispositions of some material. [Allotrope]
    
DeviceSystemDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002526")
# A device system document is a document that encompasses the information associated with a device system. [Allotrope]
    
DetectorControlAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002527")
# A detector control aggregate document is a document that aggregates detector control documents. [Allotrope]
    
DetectorControlDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002528")
# A detector control document is a document that encompasses the information associated with control of a detector. [Allotrope]
    
PumpModelNumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002530")
# A pump model number is a model number that denotes some class of pumps. [Allotrope]
    
Submitter = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002531")
# Submitter is measurement metadata about the name or identifier of a person that has the role of a submitter in the measurement. [Allotrope]
    
ChromatographyColumnPartNumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002532")
# A column part number is a part number that denotes some class of chromatography columns. [Allotrope]
    
ChromatographyColumnSerialNumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002533")
# A column serial number is an equipment serial number that identifies some chromatography column. [Allotrope]
    
DetectionType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002534")
# A detection type is a classification datum that classifies the type of detection performed by the detector.. [Allotrope]
    
DetectorSignal = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002546")
# A detector signal is a signal that is produced by a detector that signals the presence or magnitude of the entity observed by the detector. [Allotrope]
    
ExcitationBandwidthSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002548")
# An excitation bandwidth setting is a control setting specifying the bandwidth of the beam used for the excitation of the sample. [Allotrope]
    
CompartmentTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002549")
# A compartment temperature is a quality quantification facet quantifying the temperature of some compartment. [Allotrope]
    
ElectricImpedance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002554")
# An electric impedance is a quality quantification facet quantifying the electric impedance of some material. [Allotrope]
    
ProfileAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002555")
# A profile aggregate document is a document that aggregates profiles. [Allotrope]
    
MassProfileAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002556")
# A mass profile aggregate document is a document that aggregates mass profiles. [Allotrope]
    
VolumeProfileAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002557")
# A volume profile aggregate document is a document that aggregates volume profiles. [Allotrope]
    
TemperatureProfileAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002558")
# A temperature profile aggregate document is a document that aggregates temperature profiles. [Allotrope]
    
HeatFlowProfileAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002559")
# A heat flow profile aggregate document is a document that aggregates heat flow profiles. [Allotrope]
    
AngularVelocityProfileAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002560")
# An angular velocity profile aggregate document is a document that aggregates angular velocity profiles. [Allotrope]
    
StartTimeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002562")
# A start time setting is a setting specifying the start time of some process. [Allotrope]
    
EndTimeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002563")
# An end time setting is a setting specifying the end time of some process. [Allotrope]
    
DeviceDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002567")
# A device document is a document that encompasses the information associated with a device. [Allotrope]
    
DeviceType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002568")
# A device type is a classification datum that classifies the type of device used. [Allotrope]
    
GripVelocitySetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002569")
# A grip velocity setting is a control setting specifying the velocity at which the device grips move during the run. [Allotrope]
    
GripDistanceSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002571")
# A grip distance setting is a control setting that specifies the distance between the grips of a device at the start of a measurement run. [Allotrope]
    
SamplingOrientationType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002573")
# A sampling orientation type is a classification datum that classifies the orientation of the cuts used to separate a sample from the material it was derived from, relative to the device extruding the material. [Allotrope]
    
SampleShapeClassification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002574")
# A sample shape classification is a classification datum that classifies the shape of the sample undergoing testing. [Allotrope]
    
SampleThickness = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002575")
# A sample thickness is a quality quantification facet that quantifies the thickness of some sample. [Allotrope]
    
SampleWidth = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002576")
# A sample width is a quality quantification facet that quantifies the horizontal length of a sample at the point of measurement. [Allotrope]
    
YoungModulus = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002583")
# A Young modulus is a quality quantification facet quantifying the ratio of tensile stress to tensile strain of a material. [Allotrope]
    
SamplingOrientationCode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002596")
# A sampling orientation code is a code that indicates a sampling orientation. [Allotrope]
    
CodeScanResult = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002603")
# A code scan result is an assay result that is the output of a code scanning. [Allotrope]
    
DeviceResponseSignal = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002604")
# A device response signal is a signal that is sent by some device as a result of some prior communication. [Allotrope]
    
SamplingType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002610")
# A sampling type is a classification datum that classifies the type of sampling approach used to take a sample. [Allotrope]
    
MeasurementStartSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002612")
# A measurement start delay setting is a control setting that specifies a delay before starting a measurement process. [Allotrope]
    
AmbientPressure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002613")
# An ambient pressure is a quantity facet that quantifies the pressure of the surrounding atmosphere. [Allotrope]
    
RelativeHumidity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002614")
# Relative humidity is the ratio, often expressed as a percentage, of the partial pressure of water in the atmosphere at some observed temperature, to the saturation vapor pressure of pure water at this temperature. [IUPAC]
    
ReservoirTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002616")
# A reservoir temperature is a quantity facet that quantifies the temperature of some reservoir. [Allotrope]
    
PlateTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002618")
# A plate temperature is a quality quantification facet that quantifies the temperature of some plate. [Allotrope]
    
PlateHeaterTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002619")
# A plate heater temperature is a quality quantification facet that quantifies the temperature of some plate heater. [Allotrope]
    
DielectricPolarizationFieldFrequencySetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002620")
# A dielectric polarization field frequency setting is a control setting that specifies the frequency of the electrical field used for dielectric polarization of a sample. [Allotrope]
    
ReactionDuration = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002621")
# A reaction duration is a duration that indicates the time taken for a reaction to complete. [Allotrope]
    
ForceGaugeType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002622")
# A force gauge type is a classification datum that classifies some force gauge by its rated force calibration. [Allotrope]
    
ContainerShape = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002623")
# A container shape is a classification datum that classifies the shape of some container. [Allotrope]
    
ContainerHeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002624")
# A container height is a height of some container. [Allotrope]
    
ContainerDiameter = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002625")
# A container diameter is a diameter of some container. [Allotrope]
    
ProcessTerminationStateType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002626")
# A process termination state type is a classification facet that classifies the process state at the end of a process. [Allotrope]
    
StartHeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002627")
# A start height is the height of some entity at the start of a process. [Allotrope]
    
EndHeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002628")
# An end height is the height of some entity at the end of a process. [Allotrope]
    
GelTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002636")
# A gel time is the time at which a material&apos;s state of matter transitions into a gel. [Allotrope]
    
DielectricPolarization = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002640")
# The electric displacement vector and the product of the electric field strength with the permittivity of vacuum. [IUPAC]
    
SampleIntroductionDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002645")
# A sample introduction document is a document that encompasses the information associated with the process of sample introduction. [Allotrope]
    
SampleIntroductionModeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002646")
# A sample introduction mode setting is a control setting that specifies the type of sample introduction process to be used, which is the process of loading the sample into a system. [Allotrope]
    
LaserFiringFrequencySetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002647")
# A laser firing frequency setting is a control setting that specifies the frequency of firing of a laser. [Allotrope]
    
SampleIntroductionDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002648")
# A sample introduction description is a description that describes the process of sample introduction. [Allotrope]
    
SampleIntroductionMedium = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002649")
# A sample introduction medium designates the material type that is used as medium (role) in a sample introduction process in a measurement. [Allotrope]
    
MeasurementModeSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002650")
# A measurement mode setting is a control setting that specifies the measurement mode of some measurement process. [Allotrope]
    
DataProcessingAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002654")
# A data processing aggregate document is a document that aggregates data processing documents. [Allotrope]
    
DataProcessingDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002655")
# A data processing document is a document that encompasses the metadata associated with a data processing operation. [Allotrope]
    
DataProcessingType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002656")
# A data processing type is a classification datum that classifies the type of data processing performed. [Allotrope]
    
DataFormatSpecificationType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002657")
# A data format specification type is a classification datum that classifies the data format used to store data. [Allotrope]
    
ProcessedDataAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002658")
# A processed data aggregate document is a document that aggregates processed data documents. [Allotrope]
    
ProcessedDataDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002659")
# A processed data document is a document that encompasses the output of some data processing operation. [Allotrope]
    
DataProcessingDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002660")
# A data processing description is a description of some data processing operation. [Allotrope]
    
PixelDensity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002664")
# A pixel density is a figure facet that quantifies the number of pixels per unit size of some image. [Allotrope]
    
ExceptionDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002682")
# An exception description is a description of some unexpected, unusual or unintended situation. [Allotrope]
    
PixelCount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002685")
# A pixel count is a count of the number of pixels in some raster image. [Allotrope]
    
Eccentricity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002686")
# An eccentricity is a quality quantification facet that quantifies some eccentricity. [Allotrope]
    
RelativeLocation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002687")
# A relative location is a location facet that denotes a location of an entity relative to some other entity. [Allotrope]
    
Pixel = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002693")
# A pixel is a figure facet that is the smallest addressable element in a raster image. [Wikipedia]
    
RasterImage = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002694")
# A raster image is an image represented as a rectangular matrix or grid of square pixels, viewable via a computer display, paper, or other display medium. [Wikipedia]
    
StatisticsAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002697")
# A statistics aggregate document is a document that aggregates statistics documents. [Allotrope]
    
StatisticsDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002698")
# A statistics document is a document that encapsulates the statistical information associated with some population. [Allotrope]
    
StartDelay = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002700")
# A start delay is a process property that describes a difference in time between a start process boundary and some other point in time. [Allotrope]
    
EndDelay = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002701")
# An end delay is a process property that describes a difference in time between an end process boundary and some other point in time. [Allotrope]
    
DiagnosticTraceAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002705")
# A diagnostic trace aggregate document is a document that aggregates diagnostic trace documents. [Allotrope]
    
DiagnosticTraceDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002706")
# A diagnostic trace document is a document that encapsulates the information associated with a diagnostic trace. [Allotrope]
    
AbrasionSourceDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002709")
# An abrasion source description is a description of the device or manual agent of abrasion in an abrasion process. [Allotrope]
    
CoatedMaterialDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002710")
# A coated material description is a description of the material with the role of coated material. [Allotrope]
    
AbradingMaterialDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002711")
# An abrading material description is a description of the material with the role of abrading material. [Allotrope]
    
AbrasionCycleCount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002713")
# An abrasion cycle count is a count of the number of abrasion cycles in an abrasion process. [Allotrope]
    
AbrasionWeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002714")
# An abrasion weight is a mass facet that quantifies the mass of the component used to apply abrasion to a sample. [Allotrope]
    
DeviceControlAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002722")
# A device control aggregate document is a document that aggregates device control documents. [Allotrope]
    
DeviceControlDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002723")
# A device control document is a document that encompasses the information associated with control of a device. [Allotrope]
    
GripPressureSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002724")
# A grip pressure setting is a pressure setting that specifies the pressure applied to a material by the closure of a pair of grips. [Allotrope]
    
SeparationAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002729")
# A separation aggregate document is a document that aggregates separation documents. [Allotrope]
    
SeparationDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002730")
# A separation document is a document that encompasses the information associated with some separating process. [Allotrope]
    
PressureSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002731")
# A pressure setting is a setting that specifies some pressure configuration of a pressure controlling or monitoring device, that controls or monitors the target pressure at the site of some system component. [Allotrope]
    
LogSourceName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002743")
# A log source name is a written name that denotes the source of some log entry. [Allotrope]
    
SystemSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002744")
# A system setting is a setting that specifies the configuration of some system. [Allotrope]
    
VelocitySetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002745")
# A velocity setting is a setting that specifies some velocity configuration of a  controlling or monitoring device, that controls or monitors the velocity of some process occurring at the site of some system component. [Allotrope]
    
DistanceSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002746")
# A distance setting is a setting that specifies some distance configuration of a  controlling or monitoring device, that controls or monitors the distance between materials at the site of some system component. [Allotrope]
    
GrippingDeviceSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002747")
# A gripping device setting is a setting that specifies the configuration of a gripping device. [Allotrope]
    
AsmConverterName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002748")
# An ASM converter name is a written name of some software used to convert data into the Allotrope Simple Model format. [Allotrope]
    
AsmConverterVersion = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002749")
# An ASM converter version is a software version specifying the version of an ASM converter used to convert data into the Allotrope Simple Model format. [Allotrope]
    
ServerIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002750")
# A server identifier is an identifier that identifies some server. [Allotrope]
    
AsmConverterMethodIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002751")
# An ASM converter method identifier is an identifier identifying the method used by an ASM converter to convert data into the Allotrope Simple Model format. [Allotrope]
    
FractionAggregateDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002752")
# A fraction aggregate document is a document that aggregates fraction documents. [Allotrope]
    
FractionDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002753")
# A fraction document is a document that encompasses the information associated with a fraction. [Allotrope]
    
CreationTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002755")
# A creation time is the time when an entity was created. [Allotrope]
    
ModifiedTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002756")
# A modified time is the time when a particular change was made to an entity. [Allotrope]
    
LastModifiedTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002757")
# A last modified time is the time when the last change was made to an entity. [Allotrope]
    
DilutionFactor = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002758")
# A dilution factor is a ratio quantification facet that quantifies the ratio of the final volume to the original aliquot volume of a solution in a dilution process. [Allotrope]
    
RelativeResponse = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002760")
# A relative response is a ratio quantification facet that quantifies the ratio of an analytes device response signal to the device response signal of some reference material. [Allotrope]
    
IntegrationAlgorithmType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002763")
# An integration algorithm type is a classification datum that classifies the integration algorithm used in an integration process. [Allotrope]
    
CustomInformationDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002764")
# A custom information document is a document that about some labeled information entity for which limited meaning and/or context is known. [Allotrope]
    
AttenuationCoefficient = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002765")
# Linear decadic (a,K) and Napierian attenuation coefficients (α) are equal to the corresponding absorbances divided by the optical path length through the sample, but taking into account also the effects due to scattering and luminescence. The molar absorption coefficients (decadic ε, Napierian κ) are the linear absorption coefficients divided by the amount concentration. [IUPAC]
    
ProteinAttenuationCoefficient = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002766")
# A protein attenuation coefficient is a calculated extinction coefficient at 280 nm of a protein calculated from the number of aromatic amino acids, particularly tryptophan. [Allotrope]
    
MolarAbsorptivity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002767")
# A molar absorptivity is an attenuation coefficient where the concentration is molarity and the path length is decimeters. [Allotrope]
    
ElectronicSignatureDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002769")
# An electronic signature document is a document about some electronic signature. [Allotrope]
    
DataSystemDocument = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002771")
# A data system document is a document that encapsulates the information associated with some data system. [Allotrope]
    
DataSystemInstanceIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002772")
# A data system instance identifier is an identifier that identifies an instance of some data system. [Allotrope]
    
LogEntryType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002793")
# A log entry type is a classification datum that classifies a log entry in a log. [Allotrope]
    
SignatureRoleType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002794")
# A signature role type is a classification datum that classifies the signature role of some signature. [Allotrope]
    
AsmConverter = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002795")
# An ASM converter is a software used to convert data into the Allotrope Simple Model format. [Allotrope]
    
AdfConverter = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002796")
# An ADF converter is a software used to convert data into the Allotrope Data Format. [Allotrope]
    
DataFormatConversionSoftware = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002801")
# A data format conversion software is a software the converts data into a specified target format. [Allotrope]
    
SoftwareName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002802")
# A software name is a name of some software. [Allotrope]
    
ProcessingEnabledSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002805")
# A processing enabled setting is a data processing setting that allows data processing to occur. [Allotrope]
    
StandardIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002810")
# A standard identifier is an identifier that identifies a standard being measured. [Allotrope]
    
DissolutionVesselIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002819")
# A dissolution vessel identifier is an identifier that identifies some dissolution vessel. [Allotrope]
    
BathIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002820")
# A bath identifier is an identifier that identifies some bath. [Allotrope]
    
SamplingTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002821")
# A sampling time is an elapsed time at which a sample was taken from a process measured from the start of that process. [Allotrope]
    
SignalToNoiseCalculationEnabledSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002827")
# A signal to noise calculation enabled setting is a data processing setting that indicates if signal to noise results are to be calculated. [Allotrope]
    
BaselineNoiseMinimumRuntimePercentageSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002833")
# A baseline noise minimum runtime percentage setting is a data processing setting that indicates the minimal duration for calculating the baseline noise as a percentage of the run time. [Allotrope]
    
MaximumAllowableNoiseSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002834")
# A maximum allowable noise setting is a data processing setting that indicates the maximum allowed noise value for measured noise in order for a run to be deemed valid. [Allotrope]
    
MaximumAllowableBaselineDriftSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002835")
# A maximum allowable baseline drift setting is a data processing setting that indicates the maximum allowed drift value for measured signal in order for a run to be deemed valid. [Allotrope]
    
BaselineNoiseMinimumDurationSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002836")
# A baseline noise minimum duration setting is a data processing setting that indicates the minimum duration that can be used to measure the baseline noise. [Allotrope]
    
DispensingDuration = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002839")
# A dispensing duration is a duration that indicates the time taken for a material to be dispensed. [Allotrope]
    
DispensedVolume = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002840")
# A dispensed volume is a volume (datum) that quantifies the volume of material that was dispensed. [Allotrope]
    
LocationIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002844")
# A location identifier is an identifier that identifies some location or site. [Allotrope]
    
InputRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000008")
# A general role if its bearer is the input of the process that realizes the role. The bearer exists at the beginning of the process but not necessarily at its end. [Allotrope]
    
MaterialInputRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000010")
# Material input is a role of a material that is an input in a process. [Allotrope]
    
OperatingMaximum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000016")
# An operating maximum is the contextual role of a description or specification of an upper bound of quality of a system or environment during the operation of the system. [Allotrope]
    
OperatingRange = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000017")
# An operating range is the contextual role of a description or specification about a operating situation (qualities of a system or its environment) during the normal operation of the system. [Allotrope]
    
OutputRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000018")
# A general role if its bearer is the output of the process that realizes the role. The bearer exists at the end of the process but not necessarily at its beginning. [Allotrope]
    
SelectedDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000027")
# A device that is selected to perform a specific function in a process. [Allotrope]
    
SpecifiedAction = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000066")
# Specified action is the role of information object that specifies an activity. [Allotrope]
    
SpecifiedCapability = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000067")
# Specified capability is the contextual role of an information object that specifies a capability. [Allotrope]
    
SpecifiedQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000068")
# A specified quality is the contextual role of an information object that describes a quality as part of an specification. [Allotrope]
    
SpecifiedSituation = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000069")
# A specified situation is the contextual role of an information object that describes a portion of reality as part of a specification. [Allotrope]
    
SpecifiedProcedure = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000071")
# Specified procedure is the contextual role of an information object that specifies a flow of activities. [Allotrope]
    
SpecifiedProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000079")
# Specified profile is the contextual role of an information object that specifies a process profile. [Allotrope]
    
SupportRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000085")
# A support role is a type of role whose bearer participates in a process in order to support the process so that it proceeds towards a secondary objective. [Allotrope]
    
GeneralRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000091")
# A general role is either a role that is realized in a process or a contextual role in that process. [Allotrope]
    
AgentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000095")
# The role of a participant that delivers the necessary effects as active participant in the process to the operand. [Allotrope]
    
MaterialOutputRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000100")
# Material output role is a role of a material that is participant at the end of a process. [Allotrope]
    
PhysicalSignalRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000159")
# A signal is a role of some material entity that disposed to provide information. In the physical world, any quantity exhibiting variation in time or variation in space (such as an image) is potentially a signal that might provide information on the status of a physical system, or convey a message between observers, among other possibilities. [Allotrope, Wikipedia]
    
PhysicalInputRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000160")
# &quot;Physical input&quot; is a role of a material or energy that is input in a process. [Allotrope]
    
PhysicalOutputRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000161")
# &quot;Physical input&quot; is a role of a material or energy that is input in a process. [Allotrope]
    
OperandRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000167")
# The role of a participant that is being changed in the process (passive participant) from an input state to an output state. [Allotrope]
    
GeneralAgentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000448")
# Agentive role is a general role of a material entity or software that  influences the behavior of a process in an active way. If a material entity it is an agent role, if its is a software that is executed by a computer system, it is a software agent role. [Allotrope]
    
CalibrationItemRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000493")
# The calibration item role is the role of a material that is used in calibration for testing a measurement device. [Allotrope]
    
IonRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000499")
# An ion role is a role inhered in an ion. [Allotrope]
    
OperatingMinimum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000504")
# An operating minimum is the contextual role of a description or specification of a lower bound of quality of a system or environment during the operation of the system. [Allotrope]
    
SampleRole_preparation = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000508")
# A sample role (preparation) is a role of a portion of material that is prepared for bearing the sample role in an experiment. [Allotrope]
    
RepeatedActionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000521")
# A repeated action role is a contextual role of an action specification that specifies the repeated action in a repeated action specification. [Allotrope]
    
ReactionMixtureRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000533")
# A reaction mixture role is a role of a chemical mixture undergoing some chemical reaction. [Allotrope]
    
PurgeGasRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000542")
# A purge gas role is a cleaning agent role of a gas used to remove or replace an existing gas. [Allotrope]
    
ProductRole_economic = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000543")
# A product role (economic) is a general role of some continuant that is produced for the purpose of sale. [Allotrope]
    
PhysicalProductRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000545")
# A physical product role is a role of some artifact that is produced for the purpose of sale. [Allotrope]
    
SampleIntroductionMediumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000549")
# A sample introduction medium is the role of a material that carries the sample in a sample introduction process. [Allotrope]
    
CarrierRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000553")
# A carrier role is the role of a material entity that supports another material or information localization process by keeping it moving or holding it at place. [Allotrope]
    
CarryingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000554")
# A carrying role is a role of an entity that is realized in a carrying process. [Allotrope]
    
LoadedMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000555")
# The loaded material is the role of the material that is loaded into the destination. [Allotrope]
    
AbradingMaterialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000558")
# An abrading material role is an abrading role of a material whose surface is being applied to another material to cause abrasion. [Allotrope]
    
AbradedMaterialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000559")
# An abraded material is an abrading role of a material whose surface is being abraded in an abrading process. [Allotrope]
    
AbradingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000560")
# An abrading role is a role of an entity that is realized in an abrading process. [Allotrope]
    
AbradingSourceRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000561")
# An abrading source role is an abrading role of a device or human that abrades material using abrading material. [Allotrope]
    
FractionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000563")
# A fraction role is the role of a member of the collection of material that is collected in a fraction collection process. [Allotrope]
    
Space = onto.search_one(iri="http://purl.allotrope.org/ontologies/spatial#AFSP_0000005")
# A space is a site that can be occupied or where something can be done. [Allotrope]
    
Section_site = onto.search_one(iri="http://purl.allotrope.org/ontologies/spatial#AFSP_0000007")
# A section is a site that is a more or less distinct part of a site into which the site is divided. [Allotrope]
    
Well = onto.search_one(iri="http://purl.allotrope.org/ontologies/spatial#AFSP_0000009")
# A well is a site that is a cavity in a surface open at the top. [Allotrope]
    
EnvironmentalMaterial = onto.search_one(iri="http://purl.obolibrary.org/obo/ENVO_00010483")
# An environmental material is a fiat object which forms the medium or part of the medium of an environmental system. [ENVO]
    
EnvironmentalSystem = onto.search_one(iri="http://purl.obolibrary.org/obo/ENVO_01000254")
# A system which has the disposition to environ one or more material entities. [ENVO]
    
MaterialInformationBearer = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000178")
# A material entity in which a concretization of an information content entity inheres. [IAO]
    
PlannedProcess = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000011")
# A processual entity that realizes a plan which is the concretization of a plan specification. [IAO]
    
ProcessedMaterial = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000047")
# Is a material entity that is created or changed during material processing. [OBI]
    
MaterialProcessing = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000094")
# Material processing is a planned material process which results in physical changes in a specified input material. [OBI]
    
Manufacturing = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000457")
# Manufacturing is a producing with the intent to produce a processed material which will have a function for future use. [OBI]
    
ManufacturerRole = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000571")
# Manufacturer role is a role which inheres in a person or organization and which is realized by a manufacturing process. [OBI]
    
Manufacturer = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000835")
# A manufacturer is an organizational entity that has a manufacturer role. [Allotrope]
    
DataCube = onto.search_one(iri="http://purl.org/linked-data/cube#DataSet")
# Represents a collection of observations, possibly organized into various slices, conforming to some common dimensional structure. [QB]
    