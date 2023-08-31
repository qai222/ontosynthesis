# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.1.7.4](https://github.com/so1n/protobuf_to_pydantic)
import typing
from enum import IntEnum

from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel, Field, root_validator


class DateTime(BaseModel):
    value: str = Field(default="")


class Data(BaseModel):
    _one_of_dict = {"Data.kind": {"fields": {"bytes_value", "float_value", "integer_value", "string_value", "url"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    float_value: float = Field(default=0.0)
    integer_value: int = Field(default=0)
    bytes_value: bytes = Field(default=b"")
    string_value: str = Field(default="")
    url: str = Field(default="")
    description: str = Field(default="")
    format: str = Field(default="")


class Analysis(BaseModel):
    class AnalysisType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        LC = 2
        GC = 3
        IR = 4
        NMR_1H = 5
        NMR_13C = 6
        NMR_OTHER = 7
        MP = 8
        UV = 9
        TLC = 10
        MS = 11
        HRMS = 12
        MSMS = 13
        WEIGHT = 14
        LCMS = 15
        GCMS = 16
        ELSD = 17
        CD = 18
        SFC = 19
        EPR = 20
        XRD = 21
        RAMAN = 22
        ED = 23

    _one_of_dict = {"Analysis._is_of_isolated_species": {"fields": {"is_of_isolated_species"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    type: AnalysisType = Field(default=0)
    details: str = Field(default="")
    chmo_id: int = Field(default=0)
    is_of_isolated_species: bool = Field(default=False)
    data: typing.Dict[str, Data] = Field(default_factory=dict)
    instrument_manufacturer: str = Field(default="")
    instrument_last_calibrated: DateTime = Field()


class ReactionRole(BaseModel):
    class ReactionRoleType(IntEnum):
        UNSPECIFIED = 0
        REACTANT = 1
        REAGENT = 2
        SOLVENT = 3
        CATALYST = 4
        WORKUP = 5
        INTERNAL_STANDARD = 6
        AUTHENTIC_STANDARD = 7
        PRODUCT = 8
        BYPRODUCT = 9
        SIDE_PRODUCT = 10


class ReactionIdentifier(BaseModel):
    class ReactionIdentifierType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        REACTION_SMILES = 2
        REACTION_CXSMILES = 6
        RDFILE = 3
        RINCHI = 4
        REACTION_TYPE = 5

    _one_of_dict = {"ReactionIdentifier._is_mapped": {"fields": {"is_mapped"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    type: ReactionIdentifierType = Field(default=0)
    details: str = Field(default="")
    value: str = Field(default="")
    is_mapped: bool = Field(default=False)


class VesselMaterial(BaseModel):
    class VesselMaterialType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        GLASS = 2
        POLYPROPYLENE = 3
        PLASTIC = 4
        METAL = 5
        QUARTZ = 6

    type: VesselMaterialType = Field(default=0)
    details: str = Field(default="")


class VesselPreparation(BaseModel):
    class VesselPreparationType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        NONE = 2
        OVEN_DRIED = 3
        FLAME_DRIED = 4
        EVACUATED_BACKFILLED = 5
        PURGED = 6

    type: VesselPreparationType = Field(default=0)
    details: str = Field(default="")


class VesselAttachment(BaseModel):
    class VesselAttachmentType(IntEnum):
        UNSPECIFIED = 0
        NONE = 1
        CUSTOM = 2
        SEPTUM = 3
        CAP = 4
        MAT = 5
        REFLUX_CONDENSER = 6
        VENT_NEEDLE = 7
        DEAN_STARK = 8
        VACUUM_TUBE = 9
        ADDITION_FUNNEL = 10
        DRYING_TUBE = 11
        ALUMINUM_FOIL = 12
        THERMOCOUPLE = 13
        BALLOON = 14
        GAS_ADAPTER = 15
        PRESSURE_REGULATOR = 16
        RELEASE_VALVE = 17

    type: VesselAttachmentType = Field(default=0)
    details: str = Field(default="")


class Volume(BaseModel):
    class VolumeUnit(IntEnum):
        UNSPECIFIED = 0
        LITER = 1
        MILLILITER = 2
        MICROLITER = 3
        NANOLITER = 4

    _one_of_dict = {"Volume._precision": {"fields": {"precision"}}, "Volume._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: VolumeUnit = Field(default=0)


class Vessel(BaseModel):
    class VesselType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        ROUND_BOTTOM_FLASK = 2
        VIAL = 3
        WELL_PLATE = 4
        MICROWAVE_VIAL = 5
        TUBE = 6
        CONTINUOUS_STIRRED_TANK_REACTOR = 7
        PACKED_BED_REACTOR = 8
        NMR_TUBE = 9
        PRESSURE_FLASK = 10
        PRESSURE_REACTOR = 11
        ELECTROCHEMICAL_CELL = 12

    type: VesselType = Field(default=0)
    details: str = Field(default="")
    material: VesselMaterial = Field()
    preparations: typing.List[VesselPreparation] = Field(default_factory=list)
    attachments: typing.List[VesselAttachment] = Field(default_factory=list)
    volume: Volume = Field()
    vessel_id: str = Field(default="")
    position: str = Field(default="")
    row: str = Field(default="")
    col: str = Field(default="")


class ReactionSetup(BaseModel):
    class ReactionEnvironment(BaseModel):
        class ReactionEnvironmentType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            FUME_HOOD = 2
            BENCH_TOP = 3
            GLOVE_BOX = 4
            GLOVE_BAG = 5

        type: ReactionEnvironmentType = Field(default=0)
        details: str = Field(default="")

    _one_of_dict = {"ReactionSetup._is_automated": {"fields": {"is_automated"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    vessel: Vessel = Field()
    is_automated: bool = Field(default=False)
    automation_platform: str = Field(default="")
    automation_code: typing.Dict[str, Data] = Field(default_factory=dict)
    environment: ReactionEnvironment = Field()


class Temperature(BaseModel):
    class TemperatureUnit(IntEnum):
        UNSPECIFIED = 0
        CELSIUS = 1
        FAHRENHEIT = 2
        KELVIN = 3

    _one_of_dict = {"Temperature._precision": {"fields": {"precision"}}, "Temperature._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: TemperatureUnit = Field(default=0)


class Time(BaseModel):
    class TimeUnit(IntEnum):
        UNSPECIFIED = 0
        DAY = 4
        HOUR = 1
        MINUTE = 2
        SECOND = 3

    _one_of_dict = {"Time._precision": {"fields": {"precision"}}, "Time._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: TimeUnit = Field(default=0)


class TemperatureConditions(BaseModel):
    class TemperatureControl(BaseModel):
        class TemperatureControlType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            AMBIENT = 2
            OIL_BATH = 3
            WATER_BATH = 4
            SAND_BATH = 5
            ICE_BATH = 6
            DRY_ALUMINUM_PLATE = 7
            MICROWAVE = 8
            DRY_ICE_BATH = 9
            AIR_FAN = 10
            LIQUID_NITROGEN = 11

        type: TemperatureControlType = Field(default=0)
        details: str = Field(default="")

    class TemperatureMeasurement(BaseModel):
        class TemperatureMeasurementType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            THERMOCOUPLE_INTERNAL = 2
            THERMOCOUPLE_EXTERNAL = 3
            INFRARED = 4

        type: TemperatureMeasurementType = Field(default=0)
        details: str = Field(default="")
        time: Time = Field()
        temperature: Temperature = Field()

    control: TemperatureControl = Field()
    setpoint: Temperature = Field()
    measurements: typing.List[TemperatureMeasurement] = Field(default_factory=list)


class Pressure(BaseModel):
    class PressureUnit(IntEnum):
        UNSPECIFIED = 0
        BAR = 1
        ATMOSPHERE = 2
        PSI = 3
        KPSI = 4
        PASCAL = 5
        KILOPASCAL = 6
        TORR = 7
        MM_HG = 8

    _one_of_dict = {"Pressure._precision": {"fields": {"precision"}}, "Pressure._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: PressureUnit = Field(default=0)


class PressureConditions(BaseModel):
    class PressureControl(BaseModel):
        class PressureControlType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            AMBIENT = 2
            SLIGHT_POSITIVE = 3
            SEALED = 4
            PRESSURIZED = 5

        type: PressureControlType = Field(default=0)
        details: str = Field(default="")

    class Atmosphere(BaseModel):
        class AtmosphereType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            AIR = 2
            NITROGEN = 3
            ARGON = 4
            OXYGEN = 5
            HYDROGEN = 6
            CARBON_MONOXIDE = 7
            CARBON_DIOXIDE = 8
            METHANE = 9
            AMMONIA = 10
            OZONE = 11
            ETHYLENE = 12
            ACETYLENE = 13

        type: AtmosphereType = Field(default=0)
        details: str = Field(default="")

    class PressureMeasurement(BaseModel):
        class PressureMeasurementType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            PRESSURE_TRANSDUCER = 2

        type: PressureMeasurementType = Field(default=0)
        details: str = Field(default="")
        time: Time = Field()
        pressure: Pressure = Field()

    control: PressureControl = Field()
    setpoint: Pressure = Field()
    atmosphere: Atmosphere = Field()
    measurements: typing.List[PressureMeasurement] = Field(default_factory=list)


class StirringConditions(BaseModel):
    class StirringRate(BaseModel):
        class StirringRateType(IntEnum):
            UNSPECIFIED = 0
            HIGH = 1
            MEDIUM = 2
            LOW = 3

        type: StirringRateType = Field(default=0)
        details: str = Field(default="")
        rpm: int = Field(default=0)

    class StirringMethodType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        NONE = 2
        STIR_BAR = 3
        OVERHEAD_MIXER = 4
        AGITATION = 5
        BALL_MILLING = 6
        SONICATION = 7

    type: StirringMethodType = Field(default=0)
    details: str = Field(default="")
    rate: StirringRate = Field()


class Wavelength(BaseModel):
    class WavelengthUnit(IntEnum):
        UNSPECIFIED = 0
        NANOMETER = 1
        WAVENUMBER = 2

    _one_of_dict = {"Wavelength._precision": {"fields": {"precision"}}, "Wavelength._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: WavelengthUnit = Field(default=0)


class Length(BaseModel):
    class LengthUnit(IntEnum):
        UNSPECIFIED = 0
        CENTIMETER = 1
        MILLIMETER = 2
        METER = 3
        INCH = 4
        FOOT = 5

    _one_of_dict = {"Length._precision": {"fields": {"precision"}}, "Length._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: LengthUnit = Field(default=0)


class IlluminationConditions(BaseModel):
    class IlluminationType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        AMBIENT = 2
        DARK = 3
        LED = 4
        HALOGEN_LAMP = 5
        DEUTERIUM_LAMP = 6
        SOLAR_SIMULATOR = 7
        BROAD_SPECTRUM = 8

    type: IlluminationType = Field(default=0)
    details: str = Field(default="")
    peak_wavelength: Wavelength = Field()
    color: str = Field(default="")
    distance_to_vessel: Length = Field()


class Current(BaseModel):
    class CurrentUnit(IntEnum):
        UNSPECIFIED = 0
        AMPERE = 1
        MILLIAMPERE = 2

    _one_of_dict = {"Current._precision": {"fields": {"precision"}}, "Current._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: CurrentUnit = Field(default=0)


class Voltage(BaseModel):
    class VoltageUnit(IntEnum):
        UNSPECIFIED = 0
        VOLT = 1
        MILLIVOLT = 2

    _one_of_dict = {"Voltage._precision": {"fields": {"precision"}}, "Voltage._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: VoltageUnit = Field(default=0)


class ElectrochemistryConditions(BaseModel):
    class ElectrochemistryMeasurement(BaseModel):
        time: Time = Field()
        current: Current = Field()
        voltage: Voltage = Field()

    class ElectrochemistryCell(BaseModel):
        class ElectrochemistryCellType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            DIVIDED_CELL = 2
            UNDIVIDED_CELL = 3

        type: ElectrochemistryCellType = Field(default=0)
        details: str = Field(default="")

    class ElectrochemistryType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        CONSTANT_CURRENT = 2
        CONSTANT_VOLTAGE = 3

    type: ElectrochemistryType = Field(default=0)
    details: str = Field(default="")
    current: Current = Field()
    voltage: Voltage = Field()
    anode_material: str = Field(default="")
    cathode_material: str = Field(default="")
    electrode_separation: Length = Field()
    measurements: typing.List[ElectrochemistryMeasurement] = Field(default_factory=list)
    cell: ElectrochemistryCell = Field()


class FlowConditions(BaseModel):
    class Tubing(BaseModel):
        class TubingType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            STEEL = 2
            COPPER = 3
            PFA = 4
            FEP = 5
            TEFLONAF = 6
            PTFE = 7
            GLASS = 8
            QUARTZ = 9
            SILICON = 10
            PDMS = 11

        type: TubingType = Field(default=0)
        details: str = Field(default="")
        diameter: Length = Field()

    class FlowType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        PLUG_FLOW_REACTOR = 2
        CONTINUOUS_STIRRED_TANK_REACTOR = 3
        PACKED_BED_REACTOR = 4

    type: FlowType = Field(default=0)
    details: str = Field(default="")
    pump_type: str = Field(default="")
    tubing: Tubing = Field()


class ReactionConditions(BaseModel):
    _one_of_dict = {"ReactionConditions._conditions_are_dynamic": {"fields": {"conditions_are_dynamic"}},
                    "ReactionConditions._ph": {"fields": {"ph"}}, "ReactionConditions._reflux": {"fields": {"reflux"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    temperature: TemperatureConditions = Field()
    pressure: PressureConditions = Field()
    stirring: StirringConditions = Field()
    illumination: IlluminationConditions = Field()
    electrochemistry: ElectrochemistryConditions = Field()
    flow: FlowConditions = Field()
    reflux: bool = Field(default=False)
    ph: float = Field(default=0.0)
    conditions_are_dynamic: bool = Field(default=False)
    details: str = Field(default="")


class ReactionNotes(BaseModel):
    _one_of_dict = {"ReactionNotes._forms_precipitate": {"fields": {"forms_precipitate"}},
                    "ReactionNotes._is_exothermic": {"fields": {"is_exothermic"}},
                    "ReactionNotes._is_heterogeneous": {"fields": {"is_heterogeneous"}},
                    "ReactionNotes._is_sensitive_to_light": {"fields": {"is_sensitive_to_light"}},
                    "ReactionNotes._is_sensitive_to_moisture": {"fields": {"is_sensitive_to_moisture"}},
                    "ReactionNotes._is_sensitive_to_oxygen": {"fields": {"is_sensitive_to_oxygen"}},
                    "ReactionNotes._offgasses": {"fields": {"offgasses"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    is_heterogeneous: bool = Field(default=False)
    forms_precipitate: bool = Field(default=False)
    is_exothermic: bool = Field(default=False)
    offgasses: bool = Field(default=False)
    is_sensitive_to_moisture: bool = Field(default=False)
    is_sensitive_to_oxygen: bool = Field(default=False)
    is_sensitive_to_light: bool = Field(default=False)
    safety_notes: str = Field(default="")
    procedure_details: str = Field(default="")


class ReactionObservation(BaseModel):
    time: Time = Field()
    comment: str = Field(default="")
    image: Data = Field()


class CompoundIdentifier(BaseModel):
    class CompoundIdentifierType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        SMILES = 2
        INCHI = 3
        MOLBLOCK = 4
        IUPAC_NAME = 5
        NAME = 6
        CAS_NUMBER = 7
        PUBCHEM_CID = 8
        CHEMSPIDER_ID = 9
        CXSMILES = 10
        INCHI_KEY = 11
        XYZ = 12
        UNIPROT_ID = 13
        PDB_ID = 14
        AMINO_ACID_SEQUENCE = 15
        HELM = 16

    type: CompoundIdentifierType = Field(default=0)
    details: str = Field(default="")
    value: str = Field(default="")


class Mass(BaseModel):
    class MassUnit(IntEnum):
        UNSPECIFIED = 0
        KILOGRAM = 1
        GRAM = 2
        MILLIGRAM = 3
        MICROGRAM = 4

    _one_of_dict = {"Mass._precision": {"fields": {"precision"}}, "Mass._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: MassUnit = Field(default=0)


class Moles(BaseModel):
    class MolesUnit(IntEnum):
        UNSPECIFIED = 0
        MOLE = 1
        MILLIMOLE = 2
        MICROMOLE = 3
        NANOMOLE = 4

    _one_of_dict = {"Moles._precision": {"fields": {"precision"}}, "Moles._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: MolesUnit = Field(default=0)


class UnmeasuredAmount(BaseModel):
    class UnmeasuredAmountType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        SATURATED = 2
        CATALYTIC = 3
        TITRATED = 4

    type: UnmeasuredAmountType = Field(default=0)
    details: str = Field(default="")


class Amount(BaseModel):
    _one_of_dict = {"Amount._volume_includes_solutes": {"fields": {"volume_includes_solutes"}},
                    "Amount.kind": {"fields": {"mass", "moles", "unmeasured", "volume"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    mass: Mass = Field()
    moles: Moles = Field()
    volume: Volume = Field()
    unmeasured: UnmeasuredAmount = Field()
    volume_includes_solutes: bool = Field(default=False)


class CompoundPreparation(BaseModel):
    class CompoundPreparationType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        NONE = 2
        REPURIFIED = 3
        SPARGED = 4
        DRIED = 5
        SYNTHESIZED = 6

    type: CompoundPreparationType = Field(default=0)
    details: str = Field(default="")
    reaction_id: str = Field(default="")


class Compound(BaseModel):
    class Source(BaseModel):
        vendor: str = Field(default="")
        catalog_id: str = Field(default="")
        lot: str = Field(default="")

    _one_of_dict = {"Compound._is_limiting": {"fields": {"is_limiting"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    identifiers: typing.List[CompoundIdentifier] = Field(default_factory=list)
    amount: Amount = Field()
    reaction_role: ReactionRole.ReactionRoleType = Field(default=0)
    is_limiting: bool = Field(default=False)
    preparations: typing.List[CompoundPreparation] = Field(default_factory=list)
    source: Source = Field()
    features: typing.Dict[str, Data] = Field(default_factory=dict)
    analyses: typing.Dict[str, Analysis] = Field(default_factory=dict)


class CrudeComponent(BaseModel):
    _one_of_dict = {"CrudeComponent._has_derived_amount": {"fields": {"has_derived_amount"}},
                    "CrudeComponent._includes_workup": {"fields": {"includes_workup"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    reaction_id: str = Field(default="")
    includes_workup: bool = Field(default=False)
    has_derived_amount: bool = Field(default=False)
    amount: Amount = Field()


class FlowRate(BaseModel):
    class FlowRateUnit(IntEnum):
        UNSPECIFIED = 0
        MICROLITER_PER_MINUTE = 1
        MICROLITER_PER_SECOND = 2
        MILLILITER_PER_MINUTE = 3
        MILLILITER_PER_SECOND = 4
        MICROLITER_PER_HOUR = 5

    _one_of_dict = {"FlowRate._precision": {"fields": {"precision"}}, "FlowRate._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: FlowRateUnit = Field(default=0)


class ReactionInput(BaseModel):
    class AdditionSpeed(BaseModel):
        class AdditionSpeedType(IntEnum):
            UNSPECIFIED = 0
            ALL_AT_ONCE = 1
            FAST = 2
            SLOW = 3
            DROPWISE = 4
            CONTINUOUS = 5
            PORTIONWISE = 6

        type: AdditionSpeedType = Field(default=0)
        details: str = Field(default="")

    class AdditionDevice(BaseModel):
        class AdditionDeviceType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            NONE = 2
            SYRINGE = 3
            CANNULA = 4
            ADDITION_FUNNEL = 5

        type: AdditionDeviceType = Field(default=0)
        details: str = Field(default="")

    components: typing.List[Compound] = Field(default_factory=list)
    crude_components: typing.List[CrudeComponent] = Field(default_factory=list)
    addition_order: int = Field(default=0)
    addition_time: Time = Field()
    addition_speed: AdditionSpeed = Field()
    addition_duration: Time = Field()
    flow_rate: FlowRate = Field()
    addition_device: AdditionDevice = Field()
    addition_temperature: Temperature = Field()


class ReactionWorkup(BaseModel):
    class ReactionWorkupType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        ADDITION = 2
        ALIQUOT = 3
        TEMPERATURE = 4
        CONCENTRATION = 5
        EXTRACTION = 6
        FILTRATION = 7
        WASH = 8
        DRY_IN_VACUUM = 9
        DRY_WITH_MATERIAL = 10
        FLASH_CHROMATOGRAPHY = 11
        OTHER_CHROMATOGRAPHY = 12
        SCAVENGING = 13
        WAIT = 14
        STIRRING = 15
        PH_ADJUST = 16
        DISSOLUTION = 17
        DISTILLATION = 18

    _one_of_dict = {"ReactionWorkup._is_automated": {"fields": {"is_automated"}},
                    "ReactionWorkup._target_ph": {"fields": {"target_ph"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    type: ReactionWorkupType = Field(default=0)
    details: str = Field(default="")
    duration: Time = Field()
    input: ReactionInput = Field()
    amount: Amount = Field()
    temperature: TemperatureConditions = Field()
    keep_phase: str = Field(default="")
    stirring: StirringConditions = Field()
    target_ph: float = Field(default=0.0)
    is_automated: bool = Field(default=False)


class Percentage(BaseModel):
    _one_of_dict = {"Percentage._precision": {"fields": {"precision"}}, "Percentage._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)


class FloatValue(BaseModel):
    _one_of_dict = {"FloatValue._precision": {"fields": {"precision"}}, "FloatValue._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)


class ProductMeasurement(BaseModel):
    class MassSpecMeasurementDetails(BaseModel):
        class MassSpecMeasurementType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            TIC = 2
            TIC_POSITIVE = 3
            TIC_NEGATIVE = 4
            EIC = 5

        _one_of_dict = {"MassSpecMeasurementDetails._tic_maximum_mz": {"fields": {"tic_maximum_mz"}},
                        "MassSpecMeasurementDetails._tic_minimum_mz": {"fields": {"tic_minimum_mz"}}}
        _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

        type: MassSpecMeasurementType = Field(default=0)
        details: str = Field(default="")
        tic_minimum_mz: float = Field(default=0.0)
        tic_maximum_mz: float = Field(default=0.0)
        eic_masses: typing.List[float] = Field(default_factory=list)

    class Selectivity(BaseModel):
        class SelectivityType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            EE = 2
            ER = 3
            DR = 4
            EZ = 5
            ZE = 6

        type: SelectivityType = Field(default=0)
        details: str = Field(default="")

    class ProductMeasurementType(IntEnum):
        UNSPECIFIED = 0
        CUSTOM = 1
        IDENTITY = 2
        YIELD = 3
        SELECTIVITY = 4
        PURITY = 5
        AREA = 6
        COUNTS = 7
        INTENSITY = 8
        AMOUNT = 9

    _one_of_dict = {"ProductMeasurement._is_normalized": {"fields": {"is_normalized"}},
                    "ProductMeasurement._uses_authentic_standard": {"fields": {"uses_authentic_standard"}},
                    "ProductMeasurement._uses_internal_standard": {"fields": {"uses_internal_standard"}},
                    "ProductMeasurement.value": {"fields": {"amount", "float_value", "percentage", "string_value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    analysis_key: str = Field(default="")
    type: ProductMeasurementType = Field(default=0)
    details: str = Field(default="")
    uses_internal_standard: bool = Field(default=False)
    is_normalized: bool = Field(default=False)
    uses_authentic_standard: bool = Field(default=False)
    authentic_standard: Compound = Field()
    percentage: Percentage = Field()
    float_value: FloatValue = Field()
    string_value: str = Field(default="")
    amount: Amount = Field()
    retention_time: Time = Field()
    mass_spec_details: MassSpecMeasurementDetails = Field()
    selectivity: Selectivity = Field()
    wavelength: Wavelength = Field()


class ProductCompound(BaseModel):
    class Texture(BaseModel):
        class TextureType(IntEnum):
            UNSPECIFIED = 0
            CUSTOM = 1
            POWDER = 2
            CRYSTAL = 3
            OIL = 4
            AMORPHOUS_SOLID = 5
            FOAM = 6
            WAX = 7
            SEMI_SOLID = 8
            SOLID = 9
            LIQUID = 10

        type: TextureType = Field(default=0)
        details: str = Field(default="")

    _one_of_dict = {"ProductCompound._is_desired_product": {"fields": {"is_desired_product"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    identifiers: typing.List[CompoundIdentifier] = Field(default_factory=list)
    is_desired_product: bool = Field(default=False)
    measurements: typing.List[ProductMeasurement] = Field(default_factory=list)
    isolated_color: str = Field(default="")
    texture: Texture = Field()
    features: typing.Dict[str, Data] = Field(default_factory=dict)
    reaction_role: ReactionRole.ReactionRoleType = Field(default=0)


class ReactionOutcome(BaseModel):
    reaction_time: Time = Field()
    conversion: Percentage = Field()
    products: typing.List[ProductCompound] = Field(default_factory=list)
    analyses: typing.Dict[str, Analysis] = Field(default_factory=dict)


class Person(BaseModel):
    username: str = Field(default="")
    name: str = Field(default="")
    orcid: str = Field(default="")
    organization: str = Field(default="")
    email: str = Field(default="")


class RecordEvent(BaseModel):
    time: DateTime = Field()
    person: Person = Field()
    details: str = Field(default="")


class ReactionProvenance(BaseModel):
    _one_of_dict = {"ReactionProvenance._is_mined": {"fields": {"is_mined"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    experimenter: Person = Field()
    city: str = Field(default="")
    experiment_start: DateTime = Field()
    doi: str = Field(default="")
    patent: str = Field(default="")
    publication_url: str = Field(default="")
    record_created: RecordEvent = Field()
    record_modified: typing.List[RecordEvent] = Field(default_factory=list)
    reaction_metadata: typing.Dict[str, Data] = Field(default_factory=dict)
    is_mined: bool = Field(default=False)


class Reaction(BaseModel):
    identifiers: typing.List[ReactionIdentifier] = Field(default_factory=list)
    inputs: typing.Dict[str, ReactionInput] = Field(default_factory=dict)
    setup: ReactionSetup = Field()
    conditions: ReactionConditions = Field()
    notes: ReactionNotes = Field()
    observations: typing.List[ReactionObservation] = Field(default_factory=list)
    workups: typing.List[ReactionWorkup] = Field(default_factory=list)
    outcomes: typing.List[ReactionOutcome] = Field(default_factory=list)
    provenance: ReactionProvenance = Field()
    reaction_id: str = Field(default="")


class Concentration(BaseModel):
    class ConcentrationUnit(IntEnum):
        UNSPECIFIED = 0
        MOLAR = 1
        MILLIMOLAR = 2
        MICROMOLAR = 3

    _one_of_dict = {"Concentration._precision": {"fields": {"precision"}},
                    "Concentration._value": {"fields": {"value"}}}
    _check_one_of = root_validator(pre=True, allow_reuse=True)(check_one_of)

    value: float = Field(default=0.0)
    precision: float = Field(default=0.0)
    units: ConcentrationUnit = Field(default=0)
