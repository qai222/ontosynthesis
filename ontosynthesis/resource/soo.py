# THIS FILES IS AUTOMATICALLY GENERATED BY /home/qai/workplace/ontosynthesis/ontologies/soo/to_owlready2.py
# PLEASE DO NOT EDIT
import os.path

from owlready2 import get_ontology

this_dir = os.path.dirname(os.path.abspath(__file__))
ontology_owl_path = os.path.join(this_dir, "../../ontologies/soo/soo.owl")

onto = get_ontology(f"file://{ontology_owl_path}").load()

AgitatorModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000141")
AgitatorModule.label.append('AgitatorModule')

AirDisplacementLiquidTransporterModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000146")
AirDisplacementLiquidTransporterModule.label.append('AirDisplacementLiquidTransporterModule')

AirtightEnvironment = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000220")
AirtightEnvironment.label.append('AirtightEnvironment')

AliquotingController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000114")
AliquotingController.label.append('AliquotingController')

Anti_solventCrystallizing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000045")
Anti_solventCrystallizing.label.append('Anti_solventCrystallizing')

AssembleHardwareUnits = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000197")
AssembleHardwareUnits.label.append('AssembleHardwareUnits')

Centrifugating = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000185")
Centrifugating.label.append('Centrifugating')

CentrifugationModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000186")
CentrifugationModule.label.append('CentrifugationModule')

ChangingMaterialQuality = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000104")
ChangingMaterialQuality.label.append('ChangingMaterialQuality')

ChangingMaterialQualityWithoutControl = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000105")
ChangingMaterialQualityWithoutControl.label.append('ChangingMaterialQualityWithoutControl')

ChangingTemperatureWithoutControl = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000106")
ChangingTemperatureWithoutControl.label.append('ChangingTemperatureWithoutControl')

ChemicalProcess = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000031")
ChemicalProcess.label.append('ChemicalProcess')

ChromatographyModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000184")
ChromatographyModule.label.append('ChromatographyModule')

ChromatographySeparating = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000183")
ChromatographySeparating.label.append('ChromatographySeparating')

CleanHardwareUnit = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000194")
CleanHardwareUnit.label.append('CleanHardwareUnit')

CombiningMaterials = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000139")
CombiningMaterials.label.append('CombiningMaterials')

CombiningMaterialsToQuenchReaction = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000137")
CombiningMaterialsToQuenchReaction.label.append('CombiningMaterialsToQuenchReaction')

Condensing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000067")
Condensing.label.append('Condensing')

CondensingModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000296")
CondensingModule.label.append('CondensingModule')

Condensor = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000301")
Condensor.label.append('Condensor')

ContainerEnvironment = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000126")
ContainerEnvironment.label.append('ContainerEnvironment')

ControllingPh = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000057")
ControllingPh.label.append('ControllingPh')

ControllingTemperature = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000055")
ControllingTemperature.label.append('ControllingTemperature')

ControllingVolume = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000056")
ControllingVolume.label.append('ControllingVolume')

CoolingModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000188")
CoolingModule.label.append('CoolingModule')

Crystallizing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000044")
Crystallizing.label.append('Crystallizing')

Degassing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000047")
Degassing.label.append('Degassing')

Depositing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000068")
Depositing.label.append('Depositing')

DisassembleHardwareUnit = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000198")
DisassembleHardwareUnit.label.append('DisassembleHardwareUnit')

Dispersion = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000083")
Dispersion.label.append('Dispersion')

DispersiveLiquid_liquidMicroextraction = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000290")
DispersiveLiquid_liquidMicroextraction.label.append('DispersiveLiquid_liquidMicroextraction')

Dissolving = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000060")
Dissolving.label.append('Dissolving')

DryHardwareUnit = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000195")
DryHardwareUnit.label.append('DryHardwareUnit')

EndpointControlledProcess = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000191")
EndpointControlledProcess.label.append('EndpointControlledProcess')

Environment = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000014")
Environment.label.append('Environment')

Evaporating = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000063")
Evaporating.label.append('Evaporating')

FeedbackController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000096")
FeedbackController.label.append('FeedbackController')

FeedforwardController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000097")
FeedforwardController.label.append('FeedforwardController')

Filter = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000134")
Filter.label.append('Filter')

Filtering = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000041")
Filtering.label.append('Filtering')

FiltrationModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000127")
FiltrationModule.label.append('FiltrationModule')

Freeze_pump_thaw = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000277")
Freeze_pump_thaw.label.append('Freeze_pump_thaw')

Freeze_pump_thawModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000285")
Freeze_pump_thawModule.label.append('Freeze_pump_thawModule')

Freezing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000066")
Freezing.label.append('Freezing')

FunctionalModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000091")
FunctionalModule.label.append('FunctionalModule')

FunnelExtraction = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000291")
FunnelExtraction.label.append('FunnelExtraction')

HardwareUnit = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000011")
HardwareUnit.label.append('HardwareUnit')

HardwareUnitContainer = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000258")
HardwareUnitContainer.label.append('HardwareUnitContainer')

HardwareUnitRack = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000263")
HardwareUnitRack.label.append('HardwareUnitRack')

HardwareUnitSlot = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000262")
HardwareUnitSlot.label.append('HardwareUnitSlot')

HeatingModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000215")
HeatingModule.label.append('HeatingModule')

HomogeneousMixture = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000084")
HomogeneousMixture.label.append('HomogeneousMixture')

Homogenizing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000061")
Homogenizing.label.append('Homogenizing')

InformationEntity = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000120")
InformationEntity.label.append('InformationEntity')

InstrumentCalibration = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000121")
InstrumentCalibration.label.append('InstrumentCalibration')

LabEnvironment = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000123")
LabEnvironment.label.append('LabEnvironment')

LiquidMaterial = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000089")
LiquidMaterial.label.append('LiquidMaterial')

LiquidTransporterModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000131")
LiquidTransporterModule.label.append('LiquidTransporterModule')

Liquid_liquidExtracting = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000050")
Liquid_liquidExtracting.label.append('Liquid_liquidExtracting')

LubricateJoint = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000196")
LubricateJoint.label.append('LubricateJoint')

MagneticStirrerModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000142")
MagneticStirrerModule.label.append('MagneticStirrerModule')

ManualPipetteModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000187")
ManualPipetteModule.label.append('ManualPipetteModule')

MaterialContainer = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000304")
MaterialContainer.label.append('MaterialContainer')

MaterialFlowController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000218")
MaterialFlowController.label.append('MaterialFlowController')

MaterialHolder = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000303")
MaterialHolder.label.append('MaterialHolder')

MaterialMassController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000118")
MaterialMassController.label.append('MaterialMassController')

MaterialProcess = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000")
MaterialProcess.label.append('MaterialProcess')

MaterialQuantityController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000116")
MaterialQuantityController.label.append('MaterialQuantityController')

MaterialTransporterModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000099")
MaterialTransporterModule.label.append('MaterialTransporterModule')

MaterialTransportingComponent = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000315")
MaterialTransportingComponent.label.append('MaterialTransportingComponent')

MaterialVolumeController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000117")
MaterialVolumeController.label.append('MaterialVolumeController')

Melting = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000065")
Melting.label.append('Melting')

Mixing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000059")
Mixing.label.append('Mixing')

MixingWithAgitation = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000140")
MixingWithAgitation.label.append('MixingWithAgitation')

MixtureEvaporating = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000034")
MixtureEvaporating.label.append('MixtureEvaporating')

MultiphaseMaterial = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000090")
MultiphaseMaterial.label.append('MultiphaseMaterial')

Operation = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000180")
Operation.label.append('Operation')

OverheadStirrerModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000211")
OverheadStirrerModule.label.append('OverheadStirrerModule')

PhController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000107")
PhController.label.append('PhController')

PhaseTransitioning = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000062")
PhaseTransitioning.label.append('PhaseTransitioning')

PhysicalProcess = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000030")
PhysicalProcess.label.append('PhysicalProcess')

PipetteTip = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000316")
PipetteTip.label.append('PipetteTip')

PortionOfMaterial = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000078")
PortionOfMaterial.label.append('PortionOfMaterial')

PortionOfMixedMaterial = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000079")
PortionOfMixedMaterial.label.append('PortionOfMixedMaterial')

PositiveDisplacementLiquidTransporterModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000145")
PositiveDisplacementLiquidTransporterModule.label.append('PositiveDisplacementLiquidTransporterModule')

Precipitating = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000043")
Precipitating.label.append('Precipitating')

PrepareContainer = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000204")
PrepareContainer.label.append('PrepareContainer')

PrepareEquipment = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000193")
PrepareEquipment.label.append('PrepareEquipment')

PrepareGlassware = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000199")
PrepareGlassware.label.append('PrepareGlassware')

PressureReducingModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000286")
PressureReducingModule.label.append('PressureReducingModule')

ProcessController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000092")
ProcessController.label.append('ProcessController')

ProcessEndpointController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000109")
ProcessEndpointController.label.append('ProcessEndpointController')

QuenchCooling = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000138")
QuenchCooling.label.append('QuenchCooling')

ReactionProcedure = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000122")
ReactionProcedure.label.append('ReactionProcedure')

Recrystallizing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000049")
Recrystallizing.label.append('Recrystallizing')

RefluxEnvironment = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000125")
RefluxEnvironment.label.append('RefluxEnvironment')

RinseAddition = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000276")
RinseAddition.label.append('RinseAddition')

RobotArm = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000274")
RobotArm.label.append('RobotArm')

RobotArmAttachment = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000275")
RobotArmAttachment.label.append('RobotArmAttachment')

RotaryEvaporatingModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000299")
RotaryEvaporatingModule.label.append('RotaryEvaporatingModule')

RotaryEvaporation = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000295")
RotaryEvaporation.label.append('RotaryEvaporation')

SaltingOut = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000046")
SaltingOut.label.append('SaltingOut')

Separating = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000032")
Separating.label.append('Separating')

SeparatingByAffinityDifference = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000052")
SeparatingByAffinityDifference.label.append('SeparatingByAffinityDifference')

SeparatingByGrainSize = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000040")
SeparatingByGrainSize.label.append('SeparatingByGrainSize')

SeparatingByMassDifference = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000053")
SeparatingByMassDifference.label.append('SeparatingByMassDifference')

SeparatingBySolubilityDifference = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000042")
SeparatingBySolubilityDifference.label.append('SeparatingBySolubilityDifference')

SeparatingByVolatilityDifference = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000033")
SeparatingByVolatilityDifference.label.append('SeparatingByVolatilityDifference')

SeparatingModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000279")
SeparatingModule.label.append('SeparatingModule')

ShakerModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000214")
ShakerModule.label.append('ShakerModule')

SolidHopperModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000147")
SolidHopperModule.label.append('SolidHopperModule')

SolidMaterial = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000087")
SolidMaterial.label.append('SolidMaterial')

SolidTransporterModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000130")
SolidTransporterModule.label.append('SolidTransporterModule')

SonicatorModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000212")
SonicatorModule.label.append('SonicatorModule')

SourceMassController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000216")
SourceMassController.label.append('SourceMassController')

Sparging = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000278")
Sparging.label.append('Sparging')

SpargingModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000284")
SpargingModule.label.append('SpargingModule')

Spray = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000082")
Spray.label.append('Spray')

SteeredlyPouringLiquidModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000219")
SteeredlyPouringLiquidModule.label.append('SteeredlyPouringLiquidModule')

StirrerModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000210")
StirrerModule.label.append('StirrerModule')

Sublimating = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000064")
Sublimating.label.append('Sublimating')

Suspension = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000081")
Suspension.label.append('Suspension')

SyringeNeedle = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000317")
SyringeNeedle.label.append('SyringeNeedle')

SyringePlunger = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000001")
SyringePlunger.label.append('SyringePlunger')

SyringePumpModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000149")
SyringePumpModule.label.append('SyringePumpModule')

SyringeTube = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000318")
SyringeTube.label.append('SyringeTube')

TargetMassController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000217")
TargetMassController.label.append('TargetMassController')

TemperatureController = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000108")
TemperatureController.label.append('TemperatureController')

ToBaseBath = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000202")
ToBaseBath.label.append('ToBaseBath')

ToCap = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000206")
ToCap.label.append('ToCap')

ToCleanGlassware = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000200")
ToCleanGlassware.label.append('ToCleanGlassware')

ToDecap = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000207")
ToDecap.label.append('ToDecap')

ToDryGlassware = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000203")
ToDryGlassware.label.append('ToDryGlassware')

ToPurge = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000208")
ToPurge.label.append('ToPurge')

ToSealContainer = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000205")
ToSealContainer.label.append('ToSealContainer')

ToWashWithDetergent = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000201")
ToWashWithDetergent.label.append('ToWashWithDetergent')

Transporting = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000058")
Transporting.label.append('Transporting')

UniphaseMaterial = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000086")
UniphaseMaterial.label.append('UniphaseMaterial')

Vial = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000305")
Vial.label.append('Vial')

VortexerModule = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000213")
VortexerModule.label.append('VortexerModule')

WashingLiquid = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000294")
WashingLiquid.label.append('WashingLiquid')

WashingMaterial = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000048")
WashingMaterial.label.append('WashingMaterial')

WashingSolid = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000293")
WashingSolid.label.append('WashingSolid')

Weighing = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000209")
Weighing.label.append('Weighing')

WellPlate = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000314")
WellPlate.label.append('WellPlate')

describes = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000128")
describes.python_name = 'describes'

has_crystallizing_anti_solvent = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000287")
has_crystallizing_anti_solvent.python_name = 'has_crystallizing_anti_solvent'

has_dispersive_solvent = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000292")
has_dispersive_solvent.python_name = 'has_dispersive_solvent'

has_end_location = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000102")
has_end_location.python_name = 'has_end_location'

has_extracting_solvent = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000282")
has_extracting_solvent.python_name = 'has_extracting_solvent'

has_first_step = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000003")
has_first_step.python_name = 'has_first_step'

has_input = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000023")
has_input.python_name = 'has_input'

has_material_input = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000024")
has_material_input.python_name = 'has_material_input'

has_material_output = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000026")
has_material_output.python_name = 'has_material_output'

has_mobile_phase = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000281")
has_mobile_phase.python_name = 'has_mobile_phase'

has_output = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000025")
has_output.python_name = 'has_output'

has_pH_adjusting_material = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000133")
has_pH_adjusting_material.python_name = 'has_pH_adjusting_material'

has_part = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000015")
has_part.python_name = 'has_part'

has_precipitation_salt = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000288")
has_precipitation_salt.python_name = 'has_precipitation_salt'

has_proper_part = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000016")
has_proper_part.python_name = 'has_proper_part'

has_recrystallizing_solvent = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000289")
has_recrystallizing_solvent.python_name = 'has_recrystallizing_solvent'

has_second_step = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000004")
has_second_step.python_name = 'has_second_step'

has_separation_input = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000006")
has_separation_input.python_name = 'has_separation_input'

has_separation_output = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000007")
has_separation_output.python_name = 'has_separation_output'

has_sparging_gas = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000283")
has_sparging_gas.python_name = 'has_sparging_gas'

has_start_location = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000101")
has_start_location.python_name = 'has_start_location'

has_third_step = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000005")
has_third_step.python_name = 'has_third_step'

has_washing_solvent = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000280")
has_washing_solvent.python_name = 'has_washing_solvent'

is_contained_by = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000027")
is_contained_by.python_name = 'is_contained_by'

is_dependent_on = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000000")
is_dependent_on.python_name = 'is_dependent_on'

is_environed_by = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000029")
is_environed_by.python_name = 'is_environed_by'

is_immediately_preceded_by = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000135")
is_immediately_preceded_by.python_name = 'is_immediately_preceded_by'

is_preceded_by = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000095")
is_preceded_by.python_name = 'is_preceded_by'

is_realized_by = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000115")
is_realized_by.python_name = 'is_realized_by'

operates_on = onto.search_one(iri="http://www.ontosynthesis.org/SOO#SOO_0000000008")
operates_on.python_name = 'operates_on'
