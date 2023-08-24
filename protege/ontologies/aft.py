
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
Range = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000021")
# A range is an interval of values with a lower and/or upper limit. [Allotrope]
    
Codelist = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000036")
# A set of codes in a controlled vocabulary. [Allotrope]
    
Code = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000050")
# An entry in a list of controlled symbols denoting a classification. [Allotrope]
    
Condition = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000090")
# A condition is an information content entity that is about the portion of reality under which something occurs or is valid. The condition is limited by its scope and may have preconditions. It restricts the possible realizations. [Allotrope]
    
AndCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000091")
# An and condition is a collection of conditions that is valid if all condition items of it are valid. [Allotrope]
    
OrCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000092")
# An or condition is a collection of conditions that is valid if at least one of its condition items is valid. [Allotrope]
    
OneOfCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000093")
# A one of condition is a collection of conditions that is valid if exactly one of its condition items is valid. [Allotrope]
    
List = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000160")
# A list is an ordered collection of items. [Allotrope]
    
ListItem = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000161")
# An entry in a list. [Allotrope]
    
Series = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000162")
# A series is a list (ordered collection) of literal values. [Allotrope]
    
SeriesItem = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000163")
# An individual entry in a series with an index and a numeric value. [Allotrope]
    
Collection = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000166")
# An aggregation of data items for a purpose. [Allotrope]
    
Item = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000167")
# An item is an individual member of some collection. [Allotrope]
    
Set = onto.search_one(iri="http://purl.allotrope.org/ontologies/common#AFC_0000168")
# A collection where each member is disjoint from another. [Allotrope]
    
IonSource = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000004")
# A ion source is a device that has the function to produce or provide ions. [Allotrope]
    
SamplePassage = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000022")
# A sample passage is the compartment of a device that handles the conveying of samples. [Allotrope]
    
Calorimeter = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000023")
# A piece of apparatus that is used to measure the heat of chemical reactions or physical changes. [CHMO]
    
GasChromatograph = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000024")
# A piece of apparatus, consisting of a gas supply system, an injection or sampling system, a column, detector and a data acquisition/processing system, that is used to carry out chromatographic separations. [CHMO]
    
WellPlate = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000029")
# A plate is a tray with multiple &quot;wells&quot; used as small test tubes. [Wikipedia]
    
BarcodeReader = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000040")
# A barcode reader (or barcode scanner) is an electronic device for reading printed barcodes. [Wikipedia]
    
Autosampler = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000073")
# A piece of equipment that allows for automated sampling or sample loading. [Allotrope]
    
ElectrochemicalCoulometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000085")
# A piece of apparatus, consisting of an electrolytic cell, that is used to determine electric charge by measuring the amount of an element deposited or released at the cathode during a specified time. [Allotrope]
    
FractionCollector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000088")
# A fraction collector is a collecting device for recovering fractional volumes of the column effluent. [IUPAC]
    
ElectromagneticRadiationSource = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000097")
# A source of a range of electromagnetic waves. [Allotrope]
    
FlowCell = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000105")
# A flow cell is a measurement chamber that allows the sample to flow through. [Allotrope]
    
OpticalMicroscope = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000129")
# An optical microscope is a microscope that is consisting of an eyepiece, an objective lens, object turret, stage, and light source, which collects electromagnetic radiation in the visible range. [CHMO]
    
Channel_communication = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000145")
# A communication channel or channel, refers either to a physical transmission medium such as a wire, or to a logical connection over a multiplexed medium such as a radio channel. A channel is used to convey an information signal, for example a digital bit stream, from one or several senders (or transmitters) to one or several receivers. [Wikipedia]
    
Spectrophotometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000185")
# A spectrophotometer is a photometer that measures the intensity of light at each individual wavelength. [Allotrope]
    
FlameIonizationDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000209")
# A flame ionization detector is a measurement component that measures an analyte in a gas stream through the measurement of ions created via flame ionization. [Allotrope]
    
ChromatographyColumn = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000217")
# A chromatography column is a type of column that contains a stationary phase for chromatographic separation of compounds. [Allotrope]
    
WeighingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000252")
# A weighing device is a measurement device for measuring mass by the gravitational force on earth. [Allotrope]
    
InjectionDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000266")
# A device that introduces objects into the inside of another object. [Allotrope]
    
Homogenizer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000299")
# A homogenizer is a device used for homogenization of various types of material. [Wikipedia]
    
ThermalConductivityDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000316")
# A thermal conductivity detector is a measurement component that measures changes in the thermal conductivity of the column effluent and compares it to a reference flow of carrier gas. [Allotrope]
    
Detector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000317")
# Any piece of apparatus used to detect an analyte. [CHMO]
    
Compartment = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000322")
# A separate enclosed physical section of a device that can contain other devices. [Allotrope]
    
Capillary = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000340")
# A capillary is a tube with a small diameter. [Allotrope]
    
Device = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000354")
# A device is an artifact that is designed to perform a function primarily by means of its mechanical or electrical nature. [Allotrope]
    
RefractiveIndexDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000363")
# A piece of apparatus, consisting of a light source, a hollow prism and a photoelectric cell that is used to detect non-ultraviolet-absorbing molecules in a sample separated by chromatography. Light from the sample passes through a flow cell with two channels towards the photoelectric cell. One channel holds the eluent from the column, whereas the other holds a control sample (solvent that has not passed through the column).  Detection occurs when the light is bent due to molecules eluting from the column, and this is read as a disparity between the two channels. [CHMO]
    
ElectrolyticConductivityDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000368")
# A conductivity probe to calculate the conductance value of a material at the selected reference temperature. [Allotrope]
    
Chromatograph = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000392")
# A piece of apparatus, consisting of a mobile phase supply system, an injection or sampling system, a column, detector and a data acquisition/processing system, that is used to carry out chromatographic separations. [CHMO]
    
Container = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000407")
# A device that has the function to contain material. [Allotrope]
    
Thermometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000410")
# A thermometer is a device that measures temperature or a temperature gradient. [Allotrope]
    
Electrode = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000422")
# An electrode is an electrically-conducting device that exchanges electrons with an electrolyte as part of an electrical circuit. [Allotrope]
    
Damper = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000471")
# A damper is an inhibition device that deadens, restrains, or depresses. [Wikipedia]
    
Pump = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000499")
# A pump is a device that is used to pump. [CHMO]
    
TemperatureController = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000528")
# A device used to control the temperature in a compartment. [Allotrope]
    
ElectronCaptureDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000534")
# An electron capture detector is a measurement component that measures an analyte in a gas stream through the attachment of electrons via electron capture ionization. [Allotrope]
    
VialRack = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000540")
# A vial rack is a tray capable of holding multiple vials within a defined layout. [Allotrope]
    
RamanSpectrometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000551")
# A Raman spectrometer is a piece of apparatus that allows for the measurement of Raman spectra. It consists of a laser and a detector. [Allotrope]
    
DataAcquisitionDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000555")
# A device to acquire signals or data. [Allotrope]
    
Splitter = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000558")
# A device used to split a fluid into two component streams. [Allotrope]
    
FluorescenceDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000567")
# A fluorescence detector is a detector that detects material by way of the measurement of the emitted fluorescence light after excitation with light. [Allotrope]
    
Degasser = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000587")
# A degasser is a device to remove gasses from a fluid which could otherwise form bubbles. [Wikipedia]
    
IonDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000642")
# A piece of apparatus that produces an output that depends on the number of ions that it encounters. [CHMO]
    
MeasurementChamber = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000646")
# A measurement chamber is a closed space that contains the sample for measurement. [Allotrope]
    
MassSpectrometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000648")
# A mass spectrometer is a measurement device that measures the m/z values and abundances of gas-phase ions. [IUPAC]
    
Balance = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000693")
# A balance is a weighing device, intended predominantly for medium to low capacity weighments, with moderate to high resolutions, mostly used indoors. [Allotrope]
    
Tube = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000718")
# A tube, or tubing, is a long hollow cylinder used for moving fluids (liquids or gases) or to protect electrical or optical cables and wires. [Wikipedia]
    
ElectronicAbsorbanceDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000734")
# An electronic absorbance detector is a  detector that detects material by way of the electronic absorbance of a electromagnetic ray transmitted through the material. [Allotrope]
    
Syringe = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000746")
# A syringe is an injection device that is a simple pump consisting of a plunger that fits tightly in a tube. The plunger can be pulled and pushed along inside a cylindrical tube (called a barrel), allowing the syringe to take in and expel a liquid or gas through an orifice at the open end of the tube. [Wikipedia]
    
Display = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000761")
# A display is a device or element of an instrument serving to represent information. [Allotrope]
    
CoolingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000785")
# A kind of heat exchanger or radiator designed to remove excess heat. [Wikipedia]
    
Valve = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000795")
# A valve is a plumbing equipment that regulates, directs or controls the flow of a fluid (gases, liquids, fluidized solids, or slurries) by opening, closing, or partially obstructing various passageways. [Wikipedia]
    
LiquidChromatograph = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000808")
# A liquid chromatograph is a system used to perform bioseparation techniques that are based on interactions of the sample with the mobile and stationary phases. [Allotrope]
    
Stirrer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000812")
# A stirrer is a mixing device used for stirring something. [Allotrope]
    
Oven = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000816")
# An oven is a device for heating an enclosed space. [Allotrope]
    
Microscope = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000825")
# A microscope is a device which is used to visually magnify a specimen. [Allotrope]
    
SolventChannel = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000828")
# A solvent channel is a channel where a liquid can flow through. [Allotrope]
    
Coulometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000855")
# Any piece of apparatus used to measure electric charge. [CHMO]
    
Titrator = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000876")
# A titrator is a device that automates titrations. [Allotrope]
    
Slit = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000986")
# A long narrow cut or opening. [Allotrope]
    
DeviceRegion = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001028")
# A site that is related to a device. [Allotrope]
    
Bath = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001121")
# A vessel used for regulating the temperature of something placed within it. [Allotrope]
    
HeatingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001128")
# A device used for heating something. [Allotrope]
    
Agitator = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001265")
# An agitator is a device or mechanism to put something into motion. [Wikipedia]
    
Mixer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001266")
# A mixer is a device used for mixing. [Allotrope]
    
Jar = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001410")
# Jars are cylindrical containers with wide openings that may be sealed. [Wikipedia]
    
Photometer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001515")
# A photometer, generally, is an instrument that measures light intensity or optical properties of solutions or surfaces. [Wikipedia]
    
Pan = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001623")
# A pan is a flat container. [Allotrope]
    
MassFlowController = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001671")
# A mass flow controller is a device that determines the mixture of different materials. [Allotrope]
    
Computer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001695")
# A computer is a general-purpose device that can be programmed to carry out a set of arithmetic or logical operations automatically. Since a sequence of operations can be readily changed, the computer can solve more than one kind of problem. [Wikipedia]
    
Sampler = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001711")
# A sample is a device that function to sample known amounts of material. [Allotrope]
    
TubingConnector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001761")
# A tubing connector is a part used to connect/install tubing, components, and accessories as part of a system flow path configuration. [Allotrope]
    
VisibleLamp = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001771")
# A visible lamp is a light source with a visible wavelength range of 380 to 780 nm. [Allotrope]
    
Diode = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001860")
# In electronics, a diode is a two-terminal electronic component that conducts primarily in one direction (asymmetric conductance). [Wikipedia]
    
Lamp = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0001875")
# A lamp is an electromagnetic radiation source of incoherent radiation. [IUPAC]
    
Artifact = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002099")
# An artifact is a material that is designed and built for a purpose. [Allotrope]
    
MeasurementDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002145")
# A device that measures some aspect of reality, such as a quality or the profile of a process. [Allotrope]
    
Controller = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002148")
# A device that has the function to control some quality or process. [Allotrope]
    
CouplingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002151")
# A device that has the function to couple things. [Allotrope]
    
InputDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002156")
# A device that is used to provide data and control signals to an information processing system. [Wikipedia]
    
SeparationDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002157")
# A device that has the function to separate materials. [Allotrope]
    
TransferringDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002168")
# A transferring device is a device that is designed to transfer material. [Allotrope]
    
CollectingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002172")
# A collecting device is a device that has the function to collect things. [Allotrope]
    
MeasurementComponent = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002185")
# A measurement component is a component of a measuring system, that does measuring. [Allotrope]
    
GuidingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002189")
# A guiding device is a device that has the function to direct a flow in a specific direction. [Allotrope]
    
DistributionDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002193")
# A distribution device is a device with the function to distribute a stream into multiple parts. [Allotrope]
    
Clock = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002204")
# A clock is a measurement device used to measure, keep, and indicate time. [Wikipedia]
    
Bench = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002206")
# A bench is a large table in a workspace or laboratory. [Allotrope]
    
PlacementDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002209")
# A placement device is a device that is used to hold or place a material in a defined location. [Allotrope]
    
Table = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002210")
# A table is a placement device with a flat top and one or more legs, providing a level surface for placement. [Allotrope]
    
Multimeter = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002211")
# A multimeter is an instrument designed to measure electric current, voltage, and usually resistance, typically over several ranges of value. [Allotrope]
    
FrequencySynthesizer = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002212")
# A frequency generator is an electrical device which creates a signal at a predetermined frequency. [Allotrope]
    
Nozzle = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002222")
# A nozzle is a transferring device consisting of jet port with an opening for regulating and/or directing the flow of fluid. [Allotrope]
    
CoveringDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002225")
# A covering device is a device that has the function to cover something. [Allotrope]
    
Jacket = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002226")
# A jacket is a covering device that is placed around something. [Allotrope]
    
ConnectingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002227")
# A connecting device is a device that has the function to connect things. [Allotrope]
    
ShapingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002228")
# A shaping device is a conversion device that alters the shape of some material. [Allotrope]
    
ConversionDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002229")
# A conversion device is a device that has the function to convert something. [Allotrope]
    
Tray = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002231")
# A tray is a shallow, flat container. [Allotrope]
    
CommunicationDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002235")
# A communication device is a device that has the function to communicate (transport information). [Allotrope]
    
Beamsplitter = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002236")
# A beam splitter is an optical device that splits a beam of light in two. [Wikipedia]
    
Well_plate = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002241")
# A well (plate) is a well located in a well plate. [Allotrope]
    
ObservationDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002242")
# An observation device is a device that has the function to observe something. [Allotrope]
    
RadiationSource = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002250")
# A radiation source is a device that produces radiation used in a process. [Allotrope]
    
Aperture = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002252")
# An aperture is an inhibition device that is a small opening with the function of limiting the passage of matter or energy. [Allotrope]
    
InhibitionDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002254")
# An inhibition device is a device that has the function to inhibit flows (material, energy, information). A part of the flow is passing through the device. [Allotrope]
    
CompressionDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002256")
# A compression device is a device that is designed to compress to volume of material by applying force. [Allotrope]
    
Basket = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002259")
# A basket is a container with a mesh structure used to hold solid objects. [Allotrope]
    
Lens = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002261")
# A lens is a guiding device with the function to converge or focus some radiation. [Allotrope]
    
CondenserLens = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002262")
# A condenser lens is a lens with the function to converge a radiation beam to a defined beam size. [Allotrope]
    
DisconnectingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002263")
# A disconnecting device is a device that is designed to disconnect objects. [Allotrope]
    
DisintegrationDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002264")
# A disintegration device is a device that is designed to disintegrate objects. [Allotrope]
    
PlateHeater = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002267")
# A plate heater is a heating device that heats by means of a plate shaped heating element. [Allotrope]
    
ForceGauge = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002268")
# A force gauge is a measurement device used to measure forces. [Allotrope]
    
HeaterBar = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002269")
# A heater bar is a heating device that is long and thin. [Allotrope]
    
GrippingDevice = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002271")
# A gripping device is a device that takes holds of something firmly or tightly. [Allotrope]
    
NitrogenChemiluminescenceDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002274")
# A nitrogen chemiluminescence detector is a measurement component that measures an analyte in a gas stream through the detection of nitrogen chemiluminescence. [Allotrope]
    
SulfurChemiluminescenceDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002275")
# A sulfur chemiluminescence detector is a measurement component that measures an analyte in a gas stream through the detection of sulfur chemiluminescence when reacting with ozone. [Allotrope]
    
FlamePhotometricDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002276")
# A flame photometric detector is a measurement component that measures an analyte in a gas stream through the detection of chemiluminescence as a result of ignition. [Allotrope]
    
EvaporativeLightScatteringDetector = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002277")
# An evaporative light scattering detector is a detector that detects material by way of the measurement of the scattering of light after nebulization with an inert carrier gas and evaporation of the solvent. [Allotrope]
    
ToEquilibrate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000004")
# To equilibrate is a function which is realized in the process of equilibration. [Allotrope]
    
ToCalibrate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000006")
# To calibrate is a function to establish, under specified conditions, the relationship between values of quantities indicated by a measuring instrument, or measuring system, or values represented by a material measure or a reference material, and the corresponding values realized by standards. [IUPAC]
    
ToCollect = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000007")
# Function to add a member to an aggregate or to bring a flow together. [Allotrope]
    
ToConnect = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000008")
# To bring two or more flows (material, energy, signal) together. [NIST]
    
ToConsume = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000009")
# The to consume function is a function that is realized in a process where a participant exists at the start of the process but no longer exists at the end of the process. [Allotrope]
    
ToIndicate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000010")
# To make something known to the user about a flow. [NIST]
    
ToControl = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000014")
# To alter or govern the size or amplitude of a flow (material, energy, signal). [NIST]
    
ToSense = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000023")
# To sense is a signaling function that is perceiving or becoming aware, of a flow. [NIST]
    
ToSecure = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000024")
# To firmly fix a flow path. [NIST]
    
ToTransformData = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000025")
# To submit information to a particular treatment or method having a set number of operations or steps. [NIST]
    
ToIntegrate_math = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000026")
# A information processing function that generates integrals on numerical data item. [Allotrope]
    
ToCalculate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000027")
# To calculate is a data transformation function to solve problems for numbers or quantities. [Allotrope]
    
ToSupport = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000028")
# To firmly fix a material into a defined location, or secure an energy or signal into a specific course. [NIST]
    
ToClean = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000029")
# The material processing function to get rid of dirt, impurities, or extraneous unwanted matter. [Allotrope]
    
ToInject = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000030")
# The function of a device realized when administering a substance applied particularly to the forcible insertion of a liquid or gas by means of a syringe, pump, etc. [OBI]
    
ToCount = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000036")
# To count is to observe the quantitative number of discrete things. [Allotrope]
    
ToDetect = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000037")
# To discover information about the presence of a flow. [NIST]
    
ToMeasure = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000041")
# To determine the magnitude of a flow. [NIST]
    
ToTransmitEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000043")
# To move an energy from one place to another. [NIST]
    
ToHeat = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000044")
# A function that gives thermal energy to a recipient. [Allotrope]
    
ToCommunicate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000045")
# To communicate is the function to transferring information from one material entity to another. [Allotrope]
    
ToPump = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000046")
# To pump is to transport fluids by suction or pressure or both. [Allotrope]
    
ToDisplay = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000052")
# To reveal something about a flow to the mind or eye. [NIST]
    
ToConvertASignal = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000053")
# A signal conversion function is an information processor function which transforms a signal into another type of signal. [OBI]
    
ToStore = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000055")
# To accumulate a flow. [NIST]
    
ToCool = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000089")
# A function to remove thermal energy. [Allotrope]
    
ToConsumeEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000093")
# To consume energy is the function to consume energy. [Allotrope]
    
ToPlan = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000103")
# To plan is the function of creating or modifying a plan specification. [OBI]
    
ToBranch = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000104")
# To cause a flow (material, energy or signal) to no longer be joined or mixed. [NIST]
    
ToSeparate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000105")
# To isolate a flow (material, energy, signal) into distinct components. The separated components are distinct from the flow before separation, as well as each other. [NIST]
    
ToDistribute = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000106")
# To cause a flow (material, energy, signal) to break up. The individual bits are similar to each other and the undistributed flow. [NIST]
    
ToDivide = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000107")
# To separate a flow. [NIST]
    
ToRemove = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000108")
# To take away a part of a flow from its prefixed place. [NIST]
    
ToExtract = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000109")
# To draw, or forcibly pullout, a flow. [NIST]
    
ToSort = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000110")
# A sort function is a function to distinguish flows based on some associated physical quality or entity and to distribute the separate components into distinct fractions according to a defined order. [Allotrope]
    
ToLocalize = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000111")
# To cause a flow (material, energy, signal) to move from one location to another location. [NIST]
    
ToExport = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000112")
# To send a flow (material, energy, signal) outside the system boundary. [NIST]
    
ToImport = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000113")
# To bring in a flow (material, energy, signal) from outside the system boundary. [NIST]
    
ToGuide = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000115")
# To direct the course of a flow (material, energy, signal) along a specific path. [NIST]
    
ToAllowDegreeOfFreedom = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000116")
# To control the movement of a flow by a force external to the device into one or more directions. [NIST]
    
ToRotate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000117")
# To fix the movement of a flow by a device around one axis. [NIST]
    
ToTranslate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000118")
# To fix the movement of the flow by a device into one linear direction. [NIST]
    
ToMix = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000119")
# To combine two flows (material, energy, signal) into a single, uniform homogeneous mass. [NIST]
    
ToCouple = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000120")
# To join or bring together flows (material, energy, signal) such that the members are still distinguishable from each other. [NIST]
    
ToLink = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000121")
# To couple flows together by means of an intermediary flow. [NIST]
    
ToJoin = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000122")
# To couple flows together in a predetermined manner. [NIST]
    
ToRegulate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000123")
# To adjust the flow of energy, signal, or material in response to a control signal, such as a characteristic of a flow. [NIST]
    
ToActuate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000124")
# To commence the flow of energy, signal or material in response to an imported control signal. [NIST]
    
ToIncrease = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000125")
# To enlarge a flow in response to a control signal. [NIST]
    
ToDecrease = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000126")
# To reduce a flow in response to a control signal. [NIST]
    
ToChange = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000127")
# To adjust the flow of energy, signal, or material in a predetermined and fixed manner. [NIST]
    
ToIncrement = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000128")
# To enlarge a  flow in a predetermined and fixed manner. [NIST]
    
ToDecrement = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000129")
# To reduce a flow in a predetermined and fixed manner. [NIST]
    
ToShape = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000130")
# To mold or form a flow. [NIST]
    
ToCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000131")
# To render a flow appropriate for the desired use. [NIST]
    
ToStop = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000132")
# To cease, or prevent, the transfer of a flow (material, energy, signal). [NIST]
    
ToPrevent = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000134")
# To keep a flow from happening. [NIST]
    
ToInhibit = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000135")
# To significantly restrain a flow, though a portion of the flow continues to be transferred. [NIST]
    
ToConvert = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000136")
# To change from one form of a flow (material, energy, signal) to another. [NIST]
    
ToProvision = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000137")
# To accumulate or provide a material or energy flow. [NIST]
    
ToSignal = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000138")
# To provide information on a material, energy or signal flow as an output signal flow. The information providing flow passes through the function unchanged. [NIST]
    
ToContain = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000139")
# To keep a flow within limits. [NIST]
    
ToSupply = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000140")
# To provide a flow from storage. [NIST]
    
ToTrack = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000141")
# To observe and record data from a flow. [NIST]
    
ToStabilize = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000142")
# To prevent a flow from changing course or location. [NIST]
    
ToPosition = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000143")
# To place a flow (material, energy, signal) into a specific location or orientation. [NIST]
    
ToDecompose = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000185")
# To decompose is the function to breakdown a single phase into two or more phases by heating or treatment with acid, alkali or enzymes. [Allotrope]
    
ToTransport = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000186")
# To transport is the function to transfer material. [Allotrope]
    
ToTransfer = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000187")
# To shift, or convey, a flow (material, energy, signal) from one place to another. [NIST]
    
ToMaintain = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000191")
# The function to maintain something. [Allotrope]
    
ToCombine = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000195")
# The function to make a whole out of many. [Allotrope]
    
ToProduce = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000196")
# The function to bring something into existence. [Allotrope]
    
ToSample = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000201")
# To sample is the function of to take parts or partitions of an object aggregate or data set for the interest for studying it. [Allotrope]
    
ToCover = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000203")
# To cover is a joining function realized when something is joined to a surface in such way that it is preventing some kind of material or energy flow through that surface. [Allotrope]
    
ToStir = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000205")
# To stir is a mixing function involving the agitation of a solution through circular motion. [Allotrope]
    
ToCompare = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000206")
# To compare is a function to observe or assess the similarities or dissimilarities between two things. [Allotrope]
    
ToDye = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000208")
# To dye is a function to change the color of some target material. [Allotrope]
    
ToCompress = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000209")
# To compress is the function to decrement the volume of a material by applying a force. [Allotrope]
    
ToDisconnect = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000210")
# To disconnect is a branching function that breaks up the connection between parts of an object so that they become separate. [Allotrope]
    
ToDisintegrate = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000211")
# To disintegrate is a function to change a material so that it breaks down in to smaller pieces of it. [Allotrope]
    
ToGrip = onto.search_one(iri="http://purl.allotrope.org/ontologies/function#AFFN_0000213")
# To grip is the function to prevent something from moving by holding it using friction or pressure. [Allotrope]
    
Material = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000275")
# A material entity that occupies space and possesses a rest mass. [Allotrope]
    
Cell = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000341")
# A material entity of anatomical origin (part of or deriving from an organism) that has as its parts a maximally connected cell compartment surrounded by a plasma membrane. [CL]
    
NaturalMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000877")
# A natural material is any product or physical matter that comes from plants, animals, or the ground. Minerals and the metals that can be extracted from them (without further modification) are also considered to belong into this category. [Wikipedia]
    
Energy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000880")
# Energy must be transferred to an object in order to perform work on, or to heat the object. It can be converted in form, but not created or destroyed. [Wikipedia]
    
ThermalEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000881")
# A form of energy that is transferred between bodies as a result of a temperature difference. [NIST]
    
MechanicTranslationalEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000882")
# Energy flow generated or required by a translation or virtual translation. [NIST]
    
ChemicalEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000883")
# Work resulting from the reactions by which substances are produced from or converted into other substances. [NIST]
    
ElectricalEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000884")
# Work resulting from the flow of electrons from a negative to a positive source. [NIST]
    
MechanicRotationalEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000885")
# Energy that results from a rotation or a virtual rotation. [NIST]
    
HydraulicEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000886")
# Work that results from the movement or force of a liquid, including hydrostatic forces. [NIST]
    
ElectromagneticEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000888")
# Energy that is propagated through free space or through a material medium in the form of electro-magnetic waves. [NIST]
    
PneumaticEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0000889")
# Work resulting from a compressed gas. [NIST]
    
VisibleLight = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001055")
# Electromagnetic radiation which is visible to the human eye and is responsible for the sense of sight. Visible light is usually defined as having wavelengths in the range of 400-700 nanometers. [Wikipedia]
    
UltravioletRadiation = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001056")
# An electromagnetic radiation with a wavelength from 10 nm to 400 nm. [Wikipedia]
    
InfraredRadiation = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001057")
# Electromagnetic radiation with longer wavelengths than those of visible light. It extends from the nominal red edge of the visible spectrum at 700 nanometer, to 1  micrometers. [Wikipedia]
    
GammaRadiation = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001058")
# Electromagnetic radiation of a kind arising from the radioactive decay of atomic nuclei and having wavelengths less than 10 picometers. [Allotrope]
    
Volumetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000022")
# Volumetry is a type of quantitative analysis that measures the quantity of a compound by quantifying its volume. [Allotrope]
    
Microscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000044")
# Microscopy is a imaging assay where a microscope is used to view a small object (or specimen) by producing a magnified image. [CHMO]
    
RamanSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000047")
# Any type of vibrational spectroscopy where the Raman scattering of monochromatic light, usually from a laser in the visible, near infrared, or near ultraviolet range by a sample is detected. [CHMO]
    
Granulometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000057")
# The measurement of the size distribution in a collection of grains. [CHMO]
    
OpticalDensityMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000080")
# The measurement of the light transmitted through a sample for a given wavelength. [CHMO]
    
Dissolving = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000112")
# A mixing step where a soluble component is mixed with a liquid component. [CHMO]
    
FlameIonizationMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000142")
# A flame ionization measurement is a measurement which is sensitive to compounds containing C-H bonds. A flow of carrier gas containing the sample is mixed with H2 and air and ignited. Any positively-charged radicals resulting from this process are collected at a cathode, allowing the current to be measured. [CHMO]
    
Cleaning = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000161")
# Cleaning is the process of getting rid of dirt, impurities, or extraneous unwanted matter. [Allotrope]
    
LiquidChromatography = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000225")
# Column chromatography where the mobile phase is a liquid. [CHMO]
    
Reflectometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000229")
# Any method for determining structure by directing a beam of particles or X-rays onto an extremely flat surface and measuring the intensity of the reflected radiation as a function of angle. [CHMO]
    
Vortexing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000254")
# Vortexing is a process of mixing that creates a vortex in the solution usually using a vortexer. [Allotrope]
    
Porosimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000260")
# The measurement of the pore diameter, pore-size distribution and total pore volume of a sample. [CHMO]
    
FractionCollection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000264")
# Fraction collection is the collection of fractional volumes of the column effluent. [IUPAC]
    
Spectrophotometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000266")
# A type of spectroscopy where the sample absorbs radiation in the range ultraviolet to near-infrared (0.1-2.5 µm) resulting in electronic transitions within the sample. [CHMO]
    
GasChromatography = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000310")
# Column chromatography where the mobile phase is a gas. [CHMO]
    
NuclearMagneticResonanceSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000326")
# A type of spectroscopy where the energy states of spin-active nuclei placed in a static magnetic field are interrogated by inducing transitions between the states via radio frequency irradiation. [CHMO]
    
Dilatometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000373")
# The measurement and study of dimensional changes in polymers as a function of temperature, fluid absorption, mechanical stress or chemical reaction. [CHMO]
    
CellularAssay = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000378")
# An assay that generates data about the presence, quantity, structure, function, behavior, or activity of cells, or a process that occurs at a cellular level of anatomical granularity (includes subcellular structures and organelles). [VIVO-ISF]
    
Separating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000422")
# A branching process that isolates flows into distinct component flows. The separated components are distinct from the flow before separation, as well as each other. [NIST]
    
CapillaryElectrophoresis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000474")
# A capillary electrophoresis is an electrophoresis which takes place in a capillary. [CHMO]
    
Planning = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000498")
# A process of creating or modifying a plan specification. [OBI]
    
Weighing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000503")
# Weighing is the measuring of weight of an object. Weight related to the amount of force acting on the object, either due to gravity or to a reaction force that holds it in place. [Wikipedia]
    
PeakPicking = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000516")
# Peak picking is a data transformation to convert profile spectral data into centroided spectral data. [Allotrope]
    
Conductometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000525")
# Conductometry is the measurement of the conductance of a solution as a function of concentration. Measurements are made indirectly across the resistance of the solution with alternating current. [CHMO]
    
Spectrometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000527")
# The study of the interaction of a sample with radiation or particles for measurement or detection. [CHMO]
    
Degassing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000593")
# Degassing is a sample preparation process whereby the adsorbed (dissolved) gas is removed from a solid or liquid. [Allotrope]
    
Calorimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000611")
# A measurement in which heat is measured as some chemical reaction or physical process occurs. [IUPAC]
    
Osmometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000620")
# The measurement of the osmotic strength of a substance which often used to determine its molecular weight. [CHMO]
    
Electrophoresis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000669")
# An electrophoresis is a separation where colloidal particles move at different speeds according to their electrophoretic mobilities in a separation medium, across which an electric field is applied. [CHMO]
    
Loading = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000708")
# Loading is the importing of a material into a new location that contains the material. [Allotrope]
    
Amperometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000733")
# An electrochemical technique where the cell current is measured whilst the potential difference between the indicator and reference electrodes is controlled. [CHMO]
    
VibrationalSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000780")
# Vibrational spectroscopy is a spectroscopy which probes the vibrational degrees of freedom of a molecule. [CHMO]
    
Dilution = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000785")
# Dilution is the process of adding a solvent to a solution to lower its concentration. [Allotrope]
    
Annealing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000792")
# A heat treatment that alters the microstructure of a material causing changes in its properties such as strength and hardness. [CHMO]
    
Purification = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000812")
# A purification is a removing process that is used to physically separate an analyte from byproducts, reagents or contaminating substances. [Allotrope, CHMO]
    
Rheometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000840")
# The study of the flow of fluids which cannot be defined by a single value of viscosity. Rheometry is the measurement of the relationship between deformation and stress for these liquids. [CHMO]
    
Gravimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000862")
# Gravimetry is the measurement of the strength of a gravitational field. [Wikipedia]
    
Voltammetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000869")
# An electrochemical technique where the cell current is measured as a function of time and as a function of the potential between the indicator and reference electrodes. [CHMO]
    
Detecting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000925")
# Detecting is observing the presence of an entity. This occurs when a threshold value of a quantity (quality, disposition, process property) is exceeded. [Allotrope]
    
Integration = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000970")
# The method used to obtain the integral of a function or curve. [Allotrope]
    
PeakSeparation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000979")
# Peak separation is a data transformation that allows to distinguish between two peaks. [Allotrope]
    
RemovingData = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0000983")
# Removing data is a data transformation that removes parts from an aggregate of data. [Allotrope]
    
FourierTransformRamanSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001062")
# Fourier transform Raman spectroscopy is a type of vibrational spectroscopy where the Raman scattering of light by a sample is detected and the spectrum is subject to a Fourier transform. [CHMO]
    
ElectronCaptureMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001113")
# Electron capture measurement is a measurement that is sensitive to electronegative compounds (e.g. halogenated compounds). A beta-particle emitter (e.g. 63Ni) is used to produce an electron beam, which is passed between two electrodes. As the sample is passed through the e-beam, organic functional groups interact with the electrons, interrupting the current. [Allotrope, CHMO]
    
BloodMeasurementMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001114")
# A measurement of the blood, it&apos;s contents, cells or other factors contained within the blood. [CMO]
    
BiologicalMeasurementMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001116")
# The determination of the relative strength of a substance (e.g., a drug or hormone or toxicant) by comparing its effect on a test organism with that of a standard preparation. [Wikipedia]
    
Polarimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001134")
# Polarimetry is a measurement of the extent to which a sample interacts with polarized electromagnetic radiation by transmission, reflection, refraction, or diffraction. [CHMO]
    
Mixing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001135")
# The combining of components, particles or layers into a more homogeneous state. The mixing may be achieved manually or mechanically by shifting the material with stirrers or pumps or by revolving or shaking the container. The process must not permit segregation of particles of different size or properties. Homogeneity may be considered to have been achieved in a practical sense when the sampling error of the processed portion is negligible compared to the total error of the measurement system. [CHMO]
    
QuantitativeAnalysisAssay = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001185")
# A measurement method which obtains the concentration or quantity of a specified substance in an analyte. [CHMO]
    
ChargeTransportMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001227")
# Any technique for measuring charge transport. [CHMO]
    
Magnetometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001266")
# The measurement of the strength and/or direction of magnetic fields, or the magnetic susceptibility of a sample. [CHMO]
    
SamplingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001319")
# Sampling material is sampling of a material of interest for studying. [Allotrope]
    
Chromatography = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001321")
# A chromatography is a separation where the components are distributed between two phases, one of which is stationary, while the other moves in a definite direction. [CHMO]
    
Synthesis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001348")
# Synthesis is a planned material process that combines, changes or converts material to produce a new material. [Allotrope]
    
Electroporation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001367")
# A method for introducing polar molecules into a host cell through the cell membrane. A large electric pulse (300-400 mV for &lt;1 ms) temporarily disturbs the phospholipid bilayer, allowing molecules like DNA to pass into the cell. [CHMO]
    
OpticalMicroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001404")
# A type of microscopy where the specimen is illuminated with visible light and a system of lenses is used to produce an image. [CHMO]
    
FormulationProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001426")
# The process of formulation allows the preparation of mixtures of components in accordance with a formula and documents the composition. [Allotrope]
    
MassSpectrometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001427")
# Mass spectrometry is a spectrometry that studies matter through the formation of gas-phase ions that are characterized using mass spectrometers by their mass, charge, structure, and/or physico-chemical properties. [IUPAC]
    
PhysicalBlending = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001457")
# The process of making a polymer blend by mechanically mixing different polymers together in the melt. [CHMO]
    
ScatteringSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001462")
# Any method that measures the amount of light that a substance scatters at certain wavelengths, incident angles, and polarization angles. [CHMO]
    
Cooling = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001478")
# The transfer of thermal energy from a material to its surrounding environment. [CHMO]
    
Differentiation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001499")
# The method to obtain the derivative of a function or curve. [Allotrope]
    
Filtration = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001530")
# The process of segregation of phases; the separation of suspended solids from a liquid or gas, usually by forcing a carrier gas or liquid through a porous medium. [CHMO]
    
Equilibration = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001606")
# Equilibration is the process of bring the state of a system to an equilibrium. [Allotrope]
    
Assembling = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001640")
# The process of fitting device components together to form a system. [Allotrope]
    
PieceCounting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001645")
# Piece counting is determining the number of objects in an object aggregate. [Allotrope]
    
Homogenization = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001649")
# The intensive mixing of mutually insoluble phases (sometimes with addition of surfactants) to obtain a soluble suspension or emulsion. [CHMO]
    
Dielectrometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001650")
# The measurement of the relative permittivity of a solution as a function of concentration. Measurements are made indirectly across the resistance of the solution with alternating current. [CHMO]
    
ElectronicSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001655")
# Any spectroscopic method which probes the electronic degrees of freedom of an atom or molecule. [CHMO]
    
FourierTransformNearInfraredAbsorptionSpectrometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001657")
# A type of spectroscopy where the sample absorbs a single pulse of radiation from the near infrared region (0.8-2 µm) and the spectrum obtained is subject to a Fourier transform. [CHMO]
    
Densitometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001666")
# The measurement of the density of a sample. [CHMO]
    
Stirring = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001698")
# Stirring is a mixing involving the agitation of a solution through circular motion. [Allotrope]
    
Rinsing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001750")
# Rinsing is the process of washing quickly a device with a solution. [Allotrope]
    
FourierTransformation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001756")
# The Fourier transformation decomposes a function of time (e.g. a signal) into the frequencies that make it up. [Wikipedia]
    
FourierTransformInfraredAbsorptionSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001787")
# Fourier transform infrared spectroscopy is a type of vibrational spectroscopy where the sample absorbs radiation from the infrared region (0.78-1000 µm) and the spectrum obtained is subject to a Fourier transform. [CHMO]
    
ImagingAssay = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001801")
# An imaging assay is a physical characterization assay to produce a picture of an entity. [CHMO]
    
Aspirating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001824")
# Aspirating is the process of sample preparation that is to draw an amount of a liquid by suction and then expel the liquid. [Allotrope]
    
PhMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001861")
# The measurement of pH is the negative logarithm to base ten of the hydrogen ion activity in a solution, this measures the degree of acidity or alkalinity. Operationally the pH of a solution X, pH(X), is measured relative to that of a standard reference solution, pH(S), and defined as pH(X) = pH(S) - (E(X) - E(S))/(RT/F)ln 10, where E(X) and E(S) are the electromotive forces measured in cells containing the solution X and the reference solution respectively. [CHMO]
    
Drying = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001876")
# The process of removing a solvent from a substance. [CHMO]
    
Washing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001878")
# Washing is a process by which a material entity acting as contaminant (e.g. excess staining reagent) is removed by application of one or more cycles of solution in flow. [CHMO]
    
LuminescenceMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001909")
# The measurement of luminescence from a material. [Allotrope]
    
Titration = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001916")
# Titration is the process of determining the quantity of a sample by adding measured increments of a titrant until the end-point, at which essentially all of the sample has reacted, is reached. [CHMO]
    
ScanningCalorimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001936")
# The measurement of thermodynamic parameters (e.g. enthalpy) during a chemical or biochemical reaction by the known variation (step-wise or linear) of one variable, whilst a second is kept constant. [CHMO]
    
Priming = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001951")
# Priming is a type of cleaning that happens at the beginning of a period of time and results in the device being filled with the appropriate reagents. [Allotrope]
    
Inverting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001953")
# Inverting is a sample preparation step of mixing. It is homogenization by switching the y-axis of a sample several times, turning it upside down using a syringe. [Allotrope]
    
Coulometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001955")
# An electrochemical technique where the total Coulombs of electricity required to complete (fully oxidize or fully reduce the sample in) an electrochemical reaction is measured. [CHMO]
    
Coating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001986")
# The application of a thin cover to a material. [CHMO]
    
Ionization = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001993")
# Ionization is a converting chemical reaction by which an atom or a molecule acquires a negative or positive charge by gaining or losing electrons, often in conjunction with other chemical changes. [Wikipedia]
    
Trending = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0001994")
# Trending is a process of monitoring that consists of collecting information and identifying underlying patterns. [Allotrope]
    
InfraredAbsorptionSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002016")
# Infrared absorption spectroscopy is a type of vibrational spectroscopy where the sample absorbs radiation from the infrared region. [CHMO]
    
Interferometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002065")
# The measurement of the properties of two or more lasers or waves by studying the pattern of interference created by their superposition. [CHMO]
    
Tensiometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002122")
# The measurement of the surface tension of a liquid. [CHMO]
    
DifferentialScanningCalorimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002124")
# Differential scanning calorimetry is a thermal analysis method in which the difference in energy inputs into a substance and a reference material is measured as a function of temperature whilst the substance and reference material are subjected to a controlled temperature program. [IUPAC]
    
Viscometry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002171")
# The measurement of the viscosity of fluids by observing the relative motion of the fluid and an object. Viscometry is used to measure the molecular weight of polymers. [CHMO]
    
Concentrating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002185")
# A preparative step where the concentration of one component is increased. [CHMO]
    
ElectronicAbsorbanceMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002188")
# Electronic absorption measurement is a measurement that is based on the absorption of energy by electronic transitions. [Allotrope]
    
Passaging = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002204")
# In biology, a subculture is a new cell or microbiological culture made by transferring some or all cells from a previous culture to fresh growth medium. This action is called subculturing or passaging the cells. Subculture is used to prolong the life and/or expand the number of cells or microorganisms in the culture. [Wikipedia]
    
ThermalConductivityMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002206")
# A measuring that is sensitive to inorganic gases. A hot (450 deg. C) filament is used to heat a carrier gas containing the sample and the difference in thermal conductivity caused by the presence of the sample is measured. [CHMO]
    
ClinicalMeasurementMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002212")
# A quantitative or qualitative value which is the result of an act of assessing a morphological or physiological state or property in a single individual or sample or a group of individuals or samples, based on direct observation or experimental manipulation. [CMO]
    
Oximetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002216")
# Any technique used to measure the levels of oxygen in a sample. [CHMO]
    
RefractiveIndexMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002239")
# A refractive index measurement is a measuring based on the change in refractive index of a solution. Light is passed through a hollow prism and focused on a photocell. When a liquid containing the sample is allowed to flow through the prism, the light diverges from its original path and the change in intensity and angle of the transmitted light is measured. [CHMO]
    
InfraredTransmissionSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002276")
# Infrared transmission spectroscopy is a type of vibrational spectroscopy where the transmission of infrared radiation (0.78-1000 µm) through a sample is detected. [CHMO]
    
Sonication = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002293")
# The irradiation of a liquid sample with sound (20-20 000 Hz) waves resulting in agitation. Sound waves propagate into the liquid media result in alternating high-pressure (compression) and low-pressure (rarefaction) cycles. During rarefaction, high-intensity sonic waves create small vacuum bubbles or voids in the liquid, which then collapse violently (cavitation) during compression, creating very high local temperatures. [CHMO]
    
Measuring = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002294")
# Measuring is observing a property of an entity called a quantity, that has a magnitude that can be expressed as a number and a reference to another entity, and obtaining one or more quantity values for it. The observed entity is a quality or a disposition for a continuant, for a process it is a process property such as duration. [Allotrope]
    
DataApodization = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002296")
# A term used meaning the processing and manipulation of the spectral data produced for the purposes of improving spectral appearance, change the signal to noise ratio (S/N), or resolution. The term is often collectively used in conjunction with line broadening, sharpening, averaging, smoothing. [Allotrope]
    
Colorimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002309")
# The determination of the spectral absorbance of a solution. This method is often used to determine the concentration of a chemical in a solution. [CHMO]
    
ThermalAnalysis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002313")
# Thermal analysis is any measurement technique in which a physical property of the sample is measured as a function of temperature. [CHMO]
    
Calibration = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002389")
# Calibration is the comparison of measurement values delivered by a device under test with those of a calibration standard of known accuracy. [Wikipedia]
    
Pipeting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002397")
# Pipeting transfers a given amount of liquid solution using a pipette, dropper or pipettor. [Allotrope]
    
NearInfraredAbsorptionSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002421")
# Near infrared absorption spectroscopy is a type of vibrational spectroscopy where the sample absorbs radiation from the near infrared region (0.8-2 µm). [CHMO]
    
Velocimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002434")
# The measurement of the velocity of a moving object or medium. [CHMO]
    
IonDetection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002541")
# Ion detection is detecting the presence of ions. [Allotrope]
    
MassAnalysis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002567")
# Mass analysis is a measuring process by which a mixture of ionic or neutral species is identified according to their m/z values (ions), or their aggregate atomic masses (neutrals), and their relative abundances. The analysis may be qualitative and/or quantitative. [IUPAC]
    
HardnessTest = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002668")
# Tablet hardness testing is a laboratory technique used by the pharmaceutical industry to test the breaking point and structural integrity of a tablet under conditions of storage, transportation, and handling before usage. [Wikipedia]
    
VaporGeneration = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002670")
# The producing of vapor. [Allotrope]
    
Assay = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002680")
# A planned process with the objective to produce information about the material entity that is the evaluand, by physically examining it or its proxies. [OBI]
    
Dedusting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002683")
# Dedusting is the process of removal of dust. [Allotrope]
    
Fingerprinting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002691")
# Fingerprinting is the process of comparison or overlay of measured spectra with existing reference spectra. [Allotrope]
    
ClosedLoopVaporGeneration = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002702")
# The closed loop uses feedback control for the regulation of the vapor generation. The system continuously detects deviations from the target partial pressure and adjusts the vapor generation correspondingly. [Allotrope]
    
SieveAnalysis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002715")
# Sieve analysis is a process of particle sizing by filtering particles according to their size through sieves with decreasing pore size. [Allotrope]
    
ParticleSizing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002716")
# Particle sizing is an experimental method for the investigation of particle sizes in a sample. [Allotrope]
    
DisintegrationTest = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002744")
# A disintegration test is a test to check the time that an object needs to disintegrate. [Allotrope]
    
TubeBreeding = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002764")
# Tube breeding is a process of cleaning vacuum tubes in order to remove any impurities. [Allotrope]
    
Fluorimetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002788")
# An assay in which a materials fluorescence is determined. [VIVO-ISF]
    
Packing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002792")
# Packing is the process of transferring an object into a container as a densely packed phase. [Allotrope]
    
ConcentrationMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002800")
# An concentration measurement is the determination of the concentration of a compound in solution. [Allotrope]
    
Test = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002834")
# A test can be considered a technical operation or procedure that consists of determination of one or more characteristics of a given product, process or service according to a specified procedure. Often a test is part of an experiment. The test result can be qualitative (yes/no), categorical, or quantitative (a measured value). It can be a personal observation or the output of a precision measuring instrument. [Wikipedia]
    
Compression = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002843")
# Compression is the act of reducing volume by applying a force. [Allotrope]
    
Quantification = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0002849")
# In mathematics and empirical science, quantification (or quantitation) is the act of counting and measuring that maps human sense observations and experiences into members of some set of numbers. [Wikipedia]
    
DataAcquisition = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003095")
# Data acquisition is the process of sampling signals that measure real world physical conditions and converting the resulting samples into digital numeric values that can be manipulated by a computer. [Wikipedia]
    
StructureDetermination = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003274")
# A chemical structure determination includes a chemist&apos;s specifying the molecular geometry and, when feasible and necessary, the electronic structure of the target molecule or other solid. [Wikipedia]
    
QualityProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003281")
# A quality process profile is a process profile that covers the change of a quality of an independent continuant that is participant of the profiles process. [Allotrope]
    
Calculation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003282")
# A calculation is a process by which a data transformation technique that involves problem solving for numbers or quantities is performed. [Allotrope]
    
Drawing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003284")
# Drawing is the process by which an object or liquid is extracted from a container or receptacle. [Allotrope]
    
End = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003286")
# The process boundary when the process ends. [Allotrope]
    
PeakAnalysis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003290")
# A peak analysis is a data transformation on a peak that analyzes peak facets. [Allotrope]
    
RatioCalculation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003297")
# A ratio calculation is the process of performing the mathematical exercise of dividing a quotient of one quantity by another quotient to demonstrate the quantitative relation between two amounts showing the number of times one value contains or is contained within the other. [Allotrope]
    
Specifying = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003299")
# Specifying is a process that produces an information object which describes constraints or objectives on characteristics like qualities, functions, dispositions, facets of continuants or processes. [Allotrope]
    
Observing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003305")
# Observation is the active acquisition of information from a primary source. In living beings, observation employs the senses. [Wikipedia]
    
ContainingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003306")
# The state of keeping a flow within spatial limits. [Allotrope]
    
Transferring = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003312")
# Transferring is channeling a flow (material, energy, signal) from one place to another. [NIST]
    
Communicating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003314")
# Communicating is transferring information from one material entity to another. This can be by way of a material or energy connecting the entity or by transporting the material bearing the information between the locations. [Allotrope]
    
Producing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003315")
# A process where some new material entity or information content entity does not exists at the start of the process but is existing at the end by way of the process. [Allotrope]
    
Consuming = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003316")
# A process where a essential material entity participant ceases to exist at the end and  it was existing at the start. [Allotrope]
    
ConsumingEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003318")
# Consuming energy is a consuming that consumes energy. [Allotrope]
    
ProducingEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003319")
# Producing energy is the producing of energy (from an unspecified energy source). [Allotrope]
    
Recording = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003325")
# The process of copying the information in a signal into a persistent information bearer. [Allotrope]
    
Start = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003328")
# The process boundary when the process starts. [Allotrope]
    
Selecting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003329")
# The partitioning of some object aggregate. [Allotrope]
    
Referencing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003330")
# Referencing is the process of mentioning or referring to an entity by using a denotation of the entity. [Allotrope]
    
Maintaining = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003331")
# Maintaining is a regulating process that keeps some or all of the characteristics of a material over time within a specification. [Allotrope]
    
Branching = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003332")
# The process of causing a flow to no longer be topologically connected. [NIST]
    
Dividing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003335")
# Dividing is a separating of flows focused on all parts of the flow. [Allotrope]
    
Extracting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003336")
# Separating by drawing, or forcibly pulling out, a flow that is of a different kind than that of the input flow. [Allotrope, NIST]
    
Localizing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003348")
# A processing that affects the spatial location or orientation of some participants. [Allotrope]
    
Importing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003349")
# Importing is a localization that brings in a flow (material, energy, signal) from outside of a boundary to the inside. [Allotrope, NIST]
    
Exporting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003350")
# Exporting is a channeling that sends a flow (material, energy, signal) from inside of a boundary to the outside. [Allotrope, NIST]
    
Guiding = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003351")
# Guiding is directing the course of a flow (material, energy, signal) along a specific path. [Allotrope, NIST]
    
Connecting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003354")
# Connecting is bringing two or more topological flows into connection. [Allotrope, NIST]
    
Coupling = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003356")
# Coupling is connecting together material such that the members are still distinguishable from each other. [NIST]
    
Joining = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003357")
# Joining is the direct coupling of flows without any intermediary flow. [Allotrope]
    
Linking = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003358")
# Linking is coupling flows together by means of an intermediary flow. [NIST]
    
Controlling = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003359")
# Controlling is changing or regulating a flow in its magnitude. [NIST, Allotrope]
    
Actuating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003360")
# Actuating is the process of commencing the flow of energy, signal, or material in response to an imported control signal. [NIST]
    
RegulatingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003361")
# Regulating material is adjusting a quality of material in response to a control signal. [Allotrope]
    
Shaping = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003364")
# Shaping is changing the material in regard to spatial form. [Allotrope]
    
Decrementing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003367")
# Decrementing is reducing the magnitude of a quality in a predetermined and fixed manner. [Allotrope]
    
Incrementing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003368")
# Incrementing is enlarging the magnitude of a quality in a predetermined and fixed manner. [NIST]
    
Achievement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003370")
# A process boundary based on some physical characteristics at the start or end of some process changing these characteristics. [Allotrope]
    
Accomplishment = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003371")
# A non-cumulative process (event) that is non-atomic. [DOLCE]
    
State = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003374")
# A state is a homomeric, cumulative process in which all the temporal parts are described by the same expression used for the whole. [Allotrope]
    
Collecting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003385")
# The act of gathering things together; having been brought together in one place. [NCI]
    
Arrival = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003393")
# Arrival is the achievement of reaching the destination site in a moving process. [Allotrope]
    
Repelling = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003394")
# A spatial change processing the increases the spatial distance from the start. [Allotrope]
    
RestingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003395")
# A state when material object keeps its spatial location and orientation. [Allotrope]
    
Attracting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003396")
# A spatial change state the decreases the spatial distance at the end. [Allotrope]
    
MereotopologicalProcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003400")
# A process that affects the topological connectedness or parthood of two or more flows. [Allotrope]
    
Partitioning = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003403")
# A processing that causes a flow to break up into disconnected partitions. The individual bits are similar to each other and the undistributed material. [Allotrope]
    
Blocking = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003404")
# A state of keeping two materials topologically disconnected by a separation medium. [Allotrope]
    
Departure = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003408")
# Departure is the achievement of leaving the source site in a moving process. [Allotrope]
    
Positioning = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003409")
# Positioning is a localization that changes a specific spatial location and orientation of an object relative to another. [Allotrope]
    
ConvertingEnergy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003416")
# Changing from one form of a flow energy to another. [NIST]
    
Charging = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003419")
# Increasing the amount of energy in a system. [Allotrope]
    
Stopping = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003424")
# Stopping it the process of ceasing or preventing the transfer of a flow. [NIST]
    
Receiving = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003431")
# A process that transports a signal across a system boundary into the system. [Allotrope]
    
Sending = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003432")
# A process that transports a signal across a system boundary out of the system. [Allotrope]
    
SensingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003433")
# The state of perceiving or becoming aware of a signal. [Allotrope]
    
Displaying = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003434")
# The process of transforming a signal into a visual signal (color, pattern). [Allotrope]
    
Emission = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003437")
# The achievement that a signal has left a source in an information transmission. [Allotrope]
    
HoldingInPlace = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003449")
# A state of supporting a material to stay in a location or orientation. [Allotrope]
    
Reception = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003450")
# The accomplishment that a transferred signal reaches at its designated target. [Allotrope]
    
RateProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003454")
# A rate profile is a process profile, which are changes to ratios of determinate quality magnitudes over time. [Allotrope]
    
CyclicRateProcessProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003455")
# A cyclic rate profile is a rate profile of a process that follows a cyclic pattern. [Allotrope]
    
DisconnectedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003456")
# A state s with participating materials m1 and m2, and m1 is not connected to m2. [Allotrope]
    
ConnectedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003457")
# A state s with participating materials  m1 and m2  and m1 is connected to m2. [Allotrope]
    
Melting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003458")
# The state of material becoming liquid from a solid. [Allotrope]
    
Solidifying = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003459")
# The state of material becoming solid from liquid. [Allotrope]
    
Moving = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003464")
# A state when material is changing its position in space. [Allotrope]
    
IndicatingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003470")
# The state when the role of a signal is realized independent of any other material entity that may sense (perceive) the signal. [Allotrope]
    
Tracking = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003471")
# The process of sensing signals and recording the information in the signals. [Allotrope]
    
SortingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003472")
# Sorting is the dividing of material by an ordering criteria. [Allotrope]
    
Removing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003473")
# Taking away a part of a flow from its prefixed place. [NIST]
    
Combining = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003475")
# Combining is the building of a whole out of parts. [Allotrope]
    
EnergizingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003481")
# State of making energy available for a consumer. [Allotrope]
    
Regulating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003485")
# Regulating is the adjusting of a flow in response to a control signal. [NIST]
    
Changing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003486")
# Changing is a processing by which an entity gains or looses parts, qualities, roles, dispositions, functions etc in a predetermined and fixed manner but maintains its identity. [Allotrope]
    
Indicating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003488")
# Indicating is signaling to make something known to the user about a flow. [NIST]
    
MaterialTest = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003490")
# A test that verifies that some quality is within a specification. [Allotrope]
    
AnalysisAssay = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003491")
# An assay with the objective to capture information about the presence, concentration or amount of an analyte in the evaluand. [OBI]
    
Assessing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003538")
# Assessing is evaluating or estimating a quality or behavior. [Allotrope]
    
ImageAnalysis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003540")
# Image analysis is the discovering of patterns in an image that are correlated to qualities of the material entity the image represents or of abstract patterns. [Allotrope]
    
TemperatureMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003541")
# A temperature measurement is a measurement that targets the temperature of some material entity. [Allotrope]
    
StoringState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003551")
# Storing is containing or collecting flows to accumulate. [NIST]
    
Signaling = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003552")
# Signaling is the process of providing information on a material, energy or signal flow as an output signal. [NIST]
    
SupplyingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003553")
# A supplying state is a providing state that makes energy or material available for processing or consumption. [Allotrope]
    
ConsumingSignal = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003554")
# Consuming signal is consuming of signals. [Allotrope]
    
PhysicalCharacterizationAssay = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003556")
# An assay that examines physical qualities of material. [Allotrope]
    
ProvidingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003563")
# Providing is the state of accumulating or supplying a material or energy flow. [NIST]
    
CollectingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003564")
# A storing state that brings a flow together at one place. [NIST]
    
Converting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003565")
# Converting is a process that changes from one form of a flow (material, energy, signal) to another. [NIST]
    
ConvertingMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003566")
# Changing from one form of a flow material to another. [NIST]
    
Interpolation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003568")
# Interpolation is the constructing new data points within the range of a discrete set of known data points. [Wikipedia]
    
PeakHeightAnalysis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003570")
# A peak analysis that determines the peak height following a specified algorithm. [Allotrope]
    
PeakWidthAnalysis = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003571")
# A peak analysis that determines the peak width following a specified algorithm. [Allotrope]
    
Totaling = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003572")
# Totaling is the calculation of a sum or an integral. [Allotrope]
    
Sorting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003573")
# Sorting is distributing flows based on some associated physical quality or entity into distinct fractions according to a defined order. [Allotrope]
    
Taking = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003576")
# Taking material is the exporting of material from a location or site. [Allotrope]
    
Pumping = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003577")
# Pumping is a material transport of fluids by suction or pressure or both. [Allotrope]
    
DataCollection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003581")
# A data transformation that assigns some data to a collection. [Allotrope]
    
OrderingData = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003582")
# Ordering data is the process of arranging data items systematically. [Allotrope]
    
Denoting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003583")
# Denoting is a process that assigns a symbol to an entity in order to reference it. [Allotrope]
    
Describing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003584")
# Describing is a process by which an account of some relevant characteristics, qualities or events of an entity are given or presented. [Allotrope]
    
Identifying = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003585")
# Identifying is recognizing an entity by some criteria and assigning an identifier to the entity. [Allotrope]
    
Indexing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003586")
# Indexing is the process of organizing data according to a specific plan, usually to streamline data retrieval. [Allotrope]
    
Reflection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003591")
# Reflection is the change in direction of a wavefront at an interface between two different media so that the wavefront returns into the medium from which it originated. [Wikipedia]
    
SpecularReflection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003592")
# Specular reflection is the mirror-like reflection of waves, such as light, from a surface. In this process, each incident ray is reflected, with the reflected ray having the same angle to the surface normal as the incident ray. [Wikipedia]
    
DiffuseReflection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003593")
# Diffuse reflection is the reflection of light or other waves or particles from a surface such that a ray incident on the surface is scattered at many angles rather than at just one angle as in the case of specular reflection. An ideal diffuse reflecting surface is said to exhibit Lambertian reflection, meaning that there is equal luminance when viewed from all directions lying in the half-space adjacent to the surface. [Wikipedia]
    
Scattering = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003594")
# Scattering is a general physical process where some forms of radiation, such as light, sound, or moving particles, are forced to deviate from a straight trajectory by one or more paths due to localized non-uniformities in the medium through which they pass. [Wikipedia]
    
Deflecting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003595")
# A deflection, in physics, refers to the change in an objects&apos; acceleration as a consequence of contact (collision) with a surface or the influence of a field. [Wikipedia]
    
Inhibiting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003596")
# Significantly restraining a flow, though a portion of the flow continues to be transferred. [NIST]
    
Preventing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003597")
# Keeping a flow from happening. [NIST]
    
DataTransformation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003598")
# A converting process that converts the signals from one form into another by changing its content. [Allotrope]
    
Comparing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003599")
# The observation or assessment of the similarities or dissimilarities between two things. [Allotrope]
    
Assigning = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003603")
# Assigning is the producing of an assignment that asserts some relation between entities. [Allotrope]
    
PeakIdentification = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003618")
# Peak identification is an assigning of a peak to an analyte or portion of an analyte of interest. [Allotrope]
    
PeakDetection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003619")
# Peak detection is a data transformation that finds peaks in a data distribution function. [Allotrope]
    
Activity = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003620")
# An activity is a process that is cumulative but not homomeric. [Allotrope, DOLCE]
    
Containing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003623")
# Containing is the state of keeping an object in the inside of a cavity. [Allotrope]
    
NumberDensityMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003627")
# A measuring that targets the number density. [Allotrope]
    
Sampling = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003634")
# Sampling is the process of taking parts or partitions of an object aggregate or data set for the interest for studying it. [Allotrope]
    
SamplingData = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003635")
# Sampling data is sampling on a set of data items. [Allotrope]
    
DescriptiveStatistics = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003636")
# Descriptive statistics is the process of using and analyzing descriptive statistics. A descriptive statistic is a summary statistic that quantitatively describes or summarizes features of a collection of information. [Wikipedia]
    
Inferring = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003637")
# Inferring is a process that produces logical consequences by steps of reasoning, moving from premises. [Wikipedia]
    
StatisticalInference = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003638")
# Statistical inference is the process of using data analysis to deduce properties of an underlying probability distribution. [Wikipedia]
    
Marking = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003639")
# Marking is changing some quality of a material so that it concretizes a symbol. [Allotrope]
    
DispersedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003640")
# Dispersed state is a state of a system in which discrete particles of one material are dispersed in a continuous phase of another material. [Allotrope]
    
Degradation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003641")
# Degradation is the state of changing in the qualities of a material under the influence of one or more environmental factors such as heat, light or chemicals such as acids, alkalies and some salts to a lower level of quality. [Allotrope]
    
Approving = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003643")
# Approving is agreeing to a proposition or accepting something as satisfactory towards an  set objective. [Allotrope]
    
Deciding = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003644")
# Deciding is making a choice from a set of alternatives. [Allotrope]
    
Signing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003645")
# A signing is attaching a signature to an information content entity. The signature is an identifier for the agent doing the signing. [Allotrope]
    
Submitting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003646")
# Submitting is the transferring of a material or information from a sender (the submitter) to a receiver with the intent that the receiver acts on the transferred entity towards an objective stated by the submitter. [Allotrope]
    
Summarizing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003654")
# Shortening a passage or a write-up without changing its meaning but by using different words and sentences. [Wikipedia]
    
DataReduction = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003655")
# Data reduction is the transformation of numerical or alphabetical digital information derived empirically or experimentally into a corrected, ordered, and/or simplified form. [Wikipedia]
    
DataAggregation = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003656")
# Data aggregation is a data reduction that applies an aggregating function on the data to produce an aggregated (summary) datum from a collection of data items. [Allotrope]
    
Averaging = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003657")
# Averaging is the calculation of a mean statistic or a temporal average value. [Allotrope]
    
DetectingState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003664")
# A detecting state is a state that occurs when a detector detects its detection target. [Allotrope]
    
RunningState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003665")
# A running state is a state during which a device or service performs its specified function in normal operation. [Allotrope]
    
Injecting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003666")
# Injecting is the forceful loading of a fluid into the interior of some other object. [Allotrope]
    
IdleState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003667")
# An idle state is a state during which a device or service waits for being started to execute a planned process. [Allotrope]
    
CompletedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003668")
# A completed state is a state during which a planned process has run to completion and the device or service is waiting for a reset that cause the state to change to an idle state. [Allotrope]
    
PausedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003669")
# A paused state is a state during which a device or service waits for being resumed to continue a planned process. [Allotrope]
    
AbortedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003670")
# An aborted state is a state during which a planned process has run to completion in an abnormal way and the device or service is waiting for a reset that cause the state to change to an idle state. [Allotrope]
    
StoppedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003671")
# A completed state is a state during which a planned process has run to an end and the device or service is waiting for a reset that cause the state to change to an idle state. [Allotrope]
    
HeldState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003672")
# A held state is a state during which a device or service waits for a longer time e.g. for maintenance. [Allotrope]
    
ProcessState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003673")
# A process state is a state where a device or service is executing a planned process or is in a specific configuration. [Allotrope]
    
Monitoring = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003681")
# Monitoring is an observing of a quality important for the successful and/or safe operation of a controlled process. [Allotrope]
    
TimeDomainZeroPadding = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003682")
# Time domain zero padding is a data transformation used in Fourier transformation by padding the time domain with zero values. [Allotrope]
    
CoatedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003687")
# Coated state is the covering state when a substance covers the surface of another substance firmly. [Allotrope]
    
TimeMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003700")
# A time measurement is a measurement of the duration of some process which is a quantification of the magnitude of the time region between the start and the end of the process in relation to some recurring process involving a clock. [Allotrope]
    
AnalyteCalibration = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003706")
# Analyte calibration is producing a calibration curve from measurements of known amounts of analyte that will be used as measurement function for the measurement of unknown amounts of analytes. [Allotrope]
    
Nebulizing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003719")
# Nebulizing is converting by of breaking up solutions and suspensions into small aerosol droplets. [Wikipedia]
    
BackgroundCorrection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003721")
# Background correction is a data transformation designed to remove irrelevant contributions from the measured signal, e.g. those due to instrument noise or sample preparation. [BAO]
    
DataExtraction = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003722")
# Data extraction is a data transformation process whereby specific data is taken out of a larger set of data and presented in a usable format. [Allotrope]
    
Experiment = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003735")
# An experiment is a planned process that has the goal of verifying, falsifying, or establishing the validity of a hypothesis. [SIO]
    
PreventativeMaintenance = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003739")
# Preventative maintenance is a proactive maintenance of a device involving inspection, testing and preemptive replacement of parts likely to fail before the preventative maintenance activity. [Allotrope]
    
CoveredState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003745")
# Covered state is a connected state where something is located on the surface of another thing and prevents some kind of material or energy flow through that surface. [Allotrope]
    
Covering = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003746")
# Covering is a joining process where the joining is on to the surface in such way that it is preventing some kind of material or energy flow through that surface. [Allotrope]
    
ApprovalState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003757")
# An approval state is a state where information content such as a specification is allowed or is suitable by an authority for a purpose or in a context. [Allotrope]
    
IsApproved = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003758")
# Is approved is an approval state where information content such as a specification is approved by an authority for a purpose or in a context. [Allotrope]
    
IsDenied = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003759")
# Is denied is an approval state where information content such as a specification is denied by an authority for a purpose or in a context. [Allotrope]
    
ElectrolyticConductivityMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003766")
# An electrolytic conductivity measurement is a measurement of the electrolytic conductivity of a material. [Allotrope]
    
QuantitativePolymeraseChainReaction = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003769")
# Quantitative polymerase chain reaction (qPCR) is a quantitative analytical assay based on the polymerase chain reaction (PCR). It monitors the amplification of a targeted DNA molecule during the PCR. [Allotrope]
    
PolymeraseChainReaction = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003770")
# Polymerase chain reaction is a synthesis to rapidly amplify pre-determined regions of double-stranded DNA. Generally involves the use of a heat-stable DNA polymerase. [IUPAC]
    
Dyeing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003771")
# Dyeing is the changing of the color of some material. [Allotrope]
    
BaselineDetermination = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003772")
# Baseline determination is a data transformation that calculates or assigns a baseline to a curve. [Allotrope]
    
Imaging = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003774")
# Imaging is a process that produces an image of something. [Allotrope]
    
Evacuating_chem = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003785")
# Evacuating is the removing of gasses from a container to create a vacuum. [Allotrope]
    
NearInfraredTransmissionSpectroscopy = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003787")
# Near infrared transmission spectroscopy is a type of vibrational spectroscopy where the transmission of near infrared radiation (0.8-2 µm) through a sample is detected. [CHMO]
    
Shaking = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003802")
# Shaking is a mixing process involving short rapid motions of the material inside a container. [Allotrope]
    
DisintegratedState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003806")
# Disintegrated state is a state of an object when its has turned into an aggregate of small, separated pieces. [Allotrope]
    
Disintegrating = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003807")
# Disintegrating is a break a material into small, separate parts. [Allotrope]
    
Disconnecting = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003808")
# Disconnecting is a branching process that removes the connection between parts of a flow so that they become topologically separate. [Allotrope]
    
Flowing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003811")
# Flowing is the state of moving along a steady continuous stream. [Allotrope]
    
CodeScanning = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003814")
# Code scanning is the transformation of data in the representation form of visual machine-readable codes to another form. [Allotrope]
    
StateOfMatterState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003823")
# A changing state of matter is a quality state that  is expressed by the state of matter of some material participating in the state. [Allotrope]
    
MereotopologicalState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003824")
# A mereotopological state is a state that is expressed by the mereotopological connectedness or parthood of participants in the state. [Allotrope]
    
QualityState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003825")
# A quality state is a state that is expressed by a quality of some material participating in the state. [Allotrope]
    
SpatialState = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003826")
# A spatial state is a state that is expressed by a spatial location or orientation of some material participating in the state. [Allotrope]
    
GelTransition = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003828")
# A gel transition is a state of matter state where some material transitions into a gel. [Allotrope]
    
DielectricPolarizationMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003829")
# A dielectric polarization measurement is a measuring of the difference between the electric displacement vector and the product of the electric field strength with the permittivity of vacuum. [IUPAC]
    
Gripping = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003832")
# Gripping is a guiding process by applying friction or pressure to prevent movement. [Allotrope]
    
NitrogenChemiluminescenceDetection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003834")
# The detection of luminescence emitted from nitrogen in a sample as a result of a chemical reaction. [CHMO]
    
SulfurChemiluminescenceDetection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003835")
# The detection of luminescence emitted from sulfur in a sample as a result of a chemical reaction. [Allotrope]
    
FlamePhotometricDetection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003836")
# A detection method that is sensitive to sulfur- and phosphorus-containing compounds. A flow of carrier gas containing the sample is mixed with oxygen or air and ignited. Any chemiluminescence due to these compounds is then detected. [CHMO]
    
EvaporativeLightScatteringDetection = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003837")
# A detection method where a liquid containing the sample is atomized in a gas, forming small droplets which are allowed to evaporate leaving the sample as fine particles. The suspended particles pass through a light beam and the scattered light transmitted by the particles is sensed by a photodiode or photomultiplier tube. The response can be quantitative and relative to the amount of molecules eluting. [Allotrope, CHMO]
    
Dispensing = onto.search_one(iri="http://purl.allotrope.org/ontologies/process#AFP_0003838")
# Dispensing is giving out material in discrete portions. [Allotrope]
    
Ratio = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000005")
# A ratio is a relational quality that is the proportion of the magnitude of two qualities of the same kind. [Allotrope]
    
InnerDiameter_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000018")
# The inner diameter is the diameter at the inside. [Allotrope]
    
CylinderLength_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000020")
# Quality of a material entity of cylindrical or tubular shape which describes its length along its main (non-circular) dimension. [Allotrope]
    
Distance = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000032")
# A quality that is the extent of space between two entities. [PATO]
    
SystemConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000036")
# A configuration is a range of determinate quality or combination of qualities that are present in some part of a device or system that influence participants in some of the functions of the device or system including the device or system itself. [Allotrope]
    
HeatRate = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000042")
# Quality of a bearer which describes the bearer&apos;s efficiency in terms of useful output energy. [Allotrope]
    
LinearVelocity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000043")
# Quality of velocity inhering in a bearer which is traveling in a straight line, meaning its direction is not changing. [Allotrope]
    
Torque_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000045")
# A physical quality that inheres in a bearer by virtue of its rotational force. [Allotrope]
    
Voltage_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000048")
# A quality which inheres in an independent continuant which has a difference in electric potential energy between two points per unit electric charge. [Wikipedia]
    
ElectricCurrent_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000049")
# A quality inhering in a bearer by virtue of the bearer&apos;s ability to conduct an electrical charge. [Allotrope]
    
ThermalQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000056")
# A physical quality that inheres in a bearer by virtue of its material properties pertaining to temperature. [Allotrope]
    
ThermalConductivity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000057")
# A conductivity quality inhering in a bearer by virtue of the bearer&apos;s disposition to spontaneous transfer of thermal energy from a region of higher temperature to a region of lower temperature. [Wikipedia]
    
HeatCapacity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000058")
# Heat capacity is a thermal quality that inheres in a bearer by virtue of its resistance or ability to change its temperature based on a change to the heat added or removed from said object (ratio of head added or removed from an object to the resulting temperature change). [Wikipedia]
    
RadiativeEmissivity = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000059")
# A physical quality that inheres in a bearer by virtue of its emissivity, which is defined as a material&apos;s effectiveness in emitting energy as thermal radiation. [Wikipedia]
    
Absorbance_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000061")
# Absorbance is the logarithm of the ratio of intensities of electromagnetic radiation on both sides of a medium that the radiation passes through. Lambert-Beer&apos;s law states that absorbance is equal to the product of molar coefficient of absorbance of an absorbing compound in a medium times its concentration in the medium times path length of the electromagnetic radiation passing through the medium. [Allotrope]
    
FocalLength = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000062")
# A physical quality that inheres in a bearer by virtue of how strongly the bearer converges or diverges light. [Wikipedia]
    
Reflectance_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000064")
# Reflectance is an optical quality that is the fraction of incident radiation reflected by a surface or discontinuity. [IUPAC]
    
ElectricalAndMagneticQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000065")
# A physical quality that inheres in an bearer by virtue of how that bearer interacts with electromagnetic radiation. [Wikipedia]
    
ElectricResistance_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000067")
# Electric resistance is the quality inhered in a conductor that is the electric potential difference divided by the electric current when there is no electromotive force in the conductor. [IUPAC]
    
StateOfMatter = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000111")
# A state of matter is a quality of material that is one of the distinct forms in which matter can exist. Four states of matter are observable in everyday life: solid, liquid, gas, and plasma. Many other states are known to exist only in extreme situations, such as Bose-Einstein condensates, neutron-degenerate matter, and quark-gluon plasma, which only occur in situations of extreme cold, extreme density, and extremely high-energy color-charged matter respectively. [Wikipedia]
    
Solid = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000112")
# A state of matter, in which particles are closely packed together. The forces between particles are strong so that the particles cannot move freely but can only vibrate. As a result, a solid has a stable, definite shape, and a definite volume. Solids can only change their shape by force, as when broken or cut. [Wikipedia]
    
Liquid = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000113")
# A state of matter that is a nearly incompressible fluid that conforms to the shape of its container but retains a (nearly) constant volume independent of pressure. [Wikipedia]
    
Gas = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000114")
# A state of matter that is a compressible fluid. Not only will a gas conform to the shape of its container but it will also expand to fill the container. In a gas, the molecules have enough kinetic energy so that the effect of intermolecular forces is small (or zero for an ideal gas), and the typical distance between neighboring molecules is much greater than the molecular size. A gas has no definite shape or volume, but occupies the entire container in which it is confined. [Wikipedia]
    
Plasma = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000115")
# A physical quality that inheres in a bearer by virtue of its plasma is a state of matter, that is, it does not have definite shape or volume. Unlike gases, plasmas are electrically conductive, produce magnetic fields and electric currents, and respond strongly to electromagnetic forces. Positively charged nuclei swim in a &quot;sea&quot; of freely-moving disassociated electrons, similar to the way such charges exist in conductive metal. [Wikipedia]
    
ShearModulus_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000116")
# Shear modulus is a ratio of shear stress to the shear strain. It is a quantity for measuring the stiffness of materials. The shear modulus is concerned with the deformation of a material. [Wikipedia]
    
ShearModulusOfZeroMagnitude = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000118")
# A zero shear modulus is a determinate shear modulus with zero magnitude. [Allotrope]
    
SupercriticalFluid = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000119")
# A gaseous state of matter in which temperature and pressure are above the critical temperature and critical pressure. In this state, the distinction between liquid and gas disappears. [Wikipedia]
    
Gel_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000120")
# A gel is a solid state of matter of jelly-like material that can have properties ranging from soft and weak to hard and tough. Gels are defined as a substantially dilute cross-linked system, which exhibits no flow when in the steady-state. By weight, gels are mostly liquid, yet they behave like solids due to a three-dimensional cross-linked network within the liquid. [Wikipedia]
    
ExactMass = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000123")
# Exact mass is a quality of mass of an isotopic species that is obtained by summing the masses of the individual isotopes of the molecule. [Wikipedia]
    
Fugacity = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000129")
# Thermodynamic property of a real gas that, if substituted for the pressure or partial pressure in the equations for an ideal gas, gives equations applicable to the real gas. [Wikipedia]
    
AcousticQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000138")
# Property that inheres in an independent continuant having to do with sound or hearing. [NCI]
    
FrequencyResponse = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000139")
# Frequency response is the quantitative measure of the output spectrum of a system or device in response to a stimulus, and is used to characterize the dynamics of the system. It is a measure of magnitude and phase of the output as a function of frequency, in comparison to the input. [Wikipedia]
    
AudibleDeviceNoise = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000141")
# An unintended or unpleasant sound that emanates from a device. [NCI]
    
Polarization = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000142")
# A physical quality that inheres in a bearer by virtue of the geometrical orientation of the oscillations of a transverse wave. [Allotrope]
    
Flowability = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000144")
# Flowability is the quality of material to move by flow. [Allotrope]
    
Friction_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000145")
# Friction is a quality of an object which is resisting the force the relative motion of solid surfaces, fluid layers, and material elements produce when sliding against each other. [Wikipedia]
    
AmountOfSubstance_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000166")
# Amount of substance is a quality inhered in a portion of material that is a size that is proportional to the number of elementary entities present. [Allotrope]
    
MassConcentration_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000167")
# Mass concentration is a concentration that is defined as the mass of a constituent divided by the volume of the mixture. [IUPAC]
    
MolarConcentration_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000168")
# Molar concentration is the ratio of molar amount of a substance divided by volume of mixture containing the amount of substance. [Allotrope]
    
VolumeFraction_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000169")
# The volume fraction is a fraction pertaining the volume of a constituent divided by the total volume of all constituents in the mixture. [Allotrope]
    
Fraction_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000172")
# A fraction is the ratio of one constitutent (part) to all constituents of a mixture. [Allotrope]
    
MassFraction_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000173")
# The mass fraction is a fraction pertaining the mass of a constituent divided by the total mass of all constituents in the mixture. [Allotrope]
    
AmountFraction_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000174")
# The amount fraction is the ratio of the amount of a constituent divided by the total amount of all constituents in the mixture. [Allotrope]
    
VolumeConcentration_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000175")
# Volume concentration is a concentration that is defined as the volume of a constituent divided by the volume of the mixture. [Allotrope]
    
NumberConcentration_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000176")
# Number concentration is a concentration defined by number of entities of a constituent in a mixture divided by the volume of the mixture. [IUPAC]
    
DilutionRatio = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000177")
# The dilution ratio is the ratio of solute to solvent. [Wikipedia]
    
DilutionFactor_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000178")
# Dilution factor is the ratio of the aliquot volume to the final volume. [Wikipedia]
    
Amount_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000179")
# The amount is the quality of a whole that is the number of entities that are part of the whole. [Allotrope]
    
NumberDensity = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000180")
# Number density is a quality of the amount of countable objects per units size. [Allotrope]
    
SignalConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000200")
# A signal configuration is a device configuration of a device producing or consuming signals, that controls the processing of a signal. [Allotrope]
    
SignalGainConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000201")
# A gain setting is a signal configuration, that controls the amplification of an incoming or outgoing signal. [Allotrope]
    
SignalOffsetConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000202")
# A signal offset configuration is a signal processing configuration, that adds/subtracts a fixed amount of magnitude to the signal strength or amplitude to move the zero reference. [Allotrope]
    
ControllerConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000204")
# A controller configuration is a device configuration of a controller, that directly influences the controlling process done by the controller towards a goal. [Allotrope]
    
TriggerConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000205")
# A trigger configuration is a device configuration for a system with a sensor and an actor component, that directly influences when the sensor sends an activating signal to the actor based on an observation. [Allotrope]
    
NotificationConfiguration = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000206")
# A notification setting is a trigger setting in a system that has a notification component, that controls when the component send out a notification signal. [Allotrope]
    
PartialPressure_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000208")
# Partial pressure is the notional pressure of a gas in a mixture of gases, if it alone occupied the entire volume of the original mixture at the same temperature. [Wikipedia]
    
Purity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000209")
# Purity is a composition quality inhering in an bearer by virtue of the bearer lacking undesired components. [Allotrope]
    
MechanicalQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000210")
# A physical quality that inheres in an bearer by virtue of how that bearer behaves when subjected to forces or displacements and the effect of their bodies on their environment. [Wikipedia]
    
Strain_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000211")
# Strain is a quality of deformation representing the displacement between particles in the body relative to a reference length. [Wikipedia]
    
ShearStress_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000212")
# A shearing force is applied to the top of the rectangle while the bottom is held in place. The resulting shear stress deforms the rectangle into a parallelogram. The area involved would be the top of the parallelogram. A shear stress is the component of stress coplanar with a material cross section. [Wikipedia]
    
NormalStrain = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000213")
# A normal strain is strain perpendicular to the face of an element. [Wikipedia]
    
ShearStrain = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000214")
# A shear strain is parallel to the face of an element. [Wikipedia]
    
TotalImpurities = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000215")
# Total impurities is a composition quality that is the sum of the mass of all impurities in a material. [Allotrope]
    
StereochemicalPurity = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000216")
# A purity quality of a material with respect to its stereoisomers. [Allotrope]
    
DiastereomericExcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000217")
# The absolute value of the mole fraction for one diastereomer in a mixture minus the mole fraction for the other. [CHMO]
    
DiastereomericRatio = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000218")
# The ratio of the percentage of one diastereomer in a mixture to that of the other. [CHMO]
    
EnantiomericRatio = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000219")
# The ratio of the percentage of one enantiomer in a mixture to that of the other. [CHMO]
    
EnantiomericExcess = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000220")
# The absolute value of the mole fraction for one enantiomer in a mixture minus the mole fraction for the other enantiomer. [CHMO]
    
Excess = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000221")
# An excess  is a relational quality that is the difference in magnitude of two qualities of the same kind. [Allotrope]
    
Impurity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000222")
# Impurity is a composition quality inhering in an bearer by virtue of the bearer having undesired components. [Allotrope]
    
StereochemicalComposition = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000223")
# Stereochemical composition is a composition quality based on the stereochemistry of its components. [Allotrope]
    
DilutionComposition = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000224")
# A dilution composition is a composition quality of a dilution. [Allotrope]
    
ReactionComposition = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000225")
# Reaction composition is a composition quality of a reaction mixture. [Allotrope]
    
Conversion_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000226")
# Conversion is a reaction composition quality dependent on the fraction of reactant remaining. [Allotrope]
    
Yield_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000227")
# Reaction yield is a reaction composition quality expressed as a percentage of the theoretical maximum mass of the product given the masses of the reactants. [CHMO, Allotrope]
    
ReactionSelectivity = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000228")
# Reaction selectivity is a reaction composition that is expressed as the number of moles of desired product per the number of moles of undesired product. [Wikipedia]
    
Wavenumber_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000235")
# Wavenumber is a physical quality that inheres in a wave by virtue of the number of wave patterns per unit length along the direction of propagation. It is reciprocal to wavelength. [Allotrope]
    
Resolution_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000237")
# Resolution is the quality of a sensor (measurement instrument, detector) to be able to measure the smallest change in a qualities that causes a perceptible change in the corresponding indication. [Allotrope]
    
MeltingPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000238")
# The melting point is the temperature where a material changes from the solid phase to the liquid phase. [Allotrope]
    
Polarity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000242")
# Polarity is the quality inhered in an energy that is the positive or negative direction of an electrical, acoustical, or magnetic force relative to a reference state. [Allotrope, NCI]
    
PoreSize = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000244")
# The average radius of the pores within the solid particles. [Allotrope]
    
FusedCore = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000245")
# A porosity quality inhering in a bearer by virtue of the bearer&apos;s being only capable of admitting the passage of gas or liquid through pores or interstices in outer layer of the solid and not its solid impermeable core. [Allotrope]
    
ChemicalSubstanceQuality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000250")
# A chemical substance quality is a quality that inheres in some portion of chemical substance. [Allotrope]
    
Energy_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000253")
# Energy (quality) is the amount of energy that a material entity contains. [Allotrope]
    
ElectricResistivity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000266")
# Electric resistivity is the quality of the electric field strength divided by the current density when there is no electromotive force in a conductor. [IUPAC]
    
ElectricConductance_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000267")
# Electric conductance is the quality inhered in a conductor that is the reciprocal of a the electric resistance. [IUPAC]
    
Enthalpy_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000269")
# Enthalpy (quality) is the quality of a system that is the internal energy of the system plus the product of pressure and volume. Its change in a system is equal to the heat brought to the system at constant pressure. [IUPAC]
    
SpecificHeatCapacity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000271")
# A specific heat capacity (quality) is a heat capacity of a pure substance by virtue of the amount of heat necessary to raise the temperature per amount of mass. [Allotrope]
    
ElectricCharge_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000273")
# Electric charge is the electrical quality of matter that causes it to experience a force when placed in an electromagnetic field. [Wikipedia]
    
SaturationVaporPressure_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000275")
# The pressure exerted by a pure substance (at a given temperature) in a system containing only the vapor and condensed phase (liquid or solid) of the substance. [IUPAC]
    
Hygroscopicity = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000279")
# Hygroscopicity is a quality inhered in a compound by virtue of its ability to readily take up and retain water, especially from the atmosphere. [Wikipedia]
    
EnthalpyOfFusion_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000280")
# The enthalpy of fusion is a quality inhered in of a solid substance that is the change in its enthalpy resulting from providing energy, typically heat, to a specific quantity of the substance to change its state from a solid to a liquid, at constant pressure. [Wikipedia]
    
EnthalpyOfVaporization_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000281")
# The enthalpy of vaporization is a quality inhered in a liquid substance that is the amount of energy (enthalpy) that must be added to the liquid substance, to transform a quantity of that substance into a gas. [Wikipedia]
    
SpecificEnthalpyOfVaporization_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000282")
# The specific enthalpy of vaporization is the enthalpy of vaporization referenced to a unit mass of substance. [Allotrope]
    
MolarEnthalpyOfVaporization_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000283")
# The molar enthalpy of vaporization is the enthalpy of vaporization referenced to a unit amount of substance. [Allotrope]
    
MolarEnthalpyOfFusion_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000284")
# The molar enthalpy of fusion is the enthalpy of fusion referenced to a unit amount of substance. [Allotrope]
    
SpecificEnthalpyOfFusion_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000285")
# The specific enthalpy of fusion is the enthalpy of fusion referenced to a unit mass of substance. [Allotrope]
    
EnthalpyOfSublimation_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000286")
# The enthalpy of sublimation is a quality inhered in a solid substance that is the amount of energy (enthalpy) that must be added to the solid substance, to transform a quantity of that substance into a gas. [Wikipedia]
    
SpecificEnthalpyOfSublimation_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000287")
# The specific enthalpy of sublimation is the enthalpy of sublimation referenced to a unit mass of substance. [Allotrope]
    
MolarEnthalpyOfSublimation_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000288")
# The specific enthalpy of sublimation is the enthalpy of sublimation referenced to a unit amount of substance. [Allotrope]
    
CountFraction_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000291")
# The count fraction is a quality pertaining the number of particles of a constituent divided by the total number of particles of all constituents in the mixture. [Allotrope]
    
RefractiveIndex_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000292")
# The refractive index is an optical quality inhered in a material by virtue of how fast light travels through the material. [Allotrope]
    
Birefringence_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000295")
# An optical quality of anisotropic material that has a refractive index which depends on the properties of light. [Allotrope]
    
Gain = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000297")
# Signal gain is the ratio of magnitude of a quality between a flow of energy incoming to a system (input signal) and the outgoing flow of energy (output signal) used for signaling. [Allotrope]
    
CircularBirefringence_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000316")
# Circular birefringence is the angle through which plane polarized light is rotated clockwise, as seen when facing the light source, in passing through an optically active medium. [IUPAC]
    
SpecificRotation_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000317")
# Specific rotation is the change in orientation of monochromatic plane-polarized light, per unit distance–concentration product, as the light passes through a sample of a compound in solution. [Wikipedia]
    
TemperatureRate_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000318")
# A temperature rate is a thermal quality which describes the change in temperature over time in some material bearer. [Allotrope]
    
RelativePermittivity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000321")
# Relative permittivity is an electrical and magnetic quality inhered in a medium that is the ratio of the electric field strength in vacuum to that in the medium. [IUPAC]
    
ThermalConductance_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000323")
# Thermal conductance is the quality inhered in a conductor that is the reciprocal of the thermal resistance. [IUPAC]
    
Luminescence_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000325")
# Luminescence is an optical quality inhering in a bearer by virtue of the bearer&apos;s spontaneous emission of radiation from an electronically or vibrationally excited species not in thermal equilibrium with its environment. [IUPAC]
    
Angle_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000326")
# An quality inhering in a bearer by virtue of the bearer&apos;s placement at an angle. [PATO]
    
ParticleDensity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000327")
# Particle density is the number density of a population of particles. [Allotrope]
    
CumulativeParticleDensity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000328")
# A cumulative particle density is the number density of particles meeting a given criterion. [Allotrope]
    
DifferentialParticleDensity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000329")
# A differential particle density is the number density of particles within a specified range criterion. [Allotrope]
    
VerticalPosition_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000333")
# A vertical position is a position in a vertical spacial direction. [Allotrope]
    
AboveOf_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000334")
# Above of is a vertical position if the bottom of the bearer&apos;s spatial extend along the vertical dimension is higher then then the top of the other. [Allotrope]
    
BelowOf_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000335")
# Below of is a vertical position if the top of the bearer&apos;s spatial extend along the vertical dimension is higher then then the bottom of the other. [Allotrope]
    
ElectricImpedance_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000339")
# Electric impedance is the quality inhered in a conductor that is the complex representation of potential difference divided by the complex representation of the current. [IUPAC]
    
Stress_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000340")
# Stress is a mechanical quality representing the internal forces that neighboring particles of a continuous material exert on each other. [Wikipedia]
    
YoungModulus_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000341")
# A Young modulus is the ratio of tensile stress to tensile strain of a material. [Allotrope]
    
Eccentricity_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000346")
# The eccentricity of a conic section is a non-negative real number that uniquely characterizes its shape. [Wikipedia]
    
Height_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000347")
# A 1-D extent quality inhering in a bearer by virtue of the bearer&apos;s vertical dimension of extension. [PATO]
    
DielectricPolarization_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000348")
# Dielectric polarization is the quality inhered in a dielectric that is the difference between the electric displacement vector and the product of the electric field strength with the permittivity of vacuum. [IUPAC]
    
Gloss_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000349")
# Gloss is an optical property which indicates how well a surface reflects light in a specular (mirror-like) direction. [Wikipedia]
    
RelativeResponse_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000353")
# A relative response is the ratio of an analytes device response signal to the device response signal of some reference material. [Allotrope]
    
RotationalSpeed_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000359")
# A rotational speed is a movement quality inhering in a bearer by virtue of the bearer&apos;s frequency of rotation. [Allotrope]
    
Action = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000001")
# An action is a unit element in a procedure and is a concretization of an action specification. [Allotrope]
    
Procedure = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000002")
# A procedure is plan containing multiple activities that are intended to be executed in an order following a procedure specification. [Allotrope]
    
Situation = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000003")
# Portion of reality that is realized in some process. [Allotrope]
    
Configuration = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000004")
# A specific combination of qualities that the bearer realizes at some time. [Allotrope]
    
EnvironmentalSituation = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000005")
# A situation that is realized in a processes outside the system boundary of an operation situation of a device. [Allotrope]
    
OperationalSituation = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000006")
# The situation when a device is performing its intended function. [Allotrope]
    
Transition = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000007")
# A transition is a situation that is realized when one or more preceding processes end and the one or more succeeding processes begin. [Allotrope]
    
Trigger = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000008")
# A realizable entity that when realized coincides with the start of some intended or causally dependent process. [Allotrope]
    
ChemicalDisposition = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000011")
# A disposition of a portion of material to react with other materials in a specific way by nature of its chemical composition. [Allotrope]
    
Detergent = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000012")
# A surfactant (or a mixture containing one or more surfactants) disposed to having cleaning properties in dilute solutions. [ChEBI]
    
Surfactant = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000013")
# The disposition to lower the surface tension of the medium in which the material is dissolved, and/or the interfacial tension with other phases, and, accordingly, is positively adsorbed at the liquid/vapor and/or at other interfaces. [ChEBI]
    
ChemicalReactionDisposition = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000015")
# A chemical reaction disposition is a disposition inhered in a reaction mixture. [Allotrope]
    
ReactionSelectivityDisposition = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000016")
# A reaction selectivity disposition is a disposition of a reaction mixture to have a reaction selectivity. [Allotrope]
    
Hysteresis = onto.search_one(iri="http://purl.allotrope.org/ontologies/realizable#AFRE_0000019")
# Hysteresis is the time-based dependence of a system&apos;s output on present and past inputs. The dependence arises because the history affects the value of an internal state. To predict its future outputs, either its internal state or its history must be known. [Wikipedia]
    
AugerSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000001")
# A plot of intensity vs. kinetic energy obtained when a high energy photon ionizes a core electron and an electron from a higher energy level descends to take its place, releasing sufficient energy to eject a second so-called &apos;Auger&apos; electron. [CHMO]
    
DifferentialScanningCalorimetryCurve = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000007")
# A plot of enthalpy vs. temperature obtained by measuring the enthalpy required to increase the temperature of a sample as a function of temperature. [CHMO]
    
MicrowaveSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000020")
# A plot of emission vs. wavelength obtained through a Fourier transform of the time series of the radiation emitted by a sample of gas phase molecules that have been excited by a microwave-frequency pulse. [CHMO]
    
ConversionSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000044")
# A plot of a quantity related to the absorption, for example absorbance or cross section, multiplied by the quantum yield for the process considered against a measure of photon energy such as frequency, wavenumber or wavelength. [CHMO]
    
PhotoelectronSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000046")
# A plot of photoelectron count vs. kinetic energy. [CHMO]
    
CircularDichroismSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000053")
# A plot of ellipticity vs. wavelength obtained by measuring the differential absorption of left- and right-handed circularly polarized photon radiation as a function of wavelength. [CHMO]
    
StructureData = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000064")
# Data obtained from a structure determination method. [CHMO]
    
Voltammogram = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000070")
# A plot of cell current vs. the potential between the indicator and reference electrodes obtained from a voltammetry experiment. [CHMO]
    
ChemicalMap = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000090")
# A data set derived from chemical imaging consisting of a three-dimensional image where two axes describe the x and y spatial dimensions and the third dimension represents spectral wavelength. The image is obtained by stacking one image per spectral wavelength sequentially. [CHMO]
    
IsothermalTitrationCalorimetryCurve = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000091")
# A plot of energy vs. time obtained from the measurement of the heat evolved during a chemical or biochemical reaction (such as protein--receptor binding). [CHMO]
    
Electropherogram = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000133")
# An electropherogram is the outcome of a capillary electrophoresis that reports the response of a detector as a function of time. [Allotrope]
    
FluorescenceEmissionSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000136")
# A plot of intensity against wavelength obtained by measuring the amount of radiation emitted by a sample through fluorescence against the frequency of the incident radiation. [CHMO]
    
ExcitationSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000146")
# An excitation spectrum is a plot of the spectral radiant exitance or of the spectral photon exitance against the frequency (or wavenumber, or wavelength) of excitation. [IUPAC]
    
PhotoacousticSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000164")
# A plot of intensity vs. wavelength obtained by measuring the sound emitted when a gaseous sample is exposed to an intense laser beam, which is rapidly interrupted by a rotating slotted disk. [CHMO]
    
DataPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000186")
# A data point is the single point in a coordinate space. [Allotrope]
    
PeakGroup = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000231")
# A peak group is a user defined set of peaks for which summed peak facet data is expected. [Allotrope]
    
Chromatogram = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000236")
# A chromatogram is a distribution function of a detector signal (such as ion count or absorbance) versus time of acquisition or versus volume of analyte. [Allotrope]
    
InfraredSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000251")
# A plot of absorbance or transmittance vs. wavelength/wavenumber/frequency obtained by measuring the absorption or transmission of infrared radiation by a sample. [CHMO]
    
NuclearMagneticResonanceSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000263")
# Any spectrum that shows the response of spin-active nuclei to radio frequency radiation in an applied magnetic field. [CHMO]
    
OpticalExtinctionSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000284")
# A plot of extinction (or transmittance) vs. wavelength (or wavenumber) obtained by measuring the amount of radiation transmitted through a sample as a function of the wavelength of the incident radiation. Optical extinction spectra can also be derived theoretically. [CHMO]
    
AtomicSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000289")
# A plot of absorption or emission  radiation vs. frequency that reflects the internal degrees of freedom of an atom, obtained in an experiment where the sample is vaporized and then atomized. [CHMO]
    
InelasticTunnelingSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000294")
# A plot of current (or a first or higher derivative of current with respect to voltage) vs. voltage obtained by measuring the tunneling current through a metal-oxide-metal sandwich. Molecules are adsorbed onto the oxide and these molecules can affect the tunneling via the excitation of vibrational states. [CHMO]
    
MeltingCurve = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000297")
# A melting curve is the data distribution function over temperature that is the output of a melting curve analysis. Melting curve analysis is an assessment of the dissociation characteristics of double-stranded DNA during heating. As the temperature is raised, the double strand begins to dissociate leading to a rise in the absorbance intensity, hyperchromicity. [Wikipedia]
    
Certificate = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000304")
# A certificate refers to the confirmation of certain characteristics of an object, person or organization. This confirmation is often, but not always, provided by some form of external review, education, assessment, or audit. Accreditation is a specific organization&apos;s process of certification. [Wikipedia]
    
ActionSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000319")
# A plot of a relative biological or chemical photoresponse per number of incident photons against wavelength or energy of radiation under the same radiant power of light. [CHMO]
    
OximetrySpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000323")
# A plot of % oxygen vs. time, measured during a process where oxygen is consumed or evolved. [CHMO]
    
AcousticEmissionSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000325")
# A plot of decibels  vs. frequency obtained by measuring the amount of noise generated by a sample as a function of frequency of incident radiation. [CHMO]
    
FlowCurve = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000336")
# A plot of stress vs. flow rate obtained from rheological measurements. [CHMO]
    
TaucPlot = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000373")
# A plot of e vs hv where e is the molar extinction coefficient, that is used to determine the optical gap (or &apos;Tauc gap&apos;) in amorphous thin film materials. [CHMO]
    
Peak = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000413")
# A peak describes a part of a data distribution function at a definite range of the experimental parameter (independent variable) of the distribution function. This definition includes  a single data point of the distribution function. [Allotrope]
    
ElectromagneticRadiationSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000417")
# The electromagnetic radiation spectrum is the range of frequencies (the spectrum) of electromagnetic radiation and their respective wavelengths and photon energies. [Wikipedia]
    
PeakList = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000432")
# Collection of peaks or peak groups for a specific purpose. [Allotrope]
    
IncidentPhotonConversionEfficiencySpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000438")
# A plot of incident photon-to-current conversion efficiency (IPCE) vs. wavelength obtained from a solar or photovoltaic cell. [CHMO]
    
MassSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000439")
# A mass spectrum is a data distribution function that plots the relative abundances of ions forming a beam or other collection as a function of their m/z values. [IUPAC]
    
TitrationCurve = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000490")
# A plot of volume of titrant vs. an independent variable (e.g., pH or enthalpy) obtained from a titration experiment. [CHMO]
    
LuminescenceSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000491")
# A plot of intensity against wavelength obtained by measuring the amount of radiation emitted by a sample through luminescence against the frequency of the incident radiation. [CHMO]
    
MossbauerSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000496")
# A plot of intensity vs. velocity obtained by measuring the intensity and kinetic energy of a beam of gamma-rays transmitted through a solid sample. [CHMO]
    
ElectronicAbsorptionSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000514")
# A plot of absorbance vs. wavelength, obtained by measuring the amount of radiation absorbed by a sample as a function of the wavelength of incident radiation, which reflects the electronic degrees of freedom of an atom or molecule. [CHMO]
    
RamanSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000519")
# A plot of intensity vs. Raman shift (cm-1) obtained by measuring the Raman scattering of monochromatic light from a sample. [CHMO]
    
TotalIonCurrentProfile = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000580")
# A total ion current profile is a data distribution function of the total ion current recorded as function of time or time dependent sampling. [Allotrope]
    
Prediction = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000694")
# A prediction or forecast is a proposition about a future event. [Wikipedia]
    
CalibrationCurve = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000788")
# The calibration curve is a data distribution function of the instrumental response, the so-called analytical signal, changed with the concentration of the analyte (the substance to be measured). [Wikipedia]
    
AnalysisSequence = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000894")
# Linear procedure specification that specifies analysis. [Allotrope]
    
AnalyticalMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000895")
# An analysis method is a plan specification that specifies an analysis. [Allotrope]
    
CubicInterpolationAlgorithm = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000896")
# An interpolation algorithm using cubic polynomials. [Allotrope]
    
InterpolationAlgorithm = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000898")
# An interpolation algorithm is an algorithm about interpolation that specifies the way an interpolation process is carried out. [Allotrope]
    
LinearInterpolationAlgorithm = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000899")
# Linear interpolation is a method of curve fitting using linear polynomials to construct new data points within the range of a discrete set of known data points. [Wikipedia]
    
Log = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000900")
# A log is a list of related log entries. [Allotrope]
    
LogEntry = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000901")
# A log entry is a list item representing a recorded event. [Allotrope]
    
QualityProfileControlCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000902")
# A quality profile control command is an action specification about a quality process profile. [Allotrope]
    
LevelOfMeasurement = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000908")
# Level of measurement is a classification that describes the nature of information within the values assigned to variables. [Wikipedia]
    
NominalScale = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000909")
# A classification that only introduces categorical values. [Allotrope]
    
OrdinalScale = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000910")
# A classification of measurement that introduces equality and rank-ordering. [Allotrope]
    
IntervalScale = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000911")
# A scale that is based on equal quantitative intervals. [Allotrope]
    
RatioScale = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000912")
# A scale that introduces a zero as origin and allows equality, rank-ordering, equality of intervals and equality of ratios. [Allotrope]
    
CyclicScale = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000914")
# A cyclic scale is a type of measurement scale that classifies values based on recurring intervals. [Allotrope]
    
Counts = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000915")
# Counts are like ratio scale that they have a zero point but there are no meaningful fractional units. [Allotrope]
    
Classification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000916")
# A classification is a proposition that categorizes things into classes or collections of things differentiated by some criteria. [Allotrope]
    
Identifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000917")
# An identifier is a name that identifies (that is, labels the identity of) either a unique object or a unique class of objects, where the &quot;object&quot; or class may be an idea, physical [countable] object (or class thereof), or physical [uncountable] substance (or class thereof). [Wikipedia]
    
GloballyUniqueIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000918")
# A globally unique identifier is an identifier whose uniqueness is guaranteed in a decentralized way by following a certain algorithm in its creation. [Allotrope]
    
LocalIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000919")
# An identifier that uniquely denotes objects only within the scope of a specific object aggregate and that is not registered in an identifier registry. [Allotrope]
    
QuantityRange = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000920")
# A range that describes a range of quantity values using the same unit. [Allotrope]
    
ListIndex = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000921")
# A list index is a type of index that is related to a list item in a collection. [Allotrope]
    
Description = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000922")
# A description is a proposition about an existing entity. [Allotrope]
    
Facet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000923")
# A facet is a partial information that contains an aspect of some information content entity or parts of it when participating in some process. The facet abstracts of the concrete representation of this aspect of information. [Allotrope]
    
Factor = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000924")
# A multiplicand in a mathematical product expression. [Allotrope]
    
ComplexFactor = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000925")
# A factor with a complex number as value. [Allotrope]
    
IntegerFactor = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000926")
# A factor with a integer number as value. [Allotrope]
    
RealFactor = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000927")
# A factor with a real number as value. [Allotrope]
    
Index = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000928")
# A facet that represents some strictly ordered key in an associative array or the position of a member in a list. [Allotrope]
    
MatrixIndex = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000929")
# An index that denotes some matrix component. [Allotrope]
    
TensorIndex = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000930")
# An index that denotes some tensor component. [Allotrope]
    
VectorIndex = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000931")
# An index that denotes some vector component. [Allotrope]
    
Order = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000932")
# An order facet adds information of the ordering of some information in an aggregation of information. [Allotrope]
    
Predecessor = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000933")
# A predecessor is an order facet of an information content entity that refers to the information content entity immediately before it in a containing list. [Allotrope]
    
Successor = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000934")
# A successor is an order facet of an information content entity that refers to the information content entity immediately after it in a containing list. [Allotrope]
    
Radix = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000935")
# In mathematical numeral systems, the radix or base is the number of unique digits, including zero, used to represent numbers in a positional numeral system. [Wikipedia]
    
Size = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000936")
# Size is the number of members of some collection of data. [Allotrope]
    
Time = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000937")
# A time is a facet that adds temporal information to an information content entity about the point in time when the information content entity it is participating in the some process. [Allotrope]
    
ProcedureSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000938")
# A specification on the order, transitions and trigger of multiple action specifications that are part of some aggregate action specification. [Allotrope]
    
PolynomialInterpolationAlgorithm = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000939")
# An interpolation algorithm using polynomials. [Allotrope]
    
QuadraticInterpolationAlgorithm = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000940")
# An interpolation algorithm using cubic polynomials. [Allotrope]
    
ActionSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000941")
# A directive information entity that describes an action the bearer will take. [IAO]
    
ProcessCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000942")
# An action specification that specifies an event within a process when the specified activity is realized. [Allotrope]
    
FunctionSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000944")
# A specification that specifies a participant in a process by the function it bears in it. [Allotrope]
    
SequentialProcedureSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000945")
# A procedure specification with a linear ordered collection of action specifications. [Allotrope]
    
PeakFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000947")
# A facet that is part of a peak. [Allotrope]
    
PeakHeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000948")
# A peak facet that denotes the ordinate value of the peak apex offset by the baseline ascribed to the peak. [Allotrope]
    
RelativePeakHeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000949")
# A peak facet that denotes the height of the peak relative to some other peak or summation of peaks. [Allotrope]
    
StepSize = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000950")
# The difference between two discrete points next to each other in a range of discrete values. [Allotrope]
    
Duration = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000951")
# A measure of the magnitude of the time region in which the process occurs. [Allotrope]
    
MeasurementTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000952")
# The date/time of the measurement. [Allotrope]
    
ProcessProperty = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000953")
# A description of a fundamental characteristic of a process. [Allotrope]
    
Rate = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000954")
# A measure of the magnitude of change of some participating entity per amount of time relative to other processes having similar changes. [Allotrope]
    
Observation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000955")
# An observation is a description of a portion of reality that has been observed during an observing process. [Allotrope]
    
NumberOfSampledPoints = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000956")
# The number of points is the total number of points sampled during a measurement. [Allotrope]
    
Specification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000957")
# A specification is a proposition about the intended purpose or design of an entity. [Allotrope]
    
TensorDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000958")
# In mathematics, tensors are geometric objects that describe linear relations between geometric vectors, scalars, and other tensors. Elementary examples of such relations include the dot product, the cross product, and linear maps. The tensor datum is a facet that uses a tensor as an abstract mathematical description. [Wikipedia]
    
MatrixDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000960")
# In mathematics, a matrix (plural matrices) is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns. [Wikipedia]
    
ScalarDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000961")
# A scalar is an element of a field which is used to define a vector space. [Wikipedia]
    
VectorDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000962")
# In mathematics, physics, and engineering, a Euclidean vector (sometimes called a geometric or spatial vector, or—as here—simply a vector) is a geometric object that has magnitude (or length) and direction. [Wikipedia]
    
VectorIntegerDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000963")
# A number vector datum is a vector datum that has only integer scalar components. [Allotrope]
    
VectorNumberDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000964")
# A vector number datum is a vector datum that has only numeric scalar components. [Allotrope]
    
VectorQuantityDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000965")
# A vector quantity datum is a vector datum that has only quantity value scalar components. [Allotrope]
    
TimeDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000966")
# A time datum is a type of datum that quantifies a duration of time or is about a time interval. [Allotrope]
    
ScalarRangeDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000967")
# A scalar range datum is a type of datum that is about range quantified by a scalar value. [Allotrope]
    
QualitySpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000975")
# A specification that specifies the determinate range of some quality. [Allotrope]
    
CapabilitySpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000976")
# A capability specification specifies some function that the target of the specification inheres. This capability can be restricted to a specific situation. [Allotrope]
    
ParameterSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000977")
# A participant specification which specifies an information object that has the contextual role of a parameter in the realized process. [Allotrope]
    
ResultSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000978")
# A participant specification that specifies a information objects that have the contextual role of a result in the realized process. [Allotrope]
    
RoleSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000979")
# A specification that specifies a participant in a process by the general role it plays in it. [Allotrope]
    
TransitionSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000980")
# A specification about the transition between two or more actions. [Allotrope]
    
TriggerSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000981")
# A trigger specification is a situation specification that specifies a trigger. [Allotrope]
    
SituationSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000982")
# A specification of a circumstances (process). [Allotrope]
    
ScalarIntegerDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000983")
# A datum that is an integer value. [Allotrope]
    
ScalarDecimalDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000985")
# A datum that is a decimal value. [Allotrope]
    
ScalarFloatingPointNumberDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000986")
# A datum that is a IEEE floating point value. [Allotrope]
    
ScalarCategoricalDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000987")
# A scalar categorical datum is a type of datum that describes something based on a scalar value for a kind of category. [Allotrope]
    
ScalarNumberDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000988")
# A scalar datum that has a numeric value. [Allotrope]
    
ScalarQuantityDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000989")
# A scalar quantity datum is a type of datum that is about a quantity and quantifies by a scalar value. [Allotrope]
    
Proposition = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000991")
# A proposition is an information content entity that is statement or assertion that has a truth value. [Allotrope]
    
RepresentationForm = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000992")
# A representation form is a type of information content entity that represents an entity in a certain way. [Allotrope]
    
Model = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000993")
# A model is a purposeful simplified description of a part of reality that focuses on specific aspects. [Allotrope]
    
Theory = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000994")
# A model that explains some principle rules about something. [Allotrope]
    
PhysicalDomain = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000995")
# A physical domain is a type of description that covers physical objects. [Allotrope]
    
ParticipantSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001005")
# A specification that is part of some action specification that specifies some continuant that when the concretized action is realized becomes a participant playing some (contextual) role in the process. [Allotrope]
    
Isobar_nuclide = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001043")
# Isobar is a classification facet that classifies atoms (nuclides) of different chemical elements that have the same number of nucleons. Correspondingly, isobars differ in atomic number (or number of protons) but have the same mass number. [Wikipedia]
    
Tuple = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001046")
# A tuple is a finite ordered list (sequence) of elements. [Wikipedia]
    
MathematicalObject = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001054")
# A mathematical object is an information content entity that is an abstraction in the area of mathematics. It has a formal definition that allows for deductive reasoning and mathematical proofs. [Allotrope]
    
ConfigurationSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001058")
# A configuration specification is a situation specification that is about a realized configuration inhered in a specification target. [Allotrope]
    
Registry = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001059")
# A registry is information content entity that is an aggregate of designations. [Allotrope]
    
DataDistributionFunction = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001060")
# A description of distribution of a quantity with respect to a set of parameters. [Allotrope]
    
MolecularStructure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001072")
# A molecular structure is a description of the type and arrangement of the atoms and the direction of bonds linking atoms that constitute a molecule. [Allotrope]
    
PeakArea = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001073")
# A peak facet that quantitates the area enclosed by a peak and the selected baseline. [Allotrope]
    
PeakPosition = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001074")
# A peak facet that denotes the abscissa value of the extrema (maxima or minima) attributed to the peak in a data description function.  The extrema is often determined through a mathematical fitting of measurement signals to eliminate spurious extrema due to noise. [Allotrope]
    
PeakWidth = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001075")
# A peak facet denoting its width at a specified peak height or variance. [Allotrope]
    
PeakAsymmetry = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001088")
# A peak facet that describes the deviation of the peak&apos;s distribution from symmetry about its mean. [Allotrope]
    
Slope = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001090")
# Slope is a mathematical facet of a line that describes both the direction and the steepness of the line. [Wikipedia]
    
Point = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001092")
# A point is a two-dimensional figure that represents a zero-dimensional spacial region. [Allotrope]
    
FigureFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001093")
# A figure facet is a facet that is part of a figure. [Allotrope]
    
Assignment = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001094")
# An assignment is a proposition that is an assertion of some relation between entities. [Allotrope]
    
Timebase = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001095")
# A timebase is a description that is about a point in time (process boundary or zero dimensional temporal region) that has the role of a temporal reference. [Allotrope]
    
MathematicalFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001100")
# A facet that is part of a mathematical expression, formula or equation. [Allotrope]
    
QuantificationFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001101")
# A facet that is part of a quantification of a quality, aggregate or process. [Allotrope]
    
Capability = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001103")
# A capability is a proposition that is about a function, role or quality realized under given conditions. [Allotrope]
    
ScalarDoubleDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001104")
# A scalar double datum is a scalar floating point number datum having a IEEE double precision datum (xsd:double). [Allotrope]
    
MeasurementMetadata = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001117")
# Measurement metadata is a facet that is part of a information content entity about a measurement that is about the context of the measurement, but not directly about the measurement result or a measurement parameter. [Allotrope]
    
Ph = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001142")
# pH (datum) is a quantity facet that quantifies the acidity or basicity of an aqueous solution, defined as the decadic logarithm of the reciprocal activity of hydrogen ions. [Allotrope]
    
Absorbance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001157")
# Absorbance is a quantity facet that quantifies the absorbance as logarithm to the base 10 (linear absorbance) of the incident (prior to absorption) spectral radiant power, divided by the transmitted spectral radiant power. [IUPAC]
    
AcquisitionTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001158")
# The acquisition time is the time when a signal is captured. [Allotrope]
    
Wavelength = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001159")
# A wavelength is a facet that quantifies a wavelength of electromagnetic radiation. [Allotrope]
    
RelativePeakArea = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001165")
# A peak facet that denotes the area of the peak relative to some other peak or summation of peaks. [Allotrope]
    
PeakName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001167")
# A peak name is a written name that denotes some peak. [Allotrope]
    
PeakIndex = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001168")
# A peak index is an index that denotes a peak in a list of peaks. [Allotrope]
    
PeakAnalyteAmount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001171")
# A peak facet that quantitates the amount of analyte attributed to the peak based on a calibration curve, response factor or other quantitative formula. [Allotrope]
    
RelativePeakAnalyteAmount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001172")
# A peak facet that denotes the amount of analyte ascribed to a  the peak relative to the amount of some other analyte or summation of analytes. [Allotrope]
    
PeakPolarity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001173")
# A peak facet that indicates whether the response curve of the peak is above or below the signal baseline. [Allotrope]
    
PeakStart = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001178")
# A peak facet that denotes the first value of the abscissa that belongs to the peak. [Allotrope]
    
PeakValueAtStart = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001179")
# A peak facet that denotes the first value of the ordinate that belongs to the peak. [Allotrope]
    
PeakEnd = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001180")
# A peak facet that denotes the last value of the abscissa that belongs to the peak. [Allotrope]
    
PeakValueAtEnd = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001181")
# A peak facet that denotes the last value of the ordinate that belongs to the peak. [Allotrope]
    
PeakBaselineStartCode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001182")
# A peak facet that describes the peak start boundary with respect to the signal, integration determined signal baseline or a neighboring peak. [Allotrope]
    
PeakBaselineEndCode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001183")
# A peak facet that describes the peak end boundary with respect to the signal, integration determined signal baseline or a neighboring peak. [Allotrope]
    
BaselineValueAtStartOfPeak = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001184")
# A peak facet that denotes the ordinate value of the baseline of a peak at the peak start time. [Allotrope]
    
BaselineValueAtEndOfPeak = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001185")
# A peak facet that denotes the ordinate value of the baseline of a peak at the peak end time. [Allotrope]
    
PeakPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001186")
# A peak point is a data point that is a member of a peak. [Allotrope]
    
PeakStartPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001189")
# The peak start point is the data point of the peak with the smallest abscissa value. [Allotrope]
    
PeakEndPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001190")
# The peak start point is the data point of the peak with the largest abscissa value. [Allotrope]
    
PeakMaximumPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001191")
# The peak maximum point is the data point of the peak with the largest ordinate value. [Allotrope]
    
TupleItem = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001192")
# A tuple item is an object in a tuple. [Allotrope]
    
PeakResolution = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001199")
# A peak facet that measures the degree of separation between the peak and another specified peak. [Allotrope]
    
PeakMinimumPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001201")
# The peak minimum point is the data point of the peak with the smallest ordinate value. [Allotrope]
    
PeakExtremumPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001202")
# The peak extremum point is the data point of the peak with the largest or smallest ordinate value. [Allotrope]
    
StatisticalPopulation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001209")
# In statistics, a population is a set of similar items or events which is of interest for some question or experiment. A statistical population can be a group of existing objects or a hypothetical and potentially infinite group of objects conceived as a generalization from experience. [Wikipedia]
    
StatisticalSampleSet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001210")
# A statistical sample set is a description of a subset of the statistical population, that is chosen to represent the population in a statistical analysis. [Wikipedia]
    
Partition = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001211")
# A partition is a collection that is an aggregate part of a larger collection. Each member of the partition is also a member of the larger collection. [Allotrope]
    
DescriptiveStatistic = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001212")
# A descriptive statistic is a summary statistic that quantitatively describes or summarizes features of a collection of information. [Wikipedia]
    
SummaryDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001213")
# A summary datum is a facet of a collection that is about summary information about features of the members of the collection, such as descriptive statistics in order to communicate the largest amount of information as simply as possible. [Allotrope]
    
Position = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001216")
# The position is the location of a physical entity. [Allotrope]
    
CalibrationPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001217")
# A calibration point is a single calibration result at a specific test point (one or more reference values). [Allotrope]
    
FormulationDescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001218")
# The formulation of a material is a data object that describes its composition of ingredients. [Allotrope]
    
Baseline = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001219")
# An information content entity that describes the background (offset) component of a signal not due to the analyte (peak) of interest. [Allotrope]
    
ControlSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001243")
# A control setting is a setting that controls how a process is executed by some system. [Allotrope]
    
AlertSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001245")
# An alert setting is a setting that specifies conditions and situations that trigger alerts during the operation of a device. [Allotrope]
    
Function_math = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001257")
# A function is a process or a relation that associates each element x of a set X, the domain of the function, to a single element y of another set Y (possibly the same set), the codomain of the function. [Wikipedia]
    
ProductManufacturer = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001258")
# A product manufacturer is a symbol that denotes the organizational entity manufacturing some entity with a product role (economic). [Allotrope]
    
FirmwareVersion = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001259")
# A firmware version is a version number that identifies the firmware of a device. [Allotrope]
    
Firmware = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001260")
# In electronic systems and computing, firmware is &quot;the combination of a hardware device, e.g. an integrated circuit, and computer instructions and data that reside as read only software on that device&quot;. As a result, firmware usually cannot be modified during normal operation of the device. Typical examples of devices containing firmware are embedded systems (such as traffic lights, consumer appliances, and digital watches), computers, computer peripherals, mobile phones, and digital cameras. The firmware contained in these devices provides the control program for the device. [Wikipedia]
    
Queue = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001262")
# In computer science, a queue is a particular kind of abstract data type or collection in which the entities in the collection are kept in order and the principal (or only) operations on the collection are the addition of entities to the rear terminal position, known as enqueue, and removal of entities from the front terminal position, known as dequeue. [Wikipedia]
    
RequestQueue = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001263")
# A list used to sequence objects and to line up requests for a resource. [NCI]
    
PeakWidthAtBaseline = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001264")
# The peak width determined at the baseline level. The peak tangents are drawn from the turning points of the leading and trailing edges. Then the points of intersection with the baseline are calculated. The distance between the two points of intersection is the baseline level width. [Allotrope]
    
PeakWidthAtHalfHeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001266")
# The peak width calculated at half of the peak height. [Allotrope]
    
Standard = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001276")
# A standard is a norm or requirement that is established for technical systems. [Wikipedia]
    
ClassificationDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001277")
# A classification datum is a facet that classifies some entity. [Allotrope]
    
TypeSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001285")
# A type specification is a specification of a collection of things by the members of that collection being classified as instance of a class or concept, often with additional constraints. [Allotrope]
    
PropertySpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001286")
# A property specification is a specification about a feature, property, attribute or characteristic. The specification defines constraints on it, such as being an instance of a specific class. [Allotrope]
    
ScalarFloatDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001288")
# A scalar double datum is a scalar floating point number datum having a IEEE single precision datum (xsd:float). [Allotrope]
    
Decision = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001494")
# A decision is a proposition that is a choice made from a set of alternative propositions. [Allotrope]
    
VectorDecimalDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001495")
# A number vector datum is a vector datum that has only decimal scalar components. [Allotrope]
    
VectorFloatingPointNumberDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001496")
# A number vector datum is a vector datum that has only floating point scalar components. [Allotrope]
    
VectorFloatDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001497")
# A number vector datum is a vector datum that has only IEEE single precision floating point scalar components. [Allotrope]
    
VectorDoubleDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001498")
# A number vector datum is a vector datum that has only IEEE double precision floating point scalar components. [Allotrope]
    
PlanSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001501")
# A directive information entity with action specifications and objective specifications as parts that, when concretized, is realized in a process in which the bearer tries to achieve the objectives by taking the actions specified. [IAO]
    
StartCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001503")
# A start command is a process command that orders the procedural element to begin executing the normal RUNNING logic. This command is only valid when the procedural element is in the IDLE state. [Allotrope]
    
Setting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001505")
# A setting is a specification about a configuration of some controllable system or a situation occurring in a system that triggers a reaction. [Allotrope]
    
StatisticalMethod = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001508")
# A statistics method is a specification (method) for sampling a population, quantification of qualities of the samples and applying statistics on the quantified qualities to produce summary information on the population. [Allotrope]
    
ScalarBooleanDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001510")
# A scalar datum that has a boolean value. [Allotrope]
    
ScalarStringDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001511")
# A scalar datum that has a textual value. [Allotrope]
    
ScalarTimestampDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001512")
# A scalar datum that has a timestamp (xsd:dateTime) literal value. [Allotrope]
    
ScalarUriDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001513")
# A scalar datum that has a URI as value. [Allotrope]
    
VectorBooleanDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001514")
# A vector boolean datum is a vector datum that has only boolean scalar components. [Allotrope]
    
VectorStringDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001515")
# A vector boolean datum is a vector datum that has only string scalar components. [Allotrope]
    
VectorTimestampDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001516")
# A vector boolean datum is a vector datum that has only timestamp scalar components. [Allotrope]
    
VectorUriDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001517")
# A vector URI datum is a vector datum that has only URI scalar components. [Allotrope]
    
BaselinePoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001518")
# A baseline point is a data point that is member of a baseline. [Allotrope]
    
BaselineStartPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001519")
# The baseline start point is the data point of the baseline with the smallest abscissa value. [Allotrope]
    
BaselineEndPoint = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001520")
# The baseline end point is the data point of the baseline with the largest abscissa value. [Allotrope]
    
BaselineFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001521")
# A baseline facet is a facet that is part of a baseline. [Allotrope]
    
BaselineStart = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001522")
# A baseline facet that denotes the first value of the abscissa that belongs to the baseline. [Allotrope]
    
BaselineEnd = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001523")
# A baseline facet that denotes the last value of the abscissa that belongs to the baseline. [Allotrope]
    
BaselineValueAtStart = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001524")
# A baseline facet that denotes the first value of the ordinate that belongs to the baseline. [Allotrope]
    
BaselineValueAtEnd = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001525")
# A baseline facet that denotes the last value of the ordinate that belongs to the baseline. [Allotrope]
    
ValueSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001532")
# A value specification is a specification about constraints on the values of parameters or properties. [Allotrope]
    
StateSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001544")
# A state specification is a specification about a state that will be realized in some possible future occurrence. [Allotrope]
    
TimeTriggerSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001546")
# A trigger specification that specifies a trigger that triggers after a certain period of time. [Allotrope]
    
EventSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001547")
# An event specification is a specification about a point in time when a specific situation is realized or at process boundary. [Allotrope]
    
ClassCoordination = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001552")
# A class coordination is a facet of a definition of a class that expresses some differentia. [Allotrope]
    
EndEventSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001554")
# An end event specification is an event specification that is about the end of some process. [Allotrope]
    
StartEventSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001555")
# A start event specification is an event specification that is about the start of some process. [Allotrope]
    
ParallelProcedureSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001557")
# A parallel procedure specification is a procedure specification having a set of activity specifications, that are to be realized in parallel. [Allotrope]
    
FlowSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001558")
# A flow specification is a specification on how material or information is transferred or exchanged between subsequent activities. It links activity specifications using the direction contextual roles &apos;to role&apos; and &apos;from role&apos;. [Allotrope]
    
MaterialFlowSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001559")
# A material flow specification is a flow specification about material transfers between processes. [Allotrope]
    
DataFlowSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001560")
# A data flow specification is a flow specification about how information is exchanged between processes. [Allotrope]
    
Definition = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001561")
# A definition is a proposition that succinctly characterizes an entity. [Allotrope]
    
QualityQuantificationFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001583")
# A quality quantification facet is a quantification facet that is a data output of some measurement and quantifies some measured quality. [Allotrope]
    
Temperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001584")
# A temperature (datum) is a quantity facet that quantifies some temperature. [Allotrope]
    
Osmolality = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001586")
# A osmolality (datum) is a quantity facet that quantifies some osmolality. [Allotrope]
    
ElectricConductivity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001587")
# Electrical conductivity is a quality quantification facet that quantifies the reciprocal of resistivity in a conductor. [IUPAC]
    
RelativeIntensity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001588")
# Relative intensity (datum) is a quantity facet that quantifies the relative magnitude of a signal. [Allotrope]
    
Wavenumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001592")
# Wavenumber (datum) is a quantity facet that is the reciprocal of the wavelength or the number of waves per unit length along the direction of propagation. [Allotrope]
    
Interferogram = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001599")
# An interferogram is a data distribution function of interference between a reference wave and an experimental wave produced by an interferometer. [Allotrope]
    
RamanInterferogram = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001600")
# A Raman interferogram is an interferogram produced by FT Raman spectroscopy. [Allotrope]
    
AnalyteName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001604")
# The analyte name is a name of a material that has the role of an analyte in an analysis assay. [Allotrope]
    
MethodName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001606")
# A method name is a name that denotes a plan specification (method). [Allotrope]
    
Resolution = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001619")
# Resolution is a description of the smallest change in a quality being measured by a sensor (measurement instrument, detector) that causes a perceptible change in the corresponding indication. [Allotrope]
    
InclusiveGateway = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001622")
# An inclusive gateway is a transition specification that has multiple activity successors. The process forks into each succeeding activity of the inclusive gateway where the guard condition is true. [Allotrope]
    
ExclusiveGateway = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001623")
# An exclusive gateway is a transition specification that has multiple conditional activity successors and an optional default transition. The guard conditions on the successors are checked and at most one of them must be true at the runtime. If no guard condition is met then the optional default transition is done or the process terminates. [Allotrope]
    
Delay = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001625")
# A delay is a process property that describes a difference in time between a process boundary and some other point in time. [Allotrope]
    
StopCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001626")
# A stop command is a process command that orders the procedural element to execute the stopping logic. [Allotrope]
    
PauseCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001627")
# A pause command is a process command that orders the procedural element to pause at the next programmed pause transition within its sequencing logic and await a resume command before proceeding. [Allotrope]
    
RestartCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001628")
# A restart command is a process command that orders the procedural element to execute the restarting logic to safely return to the running state. [Allotrope]
    
AbortCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001629")
# An abort command is a process command that orders the procedural element to execute an aborting logic. [Allotrope]
    
HoldCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001630")
# A hold command is a process command that orders the procedural element to execute the holding logic. [Allotrope]
    
ResetCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001631")
# A reset command is a process command that causes a transition to the idle state. [Allotrope]
    
ResumeCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001632")
# A resume command is a process command that orders a procedural element that has paused at a programmed transition as the result of either a pause command or a single step mode to resume execution. [Allotrope]
    
ControlCommand = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001635")
# A control command is an action specification that specifies a setting to be set by a controlling process. [Allotrope]
    
PartSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001636")
# A part specification is a specification about parthood. Targets of this specifications are parts of some whole. [Allotrope]
    
IngredientSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001637")
# An ingredient specification is a part specification about ingredients in a portion of mixed materials. [Allotrope]
    
MemberSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001638")
# A member specification is a part specification about members of a collection or an object aggregate. [Allotrope]
    
ComponentSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001639")
# A component specification is a part specification about the components of a system. [Allotrope]
    
GrainSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001640")
# A grain specification is a part specification about the granular parts of a whole. [Allotrope]
    
FacetSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001641")
# A facet specification is a part specifications about some facet of an information content entity. [Allotrope]
    
ValueInRangeCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001643")
# A condition that is fulfilled if a given value falls into a given range of values. [Allotrope]
    
BooleanCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001644")
# A condition that is fulfilled if a given boolean value is equal to the specified boolean value. [Allotrope]
    
ToleranceRange = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001647")
# Range of values of allowed deviation for a given value. [Allotrope]
    
StateCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001657")
# A condition that is fulfilled if a specified situation occurs. [Allotrope]
    
MassConcentration = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001661")
# A mass concentration (datum) is a quantification facet that quantifies a concentration defined as the mass of a constituent divided by the volume of the mixture. [Allotrope]
    
Formula_math = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001663")
# A formula is a notation of a term, fact, rule or function expressed in terms of mathematical symbols. [Allotrope]
    
DiagnosticTrace = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001664")
# A diagnostic trace is a data distribution function that records the output of some diagnostic monitoring process over time. [Allotrope]
    
Polarity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001665")
# Polarity is a quality quantification facet that describes the positive or negative direction of an electrical, acoustical or magnetic force relative to a reference state. [Allotrope]
    
PolarityCode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001669")
# A polarity code is a code that indicates a polarity. [Allotrope]
    
BrandName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001680")
# A brand name is a marketed name given by a maker of a product to a product or class of products, especially a trademark. [Allotrope]
    
PartNumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001681")
# The part number is a model number of a class of device parts, specified by the device manufacturer. [Allotrope]
    
StepInterpolationAlgorithm = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001695")
# A step interpolation algorithm is an interpolation algorithm where two subsequent points are interpolated by a step function that switches from the first ordinate value to the second ordinate value at the center of the abscissa values. [Allotrope]
    
SoftwareVersion = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001700")
# A version number that identifies software. [Allotrope]
    
Frequency = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001732")
# A frequency is a rate that quantifies the number of occurrences of some discrete event in a given amount of time. [Allotrope]
    
ProcessQuantificationFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001816")
# A process quantification facet is a quantification facet that is the output of some measurement over a process or temporal region. [Allotrope]
    
Length = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001817")
# Length is a quality quantification facet that quantifies the distance between two points in space. [Allotrope]
    
CorrelationCoefficient = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001818")
# A correlation coefficient is a numerical measure of some type of correlation, meaning a statistical relationship between two variables. [Wikipedia]
    
Assessment = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001836")
# An assessment is a proposition about the judgment on a situation after considering the information known about it. [Allotrope]
    
Volume = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001843")
# A volume datum is a quality quantification facet that quantifies some amount of 3-dimensional space an entity occupies. [Allotrope]
    
Mass = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001844")
# A mass datum is a quality quantification facet that quantifies some amount of matter. [Allotrope]
    
StatisticalFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001852")
# A statistical facet is a mathematical facet that is part of some statistics. [Allotrope]
    
ElectricCurrent = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001856")
# Current is a quality quantification datum that quantifies the ability to conduct an electrical charge. [PATO]
    
Qualification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001871")
# A qualification is a proposition that an entity meets the requirements of a specific right or objective. [Allotrope]
    
Requirement = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001872")
# A requirement is a proposition that states a set of conditions that have to be fulfilled to achieve some specific objective. [Allotrope]
    
Energy_datum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001880")
# Energy amount is a quantification of the energy quality of a material or the amount of energy. [Allotrope]
    
FlowRate = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001881")
# Flow rate is a quality quantification facet that quantifies the motion of material through a surface per time. [Allotrope]
    
UniversalNamingConvention = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001907")
# The universal naming convention is a specification for the syntax of an identifier for a location of a network resource, such as a shared file, directory or printer in Microsoft Windows. [Allotrope]
    
Voltage = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001916")
# Voltage is a quality quantification facet which quantifies the difference in electric potential energy between two points per unit electric charge. [Wikipedia]
    
Power = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001917")
# Power is a quality quantification facet that quantifies the rate of doing work. [PATO]
    
Pressure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001918")
# Pressure is a quality quantification facet that quantifies the mount of force exerted per unit area. [PATO]
    
FileName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001926")
# A file name is a name that denotes a file in a file system. It is a local identifier in the scope of the folder the file is located. [Allotrope]
    
PosixStandard = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001929")
# POSIX is a family of standards specified by the IEEE Computer Society for maintaining compatibility between operating systems. [Wikipedia]
    
Signature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001963")
# A signature is facet that is a proof of identity and intent of a signer towards some information. [Allotrope]
    
DefaultCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001968")
# A default condition is a condition that is member of a set of conditions that is always true if all others conditions in the collections are false. [Allotrope]
    
ElectricConductance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001969")
# Electric conductance is the quality quantification facet that quantifies the reciprocal of a the resistance in a conductor. [IUPAC]
    
ElectricResistivity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001970")
# Electric resistivity is the is the quality quantification facet that quantifies the electric field strength divided by the current density when there is no electromotive force in a conductor. [IUPAC]
    
ElectricResistance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001971")
# Electric resistance is the quality quantification facet that quantifies the electric potential difference divided by the electric current when there is no electromotive force in a conductor. [IUPAC]
    
LocationSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001973")
# A location specification is a specification that specifies the location of something. [Allotrope]
    
WeightLoss = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001985")
# Weight loss is a mass facet that quantifies the difference in weight of a material before and after heating or drying. [Allotrope]
    
ConformanceAssessment = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001991")
# A conformance assessment is an assessment about whether two sources of data conform. [Allotrope]
    
MolarConcentration = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002006")
# A molar concentration (datum) is a quantification facet that quantifies a concentration defined as the amount of substance of a constituent divided by the volume of the mixture. [Allotrope]
    
Comment = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002017")
# A comment is a remark often related to an added piece of information, or an observation or statement. [SIO]
    
Enthalpy = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002021")
# Enthalpy (datum) is a quantification datum that quantifies the internal energy of a system plus the product of pressure and volume. Its change in a system is equal to the heat brought to the system at constant pressure. [IUPAC]
    
HeatCapacity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002022")
# Heat capacity is a quantification facet that quantifies the amount of heat to be supplied to a given mass of a material to produce a unit change in its temperature. [Wikipedia]
    
StateFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002023")
# A state facet is a facet that is about some state at a certain time. A state is a process during which some characteristic remains constant. [Allotrope]
    
ParticleSize = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002027")
# Particle size (datum) is a size datum that quantifies the dimensions of an individual particle. [Allotrope]
    
ContentSpecification = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002031")
# A content specification is a part specification that specifies a contained portion of material of a container. [Allotrope]
    
Concentration = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002036")
# A concentration (datum) is a quantification facet that quantifies a quality inhering in a substance by virtue of the amount of the bearer&apos;s there is mixed with another substance. [Allotrope]
    
ElapsedTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002050")
# Elapsed time is a duration measured from a specific reference time point or timebase. [Allotrope]
    
HeatTransferCoefficient = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002072")
# A heat transfer coefficient is a quality quantification facet that quantifies the proportionality constant between the heat flux and the thermodynamic driving force for the flow of heat. [Wikipedia]
    
AngularVelocity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002074")
# A angular velocity datum is quality quantification facet that quantifies how fast an object rotates or revolves relative to another point. [Wikipedia]
    
Area = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002076")
# An area (datum) is a quality quantification facet that quantifies the two-dimensional extend of an object. [Allotrope]
    
DataProcessingTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002095")
# Data processing time is the time when a data processing starts. [Allotrope]
    
MassFraction = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002099")
# The mass fraction (datum) is a quality quantification facet that quantifies the fraction pertaining the mass of a constituent divided by the total mass of all constituents in the mixture. [Allotrope]
    
InfraredInterferogram = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002103")
# An infrared interferogram is an interferogram produced by FT infrared spectroscopy. [Allotrope]
    
Diameter = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002107")
# Diameter is a length which is equal to the length of any straight line segment that passes through the center of a circle and whose endpoints are on the circular boundary. [PATO]
    
InnerDiameter = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002108")
# Inner diameter is the diameter quantified at the inside. [Allotrope]
    
Size_datum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002109")
# Size is a quality quantification facet that quantifies the spatial extend of an entity. [Allotrope]
    
VolumeConcentration = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002110")
# A volume concentration (datum) is a quantification facet that quantifies a concentration defined as the volume of a constituent divided by the volume of the mixture. [Allotrope]
    
ElectricCharge = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002111")
# Electric charge is the quality quantification facet that quantifies the integral of electric current over time. [Allotrope]
    
ReferenceMaterialWeight = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002115")
# A reference material weight is a quality quantification facet that quantifies the mass of a material with the role of reference material in the analysis. [Allotrope]
    
SaturationVaporPressure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002119")
# A saturation pressure (datum) is a quality quantification facet that quantifies the saturation vapor pressure of a substance. [Allotrope]
    
SpecificSurfaceArea = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002120")
# When the area of the interface between two phases is proportional to the mass of one of the phases (e.g. for a solid adsorbent, for an emulsion or for an aerosol), the specific surface area (a, s or preferably as) is defined as the surface area divided by the mass of the relevant phase. [IUPAC]
    
EquilibrationTime = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002128")
# An equilibration time is an elapsed time required to reach an equilibrium state after a perturbation. [Allotrope]
    
DilutionVolume = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002138")
# A dilution volume is a volume of diluent used in a dilution. [Allotrope]
    
SampleTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002149")
# A sample temperature result is a quality quantification facet that quantifies the temperature of the sample. [Allotrope]
    
MassChange = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002150")
# A mass change is a mass facet that quantifies the change in initial mass. [Allotrope]
    
MassChangeRate = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002151")
# A mass change rate is a rate that quantifies the change in initial mass per unit time. [Allotrope]
    
AmbientTemperature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002157")
# An ambient temperature is a quantity facet that quantifies the temperature of the surrounding atmosphere. [Allotrope]
    
EnthalpyOfFusion = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002163")
# The enthalpy of fusion datum is quantification of the amount of energy (enthalpy) that must be added to a solid substance, to transform a quantity of that substance into a liquid. [Wikipedia]
    
SpecificEnthalpyOfFusion = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002164")
# The specific enthalpy of fusion datum is the enthalpy of fusion referenced to a unit mass of substance. [Allotrope]
    
MolarEnthalpyOfFusion = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002165")
# The specific enthalpy of fusion datum is the enthalpy of fusion referenced to a unit amount of substance. [Allotrope]
    
EnthalpyOfVaporization = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002166")
# The enthalpy of vaporization datum is quantification of the amount of energy (enthalpy) that must be added to a liquid substance, to transform a quantity of that substance into a gas. [Wikipedia]
    
SpecificEnthalpyOfVaporization = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002167")
# The specific enthalpy of vaporization datum is the enthalpy of vaporization referenced to a unit mass of substance. [Allotrope]
    
MolarEnthalpyOfVaporization = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002168")
# The molar enthalpy of vaporization datum is the enthalpy of vaporization referenced to a unit amount of substance. [Allotrope]
    
EnthalpyOfSublimation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002169")
# The enthalpy of sublimation datum is quantification of the amount of energy (enthalpy) that must be added to a solid substance, to transform a quantity of that substance into a gas. [Wikipedia]
    
SpecificEnthalpyOfSublimation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002170")
# The specific enthalpy of sublimation datum is the enthalpy of sublimation referenced to a unit mass of substance. [Allotrope]
    
MolarEnthalpyOfSublimation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002171")
# The molar enthalpy of sublimation datum is the enthalpy of sublimation referenced to a unit amount of substance. [Allotrope]
    
HeatFlow = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002176")
# Heat flow is a quantification of the heat transferred per time. [Allotrope]
    
StandardNominalValue = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002178")
# A standard nominal value is a nominal value for a measurement assigned to a standard material. [Allotrope]
    
StandardMeasuredValue = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002179")
# A standard measured value is an assay result that is a measure of the standard material. [Allotrope]
    
StandardDeviation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002192")
# The standard deviation is a measure of the amount of variation or dispersion of a set of values. [Wikipedia]
    
CumulativeDistributionPercentage = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002194")
# A cumulative distribution percentage is a statistical facet that describes the percentage of population members meeting a given condition. [Allotrope]
    
BinUpperLimit = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002195")
# A bin upper limit is a statistical facet that quantifies the upper limit that population members meet within a distribution. [Allotrope]
    
DistributionModality = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002196")
# A distribution modality is a classification datum that indicates the number of peaks contained in the classified distribution. [Allotrope]
    
PartialPressure = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002198")
# A partial pressure (datum) is a quality quantification facet that quantifies the notional pressure of a gas in a mixture of gases, if it alone occupied the entire volume of the original mixture at the same temperature. [Allotrope]
    
StandardFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002203")
# A standard facet is a facet that part of some standard or is about some standard material. [Allotrope]
    
DistributionType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002205")
# A distribution type is a classification datum for distributions where the ordinate is expressed based on selected category. [Allotrope]
    
RefractiveIndex = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002207")
# Refraction index is a quality quantification facet, that quantifies how fast light travels through a material. It is defined as n = c/v, where c is the speed of light in vacuum and v is the phase velocity of light in the medium. [Wikipedia]
    
PlateWellCount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002231")
# A plate well count is a count that quantifies the number of plate well positions present on a well plate. [Allotrope]
    
WellVolume = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002232")
# A well volume is a volume (datum) that quantifies how much volume of material that can be put into each well in a well plate. [Allotrope]
    
Reflectance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002260")
# A reflectance is a quality quantification facet that quantifies the fraction of incident radiation reflected by a surface or discontinuity. [IUPAC]
    
Transmittance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002261")
# A transmittance is a quality quantification facet that quantifies the ratio of the transmitted radiant power (P_λ) to that incident on the sample (P0_λ): T = P_λ/ P0_λ. [IUPAC]
    
PositionCount = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002274")
# A position count is a spatial quantification facet that quantifies the number of distinct spatial locations. The spatial locations are defined by some pattern or morphology. [Allotrope]
    
AutomationSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002277")
# An automation flag is a flag that controls whether a process involves an automation system (true) participant alone or involves a human participant (false). [Allotrope]
    
EnabledSetting = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002280")
# An enabled flag setting is control setting that controls whether a process is running in a specific situation controlled by the setting. [Allotrope]
    
MolecularMass = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002294")
# A molecular mass is a quality quantification facet that quantifies the mass of a molecule. [Allotrope]
    
RelativePermittivity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002301")
# A relative permittivity result is a quality quantification facet that quantifies the the ability of a medium composed of molecules of a given type to transmit an electric field. [CHEMINF]
    
NearInfraredSpectrum = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002330")
# A plot of absorbance or transmittance versus wavelength obtained by measuring the amount of radiation absorbed by a sample as a function of the wavelength of incident radiation from the near infrared region (0.8-2 µm). [Allotrope]
    
Purity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002371")
# A purity (datum) is a quality quantification facet that quantifies the purity of a portion of material. [Allotrope]
    
AngleOfOpticalRotation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002394")
# An angle of optical rotation result is a quality quantification facet quantifying the angle through which plane polarized light is rotated clockwise, as seen when facing the light source, in passing through an optically active medium. [IUPAC]
    
SpecificRotation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002395")
# A specific rotation result is is a quality quantification facet quantifying the change in orientation of monochromatic plane-polarized light, per unit distance–concentration product, as the light passes through a sample of a compound in solution. [Wikipedia]
    
MolarMass = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002409")
# Molar mass is a mass that quantifies the mass of a homogeneous substance containing 6.02 x 10^23 atoms or molecules. [Allotrope]
    
Hardness = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002427")
# A hardness is a quality quantification facet that quantifies some hardness. [Allotrope]
    
Thickness = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002432")
# A thickness datum is a quality quantification facet that quantifies a 1-D extent quality which is equal to the dimension through an object as opposed to its length or width. [Allotrope]
    
MinimumValue = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002440")
# A minimum value is a descriptive statistic that denotes the smallest value present in some dataset. [Allotrope]
    
MaximumValue = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002441")
# A maximum value is a descriptive statistic that denotes the largest value present in some dataset. [Allotrope]
    
RelativeStandardDeviation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002443")
# The relative standard deviation is a ratio of the standard deviation to the arithmetic mean. [Allotrope]
    
DataValidity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002449")
# A data validity is a qualification about the suitability of some data for a specified purpose. [Allotrope]
    
Fluorescence = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002480")
# A fluorescence is a quality quantification facet that quantifies the luminescence which occurs essentially only during the irradiation of a substance by electromagnetic radiation. [IUPAC]
    
Luminescence = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002507")
# Luminescence is a quality quantification datum that quantifies the spontaneous emission of radiation from an electronically or vibrationally excited species not in thermal equilibrium with its environment. [IUPAC]
    
Prescription = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002519")
# A prescription is a proposition that is about some social rules that are imposed on the use of some entity, that a member of the social community has to follow. [Allotrope]
    
Intensity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002537")
# An intensity (datum) is an quality quantification facet that quantifies the magnitude of a signal. [Allotrope]
    
AbsoluteIntensity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002538")
# Absolute intensity (datum) is a quantity facet that quantifies the absolute magnitude of a signal. [Allotrope]
    
AmbientHumidity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002570")
# An ambient humidity is a quantity facet that quantifies the humidity of the surrounding atmosphere. [Allotrope]
    
Strain = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002591")
# A strain is a quality quantification facet that quantifies the magnitude of deformation representing the displacement between particles in the body relative to a reference length. [Allotrope]
    
Stress = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002592")
# A stress is a quality quantification facet that quantifies the internal forces that neighboring particles of a continuous material exert on each other. [Allotrope]
    
Humidity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002595")
# A humidity (datum) is a quantity facet that quantifies some humidity. [Allotrope]
    
Width = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002599")
# A width datum is a quality quantification facet that quantifies a 1-D extent quality which is equal to the distance from one side of an object to another side which is opposite. [Allotrope]
    
Force = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002600")
# A force datum is a quality quantification facet that quantifies the physical quality inhering in a bearer by virtue of the bearer&apos;s rate of change of momentum. [Allotrope]
    
Velocity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002632")
# A velocity is a quality quantification facet that quantifies some velocity. [Allotrope]
    
Viscosity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002641")
# A viscosity is a quality quantification facet that quantifies the viscosity of a fluid. [Allotrope]
    
Barcode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002690")
# A barcode is a method of representing data in a visual, machine-readable form. [Wikipedia]
    
LinearVelocity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002691")
# A linear velocity datum is a quality quantification facet that quantifies how fast an object is traveling in a straight line, meaning its direction is not changing. [Allotrope]
    
Height = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002692")
# Height is a quality quantification facet that quantifies the bearer&apos;s vertical dimension of extension. [Allotrope]
    
StatisticalFeature = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002699")
# A statistical feature is a statistical facet that defines the feature with the role of a description or classification of a property, characteristic or facet of the members of the aggregate that is common to each member and is used to make aggregated data about the aggregate. [Allotrope]
    
Angle = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002718")
# An angle is a quality quantification facet that quantifies some angle quality. [Allotrope]
    
IntegrationAlgorithm = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002762")
# An integration algorithm is an algorithm about integration that specifies the way an integration process is carried out. [Allotrope]
    
CorrectedPeakArea = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002774")
# A corrected peak area is a peak area corrected for some relative response factor. [Allotrope]
    
RelativeCorrectedPeakArea = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002775")
# A relative corrected peak area is a relative peak area that denotes the corrected area of the peak relative to some other peak or summation of peaks. . [Allotrope]
    
ErrorCode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002790")
# An error code is a code that indicates the error associated with the aborted state of a planned process. [Allotrope]
    
Error = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002804")
# An error is a description of a discrepancy between a computed, observed, or measured value or condition and the true, specified, or theoretically correct value or condition. [NCI]
    
AmountOfSubstance = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002815")
# An amount of substance (datum) is a quantity facet that quantifies some amount of substance. [Allotrope]
    
NoiseType = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002832")
# A noise type is a classification datum that classifies the type of noise being measured. [Allotrope]
    
MethodVersion = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002837")
# A method version is a version number that identifies a method. [Allotrope]
    
Torque = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002841")
# A torque is a quality quantification facet that quantifies some torque. [Allotrope]
    
RotationalSpeed = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002842")
# A rotational speed is a quality quantification facet that quantifies some rotational speed. [Allotrope]
    
AnalystRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000003")
# Analyst is the role of a person which is an agent in the process of examination. [Allotrope]
    
ConditionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000004")
# Condition role is a contextual role of an information object that specifies a prerequisite. [Allotrope]
    
ControllerRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000005")
# Controller role is a controlling role of some material entity that is controlling some other object or a process. [Allotrope]
    
Denominator = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000006")
# Denominator is the conceptual role of a scalar that indicates the number of equal parts into which the unit is divided. [Allotrope]
    
IdentifierRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000007")
# An identifier role is the contextual role of an information content entity that identifies another entity. [Allotrope]
    
InterpolationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000009")
# An interpolation is the contextual role of a quantity or number that has been the result of an interpolation. [Allotrope]
    
NameRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000012")
# Name role is a contextual role of an information content entity that refers to an entity by a non-identifying designation. [Allotrope]
    
NominalDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000013")
# A nominal value is a contextual role of an information content entity that states an asserted value, that is assumed to be true. [Allotrope]
    
Numerator = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000014")
# Numerator is the conceptual role of a scalar that indicates the number which is to be divided into equal parts. [Allotrope]
    
ObjectiveRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000015")
# Objective role is the contextual role of an information object that describes an intent or purpose which is a situation at the process end point. [Allotrope]
    
ParameterRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000019")
# Parameter role is a data input role that is about some useful or critical characteristic of a particular system, for the purpose of identification, controlling, or evaluating the performance, status or conditions in the process. [Allotrope]
    
MaterialCleanedRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000020")
# Material that is undergoing a cleaning process. [Allotrope]
    
ReferenceRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000022")
# A role inhered by a participant that is a reference for qualitative or quantitative comparison in relation to other entities. [Allotrope]
    
SelectedObjectRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000026")
# A selected object is the selection role of the object that is selected from the selection target. [Allotrope]
    
SettingDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000028")
# Setting datum is the contextual role of an information object that specifies some device or process setting. [Allotrope]
    
Snapshot = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000029")
# A snapshot is the contextual role of an information object that is about a point in time within the bounds of a process. [Allotrope]
    
SpecificationTargetRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000030")
# A specification target is the role of a material entity that participates in a specifying process and is what the resulting specification is about. [Allotrope]
    
TemporalMean = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000033")
# Temporal mean is the contextual role of a quantity (quantity value or count) that describes a arithmetic mean of a quantity over time. [Allotrope]
    
TimeSegment = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000034")
# Time segment is a contextual role of some information object that is about a temporal part in the context of representation of a process. [Allotrope]
    
SampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000035")
# A sample role is a type of role whose bearer is a material entity that is the output of a sampling. [Allotrope]
    
ProcessingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000039")
# A contextual role that describes the way information is participating in some process from a causal dependency perspective. [Allotrope]
    
BoundRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000040")
# The role of some datum forming the maximum or minimum value in a range or collection of values. [Allotrope]
    
LowerBound = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000041")
# The role of a datum that is smaller than all data in an ordered range or collection. [Allotrope]
    
UpperBound = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000042")
# The role of a datum that is greater than all data in an ordered range or collection. [Allotrope]
    
DataOutputRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000043")
# Data output role is a type of contextual role of an information artifact that is the output of a process. [Allotrope]
    
DataInputRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000044")
# Data input role is a type of contextual role of an information artifact that is the input of a process. [Allotrope]
    
AggregationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000047")
# An aggregation role is a contextual role of an information entity that is participant of an aggregation process. [Allotrope]
    
AggregateRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000048")
# Aggregate role is the contextual role of an information content entity that is a collection of others. [Allotrope]
    
MemberRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000049")
# Member role is the contextual role of an information object that is member of some collection. [Allotrope]
    
DescriptivePurpose = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000053")
# A role of an information content entity that is meant to describe an object. [Allotrope]
    
CausalRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000054")
# A description of the cause-consequence relation of processes. [Allotrope]
    
Cause = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000055")
# Cause is the causal role of an information content entity that is about something causally dependent for another thing. [Allotrope]
    
Consequence = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000056")
# Consequence is the causal role of an information content entity that is about something causally resultant from another thing. [Allotrope]
    
Invariant = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000057")
# An invariant is the contextual role of an information object that is about a situation that does not change during the whole process. [Allotrope]
    
PostCondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000058")
# A post condition is the temporal contextual role of an information content entity that is about the situation, that is a condition so that a process can end or achieve its goal. [Allotrope]
    
Precondition = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000059")
# A precondition is the temporal contextual role of an information content entity that is about the situation, that is a condition so that a process can start. [Allotrope]
    
DesignativePurpose = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000060")
# A designative purpose is a type of contextual role of information artifacts that denote an entity in order to describe its characteristics. [Allotrope]
    
IndexRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000062")
# An index role is a contextual role of an information object that denotes to another object that is part of an aggregation and it is the data output of some indexing process. [Allotrope]
    
DirectivePurpose = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000064")
# A directive purpose or specification role is a type of contextual role of information content entities that are about an entity with a purpose to give directions. [Allotrope]
    
PrescriptivePurpose = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000072")
# A contextual role of information that describes some social rules that are imposed on the use of some entity, that a member of the social community has to follow. [Allotrope]
    
TemporalRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000073")
# A contextual role of information that is dependent on some temporal region or process boundary. [Allotrope]
    
ExceptionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000074")
# A contextual role of information the describes an unexpected, unusual or unintended situation. [Allotrope]
    
Variable = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000075")
# A variable is the contextual role of some data that is part of some other data that is varied in a  mathematical function or during data processing. [Allotrope]
    
DependentVariable = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000077")
# A dependent variable is a contextual role of an information artifact that represents the outputs or outcomes whose variation is being studied. [Wikipedia]
    
IndependentVariable = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000078")
# An independent variable is a contextual role of an information artifact that represents inputs or causes for variation of a dependent variable. In the experimental setting, the independent variable is controlled by the experimenter. Models and experiments test or determine the effects that the independent variables have on the dependent variables. [Wikipedia]
    
ActualDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000080")
# A actual value is the contextual role of an information content entity that is the direct or indirect output of some observation and describes some quality. [Allotrope]
    
SenderRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000087")
# The role inhered in a material entity that sends the transferred object in a transfer process. [Allotrope]
    
ReceiverRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000088")
# The role inhered in a material entity that receives the transferred object in a transfer process. [Allotrope]
    
TransferMediumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000090")
# A transfer medium is the role of a material that carries the transferred flow. [Allotrope]
    
AtEnd = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000092")
# At end is the contextual role of an information content entity that is about the end of a process. [Allotrope]
    
AtStart = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000093")
# At start is the contextual role of an information content entity that is about the start of a process. [Allotrope]
    
During = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000094")
# During is the contextual role of an information object that is about something within a temporal range of a process. [Allotrope]
    
DetectionStimulantRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000097")
# A role inhered when the presence of the bearer indicates the presence of the detection target in a detection process. [Allotrope]
    
TransferringRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000119")
# A transferring role is a localization role that is realized in some transferring process. [Allotrope]
    
StorageMediumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000120")
# Storage medium is the role of a material or site where something is stored. [Allotrope]
    
StorageRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000121")
# A role that is realized in some storing process. [Allotrope]
    
SelectionTargetRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000124")
# The selection target is the role of a participant in a selection process from which partitions are selected. [Allotrope]
    
AnalyteRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000127")
# The component of a system to be analyzed. [CHMO]
    
LinkingMediumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000149")
# The role of a material that is the  flow by which means a linking process is established. [Allotrope]
    
CalculatedDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000154")
# A datum that is the result of some calculation. [Allotrope]
    
DerivedMeasure = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000155")
# A derived measure is a measure that is the outcome of some indirect measurement. The derived value is derived from base measures by calculations following a formula or algorithm. [Allotrope]
    
BaseMeasure = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000156")
# A base measure is a measure that is the direct output of some measurement process. [Allotrope]
    
Measure = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000157")
# A measure is an actual value that is the direct or indirect outcome of some measurement and refers to some metric. [Allotrope]
    
ContextualRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000166")
# A contextual role is a representation of a specific interpretation of the information content object or of the circumstances that the information content object is referencing to. [Allotrope]
    
IndexedMember = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000169")
# Indexed member is the member role that has an index facet. [Allotrope]
    
OrderedMember = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000170")
# Ordered member is a member role that has an ordering within the collection. [Allotrope]
    
ExperimentSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000171")
# An experiment sample is a role that is played by a material object of interest in an assay used to obtain generalizable information about the sample source. [Allotrope]
    
CoatedMaterialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000211")
# A coated material is a coating role of a material whose surface is being coated by another material which it covers. [Allotrope]
    
CoatingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000212")
# A coating role is the role of a material that coats another material (the substrate). [Allotrope]
    
MeasurandRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000213")
# A measurand role is a measurement role of a material entity that is being measured. [Allotrope]
    
AdditiveRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000216")
# Additive is a role of material that is added to a mixture in order to achieve a supportive purpose. [Allotrope]
    
CatalystRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000217")
# A catalyst role is a reagent role of a substance that increases the rate of a reaction without modifying the overall standard Gibbs energy change in the reaction; the process is called catalysis. The catalyst is both a reactant and product of the reaction. [IUPAC]
    
DebrisRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000221")
# Debris is a role of material to be waste. [Allotrope]
    
DetergentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000223")
# A detergent role is a cleaning role of a surface active agent (or a mixture containing one of more surface active agents) having cleaning properties in dilute solution. [IUPAC]
    
DiluentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000224")
# Diluent is a role of material used to lessen the strength or flavor of a solution or mixture of another ingredient. [NCI]
    
DispersantRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000225")
# A dispersant is either a non-surface active polymer or a surface-active substance added to a suspension, usually a colloid, to improve the separation of particles and to prevent settling or clumping. [Wikipedia]
    
ExcipientRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000226")
# Excipient is a role of a generally pharmacologically inactive substance that is formulated with the active ingredient of a medication. [ChEBI]
    
FiltrateRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000228")
# Filtrate is a role of liquid outcome of a filtration process that is commonly the mechanical or physical operation which is used for the separation of solids from fluids (liquids or gases) by interposing a medium through which only the fluid can pass. [Wikipedia]
    
ReactionIntermediateRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000229")
# Intermediate role is a role of material that is formed from reactants (or preceding intermediates) and reacts further to give the directly observed products of a chemical reaction. [Wikipedia]
    
MarkerRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000230")
# A marker is a role of material to allow for identification of an object of interest. [Allotrope]
    
ReactantRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000231")
# Reactant role is a role of a chemical entity that is present at the start of a reaction. [Allotrope]
    
RetentateRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000232")
# The retentate role is the role of the material that is retained by a filtration process. [Allotrope]
    
StandardMaterialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000233")
# Standard material role is a role of material that is set up and established by authority as a reference material for the measure of quantity, weight, extent, value, or quality. [Allotrope]
    
TitrantRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000234")
# Titrant is a role of a solution containing the active agent with which a titration is made. [IUPAC]
    
CleaningAgentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000244")
# Cleaning agent role is a role of material used for cleaning something. [Allotrope]
    
OriginDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000247")
# Origin is the contextual role of an information object that is about the spatio-temporal location at the beginning of a process that changes it. [Allotrope]
    
RelativeDatumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000248")
# A relative datum role is the contextual role of a datum that is about a quantity or number that is the result of a ratio or difference calculation or an assertion of magnitude relative to a reference entity. [Allotrope]
    
IngredientRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000249")
# Ingredient is a role of material that is used in a material combining process to produce a new material. [Allotrope]
    
Sum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000250")
# The sum is the contextual role of numerical data that results from the addition of two or more numbers, amounts, or items. [Allotrope]
    
VersionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000251")
# A version role is the contextual role of an information content entity that denotes a specific variant in the history. [Allotrope]
    
ValidationSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000252")
# An validation sample role is a sample role of a material sample that is used for validation purposes. [Allotrope]
    
ControlSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000253")
# An control sample role is a sample role of a material that does contain a known amount of analyte for control purposes. [Allotrope]
    
CalibrationSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000254")
# An calibration sample role is a sample role of a material that does contain a known amount of substance for calibration purposes. [Allotrope]
    
StandardSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000255")
# An standard sample role is a sample role of a material sample that does contain a known amount of standard material. [Allotrope]
    
UnknownSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000256")
# An unknown sample role is a sample role of a material of an unknown substance, or that does contain an unknown amount of analyte. [Allotrope]
    
QualityControlSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000257")
# An quality control sample role is a control sample role of a material that is used for purposes of quality control. [Allotrope]
    
ReferenceSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000258")
# An reference sample role is a sample role of a material that does contain a known amount of analyte. [Allotrope]
    
BlankRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000259")
# An blank role is a sample role of a material that does not contain any analyte. [Allotrope]
    
SpikedSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000260")
# A spiked sample role is a sample role of a material that does contain a spike substance. [Allotrope]
    
UnspikedSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000261")
# An unspiked sample role is a sample role of a material sample that does not contain a spike substance. [Allotrope]
    
DestinationDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000263")
# Destination is the contextual role of an information object that is about the spatio-temporal location at the end of a process that changes it. [Allotrope]
    
TermMathematicalRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000264")
# A role of a mathematical information object as component of a mathematical formula. [Allotrope]
    
SolventRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000269")
# Solvent is the role of a potion of liquid material when it dissolves a solute in order to produce a solution. [Allotrope]
    
SoluteRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000270")
# Solute is the role a portion of material when it is dissolved within a solution. [Allotrope]
    
DispersedPhaseRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000271")
# The dispersed phase role is the dispersion role of a portion of material in a dispersion, that is distributed in the form of discrete disco
    
ContinuousPhaseRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000272")
# The continuous phase role is the dispersion role of a portion of material constituting the medium, a phase that exhibits continuity thro
    
DispersionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000273")
# The role of a portion of material that participates in a dispersion process to form a colloid. [Allotrope]
    
DissolutionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000274")
# The role of a portion of material that participates in a dissolution process to form a solution. [Allotrope]
    
MathematicalRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000277")
# A contextual role that describes an interpretation in a mathematical model. [Allotrope]
    
CoordinateRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000280")
# A coordinate role is a contextual role of a scalar as component of a vector or tuple in a coordinate system specifying a point in space. [Allotrope]
    
CartesianCoordinateRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000281")
# A Cartesian coordinate role is a coordinate role of a scalar in a Cartesian coordinate system, that specifies each point uniquely in an n-dimensional Euclidean space . These coordinates are equal, up to sign, to distances from the point to n mutually perpendicular hyperplanes. [Allotrope, Wikipedia]
    
ReferenceDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000285")
# A reference datum is the contextual role of some information content entity that is referenced in the context of another information content entity for the purpose of comparison. It describes or denotes an object that has the role of a reference role. [Allotrope]
    
TemporalReferenceRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000286")
# The role of some data piece of information that acts as reference for stating relative time. [Allotrope]
    
OperatorRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000287")
# Operator is the role of a person which controls or uses a device in an agent role. [Allotrope]
    
SelectionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000288")
# A role which is played by a participant in a selection process. [Allotrope]
    
CleaningRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000289")
# The role of a participant of a cleaning process. [Allotrope]
    
SubjectRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000290")
# A role of an entity in some information producing process that produces information about this entity. [Allotrope]
    
DetectionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000291")
# The role of a participant in a detecting process. [Allotrope]
    
DetectionTargetRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000292")
# The role inhered by being the objective of a detecting activity. [Allotrope]
    
AnalysisRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000293")
# A role of a participant in an analysis assay. [Allotrope]
    
MeasurementRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000294")
# A role of a participant in a measurement. [Allotrope]
    
LinkingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000295")
# A role of a participant in a linking process. [Allotrope]
    
ControllingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000296")
# A role of a participant in a controlling process. [Allotrope]
    
ControlledObjectRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000297")
# Controlled object is the role of a material entity that is being controlled by a controller in a controlling process. [Allotrope]
    
DilutionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000298")
# The role of a portion of material that participates in a dilution process. [Allotrope]
    
ResultRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000299")
# Result role is a data output role that applies to new information produced by a process. [Allotrope]
    
RatioDatumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000312")
# A ratio datum role is a relative datum role that expresses the relative magnitude as a ratio of the magnitude of the subject to that of the reference entity. [Allotrope]
    
DifferenceDatumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000313")
# A difference datum role is a relative datum role that expresses the relative magnitude as a difference or interval of the magnitude of the subject to that of the reference entity. [Allotrope]
    
RelationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000314")
# A relation role is a contextual role of an information content entity that is about a relation of the subject of the information content entity to another entity. [Allotrope]
    
FirstMember = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000316")
# A first member is an ordered member that has no predecessor in the aggregate. [Allotrope]
    
LastMember = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000317")
# A last member is an ordered member that has no successor in the aggregate. [Allotrope]
    
StatisticalRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000319")
# A statistical role is a contextual role of data in statistics. [Allotrope]
    
ArithmeticMeanRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000320")
# The arithmetic mean is a statistical datum role of a datum that is the sum of a collection of numbers divided by the number of numbers in the collection. [Wikipedia]
    
MedianRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000321")
# The median role is a statistical datum role that denotes the value separating the higher half of a data sample, a population, or a probability distribution, from the lower half. [Wikipedia]
    
SkewnessRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000322")
# Skewness role is a statistical datum role of a datum that is a measure of the asymmetry of the probability distribution of a real-valued random variable about its mean. The skewness value can be positive or negative, or undefined. [Wikipedia]
    
VarianceRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000323")
# The variance role is a statistical datum role of a datum that denotes the expectation of the squared deviation of a random variable from its mean. [Wikipedia]
    
StatisticalSampleRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000324")
# A statistical sample role is the contextual role of a subset of a statistical population that is chosen to represent the population in a statistical analysis. [Wikipedia]
    
StatisticalPopulationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000325")
# A statistical population role is the statistical role of a set of similar items or events which is of interest for some question or experiment (the statistical population). A statistical population can be a group of existing entities or a hypothetical and potentially infinite group of entities conceived as a generalization from experience. [Wikipedia]
    
RandomVariable = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000326")
# In probability and statistics, a random variable, random quantity, aleatory variable, or stochastic variable is a variable whose possible values are outcomes of a random phenomenon. [Wikipedia]
    
StatisticDatumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000328")
# A statistic datum is the summary output of descriptive statistics on a statistical population. [Allotrope]
    
TriggerDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000330")
# An trigger datum is the role of a  datum that specifies some situation about a system or environment participating in a process that should trigger the start of another process. [Allotrope]
    
SurvivalRange = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000332")
# An survival range is the contextual role of an description or specification of about an environment in which the operation of a system can or should operate without damaging the system. [Allotrope]
    
AlertDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000333")
# An alert datum is a trigger datum that specifies a trigger that initiates a notification process that warns about an unintended situation. [Allotrope]
    
Domain_math = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000336")
# A domain is the mathematical role of the set a function is applied on. [Allotrope]
    
Codomain_math = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000337")
# A codomain is the mathematical role of the set a function maps to. [Allotrope]
    
DetectorRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000340")
# The detector role is a detection role of a material entity that is detecting some other entity. [Allotrope]
    
SynthesisRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000344")
# A synthesis role is a role of a material that is participating in a synthesis (material conversion) process. [Allotrope]
    
FormulationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000345")
# A formulation role is a role of a material that is participating in a formulation process. [Allotrope]
    
ParticulatePhase = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000347")
# Particulate phase role is the role of the particles dispersed in a gel, sol or aerosol. [NIST, Allotrope]
    
ActivePharmaceuticalIngredientRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000351")
# The role of a material in a drug product that is biologically active when interacting with other components of the drug product, other potential drug products, or the chemistry of the body into which the drug will be applied. [Allotrope]
    
SpecimenRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000352")
# Specimen role is the sample role of a prepared fraction of a portion of material that is analyzed in a particular experiment. [Allotrope]
    
ProductRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000360")
# A role of a material that is intended and desired to be  produced in a synthesis. [Allotrope]
    
BatchRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000361")
# Batch role is a product role of a portion of material that is intended to have uniform character and quality, within specified limits, and is produced according to a single manufacturing order during the same cycle of manufacture. [Allotrope, CFR21]
    
FiltrationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000362")
# A filtration role is a role of a material in a filtration process. [Allotrope]
    
RinseSolutionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000363")
# The rinse solution role is a cleaning agent role of a fluid used to flush something in order to remove contaminants. [Allotrope]
    
ImpurityRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000364")
# A material role for any component of material that is not part of the defined product at the particular stage of manufacture or storage. [Allotrope]
    
DegradationProductRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000365")
# A degradation product is an impurity resulting from a chemical change in the drug substance brought about during manufacture and/or storage of the new drug product by the effect of, for example, light, temperature, pH, water, or by reaction with an excipient and/or the immediate container closure system. [ICH-Q3B]
    
UnidentifiedDegradationProductRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000366")
# A degradation product role for which a structural characterization has not been achieved and that is defined solely by qualitative analytical properties (e.g., chromatographic retention time). [ICH-Q3A]
    
UnspecifiedDegradationProductRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000367")
# A degradation product role that is limited by a general acceptance criterion, but not individually listed with its own specific acceptance criterion, in the new drug product specification. [ICH-Q3A]
    
ClassificationPurpose = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000368")
# A contextual role of information that classifies some of some entity into a category, class or schema. [Allotrope]
    
SamplingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000369")
# A sampling role is a role of an object aggregate or a member of that aggregate that participates in a sampling process on the aggregate. [Allotrope]
    
PopulationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000370")
# The population role is the sampling role of the object aggregate that is object of the sampling. [Allotrope]
    
SampleSetRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000371")
# The sample set role is the role of the partition of the population object aggregate that was selected in the sampling process. [Allotrope]
    
SpatialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000373")
# A spatial role is the contextual role of some information context object that is about spatial location, orientation, or relative positioning. [Allotrope]
    
Approver = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000404")
# An approver is the role of an organizational entity that approves something. [Allotrope]
    
Researcher = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000405")
# A researcher is the role of an organizational entity that researches something. [Allotrope]
    
Investigator = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000406")
# An investigator is a researcher that is doing an investigation. [Allotrope]
    
Reviewer = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000407")
# A reviewer is the role of an agent that reviews some information. [Allotrope]
    
Signer = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000409")
# A signer is the role of the agent in a signing process. [Allotrope]
    
CalibrationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000410")
# A calibration role is role of a material entity that participates in a calibration process. [Allotrope]
    
ReferenceMaterialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000411")
# A reference material role is the role of a material used in a calibration whose qualities are sufficiently homogenous and well established to be used as reference. [Allotrope]
    
StartingMaterialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000420")
# A role for a material used in the synthesis of a new drug substance that is incorporated as an element into the structure of an intermediate and/or of the new drug substance. [ICH-Q3A]
    
LimitingReagentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000421")
# A reagent role of the material with the least mole quantity in a chemical process and as such limits the amount of product that can be formed. [Allotrope]
    
EnantiomericImpurityRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000422")
# An enantiomeric impurity is the impurity role of a compound with the same molecular formula as the drug substance that differs in the spatial arrangement of atoms within the molecule and is a non-superimposable mirror image. [ICH-Q3A]
    
ExtraneousContaminantRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000423")
# An extraneous contaminant role is an impurity role arising from any source extraneous to the manufacturing process. [ICH-Q3A]
    
IdentifiedImpurityRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000424")
# An impurity for which a structural characterization has been achieved. [ICH-Q3A]
    
PotentialImpurityRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000425")
# An impurity role for a material that theoretically can arise during manufacture or storage. It may or may not actually appear in the new drug substance. [ICH-Q3A]
    
SpecifiedImpurityRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000426")
# An impurity that is individually listed and limited with aspecific acceptance criterion in the new drug substance specification. A specified impurity can be either identified or unidentified. [ICH-Q3A]
    
UnidentifiedImpurityRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000427")
# An impurity for which a structural characterization has not been achieved and that is defined solely by qualitative analytical properties (e.g., chromatographic retention time). [ICH-Q3A]
    
UnspecifiedImpurityRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000428")
# An impurity role that is limited by a general acceptance criterion, but not individually listed with its own specific acceptance criterion, in the new drug substance specification. [ICH-Q3A]
    
IdentifiedDegradationProductRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000429")
# A degradation product role for which a structural characterization has been achieved. [ICH-Q3A]
    
SpecifiedDegradationProductRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000430")
# A degradation product role that is individually listed and limited with a specific acceptance criterion in the new drug product specification. A specified degradation product can be either identified or unidentified. [ICH-Q3A]
    
InternalStandardRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000432")
# Internal standard role is the analysis role of a chemical substance that is added in a constant amount to samples, the blank and calibration standards in a chemical analysis. [Wikipedia]
    
ApprovingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000434")
# An approving role is a role that is realized in some approving process. [Allotrope]
    
SigningRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000435")
# A signing role is a role that is realized in some signing activity. [Allotrope]
    
SignedObject = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000436")
# The signed object is the bearer of the information content entity that is signed. [Allotrope]
    
SigningContextualRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000437")
# A signing contextual role is a contextual role of information content entities that are participants in a signing process. [Allotrope]
    
SignatureRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000438")
# A signature role is the role of an information object that is associated with some information and provides a proof of identity and intent of the signer. [Allotrope]
    
SignedContentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000439")
# Signed content role is the signing contextual role of the information content entity that is being signed. [Allotrope]
    
SubmitterRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000441")
# A submitter role is the role of a material entity that plays the sender of the submitted entity in a submitting process. [Allotrope]
    
AggregatedDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000442")
# An aggregated datum is the role of an information object that is about aggregated or summary information on the aggregate, such as statistics, count or sums of member data. [Allotrope]
    
Product_math = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000443")
# The product is the contextual role of numerical data that results from the multiplication of two or more numbers, amounts, or items. [Allotrope]
    
AggregatedFeature = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000444")
# The aggregated feature is the role of a description or classification of a property, characteristic or facet of the members of the aggregate that is common to each member and is used to make aggregated data about the aggregate. [Allotrope]
    
SoftwareAgentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000446")
# A software agent is the contextual role of software in the context of a process where a system executes that software and causally is an agent in the process. [Allotrope]
    
SubmissionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000449")
# A submission role is a role that is realized in a submitting process. [Allotrope]
    
MetadataRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000450")
# A metadata role is a contextual role of an information content entity that is not a parameter or result of a process but describes the context of the process. [Allotrope]
    
DestinationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000451")
# Destination role is the localization role of a site where the localized object is at the end of the localization process. [Allotrope]
    
OriginRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000452")
# Origin role is the localization role of a site where the localized object is at the start of the localization process. [Allotrope]
    
TransferredMaterial = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000453")
# A transferred material is the role of the material that is being transferred from the origin site to the destination site. [Allotrope]
    
ReceivedObjectRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000454")
# Sent object is the role of a transferred object at the start of the transferring process. [Allotrope]
    
SentObjectRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000455")
# Sent object is the role of a transferred object at the start of the transferring process. [Allotrope]
    
PredecessorRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000457")
# A predecessor role is an ordering role that applies if the information object or the entity it is about is before another one in a sequence. [Allotrope]
    
SuccessorRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000458")
# A successor role is an ordering role that applies if the information object or the entity it is about is after another one in a sequence. [Allotrope]
    
TriggeringEvent = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000461")
# A triggered event is a contextual role of an event specification that when realized is the cause of a trigger. [Allotrope]
    
TriggeredEvent = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000462")
# A triggered event is a contextual role of an event specification that when realized is the consequence of a trigger. [Allotrope]
    
DirectionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000463")
# A direction role is a contextual role of some information content entity indicating a direction in a relation. [Allotrope]
    
ToRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000464")
# A to role is a direction role indicating that something is going into an target direction. [Allotrope]
    
FromRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000465")
# A from role is a direction role indicating that something is coming from a source. [Allotrope]
    
DefiningPurpose = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000466")
# Defining purpose is the contextual role of some information that has the purpose to define an entity. [Allotrope]
    
OrderingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000471")
# An ordering role is a contextual role of an information content entity in the scope of some sequence. [Allotrope]
    
WorkflowRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000472")
# A workflow role is a contextual role of a part of a procedure specification. [Allotrope]
    
DefaultTransition = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000473")
# An default transition is a successor role in the scope of an exclusive gateway that specifies the succeeding activity if no guard conditions on the gateway are met. [Allotrope]
    
ExpectedDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000474")
# An expected datum is a descriptive datum that describes a information that was predicted or assumed to be the outcome of some process . [Allotrope]
    
Sequential = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000475")
# A workflow role of a single step in a sequentially executed procedure. [Allotrope]
    
Repeatable = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000476")
# A single step that can be repeated multiple times during a procedure. [Allotrope]
    
CalibratedDatum = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000477")
# A calibrated datum is the contextual role of a datum that is the output of some process that applies a calibration function to a measured datum. [Allotrope]
    
Parameter_math = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000478")
# A parameter is the contextual role of a datum that is not explicitly varied in a mathematical function or during data processing. [Allotrope]
    
OxidantRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000479")
# An oxidant role is a chemical reactant role whereby the substance removes electrons from another reactant in a redox reaction. [Allotrope]
    
FuelRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000480")
# A fuel role is a chemical reactant role whereby an energy-rich substance is transformed with release of usable energy. [Allotrope]
    
CoatingProcessRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000484")
# A coating process role is a role of a material that participates in a coating activity or the state of being coated. [Allotrope]
    
StoredObjectRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000487")
# A stored object is the storage role of an material entity that is being stored in a storage medium. [Allotrope]
    
CalibratedInstrumentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000488")
# A calibrated instrument role is the role of a measurement device that is the target of a calibration. [Allotrope]
    
DilutedMaterialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000489")
# Diluted material is the dilution role of a material that is being diluted in the dilution process. [Allotrope]
    
CoolingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000505")
# A changing role is a role realized in some cooling process. [Allotrope]
    
CoolantRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000506")
# A role of a material that acts as a heat sink as it undergoes a phase change. [Allotrope]
    
NebulizerSupportRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000509")
# Nebulizer support role is a support role in converting liquid into aerosol mist. [Allotrope]
    
DryingAdditiveRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000510")
# A drying additive role is the role of a material in a drying process that supports the drying process. [Allotrope]
    
DryingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000511")
# A drying role role is a role realized in some drying process. [Allotrope]
    
DryingMediumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000512")
# A drying medium role is a drying role of a material that takes or transports the solvent from the material being dried. [Allotrope]
    
MaterialDriedRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000513")
# Material dried role is the drying role of the material being dried. [Allotrope]
    
DefaultConditionRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000519")
# A default condition role is the condition role of an item in a collection of information content entities that applies (is true) if no other items apply (are false). [Allotrope]
    
DefaultRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000520")
# A default role is a directive purpose that assigns a specification to be applied to a context if no other specification is asserted in that context. [Allotrope]
    
StandardDeviationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000527")
# Standard deviation role is a statistical datum role of a datum that is  a measure of the amount of variation or dispersion of a set of values. [Wikipedia]
    
RelativeStandardDeviationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000539")
# Relative standard deviation role is a statistical datum role of a datum that is a standardized measure of dispersion of a probability distribution or frequency distribution. [Wikipedia]
    
InformationProductRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000544")
# An information product role is a contextual role of some information content entity that is produced for the purpose of sale. [Allotrope]
    
MatrixRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000547")
# The matrix are the components of a sample other than the analyte. [IUPAC]
    
LoadingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000550")
# A loading role is a role that is realized in some loading process. [Allotrope]
    
LoadingMediumRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000551")
# A loading medium role is the role of the material that carries the loaded material. in a loading process. [Allotrope]
    
LocalizationRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000552")
# A localization role is a role that is realized in some localization process. [Allotrope]
    
MaximumValueRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000565")
# The maximum value is a statistical datum role of a datum that is the largest value of a collection of numbers. [Wikipedia]
    
MinimumValueRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000566")
# The minimum value is a statistical datum role of a datum that is the smallest value of a collection of numbers. [Wikipedia]
    
DispensingRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000567")
# A role played by a participant in a dispensing process. [Allotrope]
    
DispensedMaterialRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000568")
# Dispensed material is the role of material given out in a dispensing process. [Allotrope]
    
Bench_site = onto.search_one(iri="http://purl.allotrope.org/ontologies/spatial#AFSP_0000002")
# A bench (site) is site in a workspace or laboratory where work is being done. [Allotrope]
    
Building_site = onto.search_one(iri="http://purl.allotrope.org/ontologies/spatial#AFSP_0000003")
# A building (site) is a site located in a structure with a roof and walls. [Allotrope]
    
Room = onto.search_one(iri="http://purl.allotrope.org/ontologies/spatial#AFSP_0000004")
# A room is a site that is a part or division of a building enclosed by walls, floor, and ceiling. [Allotrope]
    
Campus = onto.search_one(iri="http://purl.allotrope.org/ontologies/spatial#AFSP_0000006")
# A campus is a site that is the grounds of a school, hospital, or other institution. [Allotrope]
    
MaterialAnatomicalEntity = onto.search_one(iri="http://purl.obolibrary.org/obo/CARO_0000006")
# A part of a multicellular organism that is a material with granularity above the level of a protein complex. Or, a substance produced by a multicellular organism with granularity above the level of a protein complex. [Allotrope, CARO]
    
Air = onto.search_one(iri="http://purl.obolibrary.org/obo/ENVO_00002005")
# The mixture of gases (roughly (by molar content/volume: 78% nitrogen, 20.95% oxygen, 0.93% argon, 0.038% carbon dioxide, trace amounts of other gases, and a variable amount (average around 1%) of water vapor) that surrounds the planet Earth. [ENVO]
    
ObjectiveSpecification = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000005")
# A directive information entity that describes an intended process endpoint. When part of a plan specification the concretization is realized in a planned process in which the bearer tries to effect the world so that the process endpoint is achieved. [IAO]
    
DatumLabel = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000009")
# A label is a symbol that is part of some other datum and is used to either partially define  the denotation of that datum or to provide a means for identifying the datum as a member of the set of data with the same label [IAO]
    
Software = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000010")
# Software is a plan specification composed of a series of instructions that can be interpreted by or directly executed by a processing unit. [IAO]
    
ModelNumber = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000017")
# A model number is an information content entity specifically borne by catalogs, design specifications, advertising materials, inventory systems and similar that is about manufactured objects of the same class. The model number is an alternative term for the class. [IAO]
    
Symbol = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000028")
# An information content entity that is a mark(s) or character(s) used as a conventional representation of another entity. [IAO]
    
InformationContentEntity = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000030")
# A generically dependent continuant that is about some thing. [IAO]
    
DotPlot = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000037")
# A dot plot is a report graph which is a graphical representation of data where each data point is represented by a single dot placed on coordinates corresponding to data point values in particular dimensions. [IAO]
    
Graph = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000038")
# A diagram that presents one or more tuples of information by mapping those tuples in to a two dimensional space in a non arbitrary way. [IAO]
    
Algorithm = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000064")
# A plan specification which describes the inputs and output of mathematical functions as well as workflow of execution for achieving an predefined objective. Algorithms are realized usually by means of implementation as computer programs for execution by automata. [IAO]
    
Report = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000088")
# A report is a document assembled by an author for the purpose of providing information for the audience. A report is the output of a documenting process and has the objective to be consumed by a specific audience. Topic of the report is on something that has completed. A report is not a single figure. [IAO]
    
DataFormatSpecification = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000098")
# A data format specification is the information content borne by the document published defining the specification. [IAO]
    
Image = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000101")
# An image is an affine projection to a two dimensional surface, of measurements of some quality of an entity or entities repeated at regular intervals across a spatial range, where the measurements are represented as color and luminosity on the projected on surface. [IAO]
    
VersionNumber = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000129")
# A version number is an information content entity which is a sequence of characters borne by part of each of a class of manufactured products or its packaging and indicates its order within a set of other products having the same name. [IAO]
    
SerialNumber = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000131")
# A serial number is an information content entity which is a unique sequence of characters borne by part of manufactured product or its packaging that is assigned to each individual in some class of products, and so can serve as a way to identify an individual product within the class. Serial numbers can be encoded in a variety of other information objects, such as bar codes, numerals, or patterns of dots. [IAO]
    
LotNumber = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000132")
# A lot number is an information content entity which is an identical sequence of character borne by part of manufactured product or its packaging for each instances of a product class in a discrete batch of an item. [IAO]
    
TextualEntity = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000300")
# A textual entity is a part of a manifestation (FRBR sense), a generically dependent continuant whose concretizations are patterns of glyphs intended to be interpreted as words, formulas, etc.
    
Caption = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000304")
# A textual entity that describes a figure [IAO]
    
Figure = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000308")
# An information content entity consisting of a two dimensional arrangement of information content entities such that the arrangement itself is about something. [IAO]
    
Diagram = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000309")
# A figure that expresses one or more propositions. [IAO]
    
Document = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000310")
# A collection of information content entities intended to be understood together as a whole [IAO]
    
LineGraph = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000573")
# A line graph is a type of graph created by connecting a series of data points together with a line. [IAO]
    
CentrallyRegisteredIdentifierSymbol = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000577")
# A symbol that is part of a CRID and that is sufficient to look up a record from the CRID&apos;s registry. [IAO]
    
CentrallyRegisteredIdentifier = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000578")
# An information content entity that consists of a CRID symbol and additional information about the CRID registry to which it belongs. [IAO]
    
CentrallyRegisteredIdentifierRegistry = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000579")
# A CRID registry is a dataset of CRID records, each consisting of a CRID symbol and additional information which was recorded in the dataset through a assigning a centrally registered identifier process. [IAO]
    
WrittenName = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000590")
# A textual entity that denotes a particular in reality. [IAO]
    
Human = onto.search_one(iri="http://purl.obolibrary.org/obo/NCBITaxon_9606")
# A member of the the species Homo sapiens. [Allotrope]
    
ElectronicSignature = onto.search_one(iri="http://purl.obolibrary.org/obo/NCIT_C142533")
# An electronic version of an individual&apos;s name or personal mark used to sign electronic documents, signifying that the writing which precedes accords with one&apos;s wishes and intentions. [NCI]
    
PharmaceuticalDosageForm = onto.search_one(iri="http://purl.obolibrary.org/obo/NCIT_C42636")
# The form in which active and/or inert ingredient(s) are physically presented. [NCI]
    
Server = onto.search_one(iri="http://purl.obolibrary.org/obo/NCIT_C48297")
# A server is a computer which provides some service for other computers connected to it via a network. [NCI]
    
ReagentRole = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000086")
# A role inhering in a biological or chemical entity that is intended to be applied in a scientific technique to participate (or have molecular components that participate) in a chemical reaction that facilitates the generation of data about some entity distinct from the bearer, or the generation of some specified material output distinct from the bearer. [OBI]
    
Plan = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000260")
# A plan is a realizable entity that is the inheres in a bearer who is committed to realizing it as a planned process. [OBI]
    
Organism = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0100026")
# A material entity that is an individual living system, such as animal, plant, bacteria or virus, that is capable of replicating or reproducing, growth and maintenance in the right environment. An organism may be unicellular or made up, like humans, of many billions of cells divided into specialized tissues and organs. [OBI]
    
CurveFitting = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0200072")
# Curve fitting is a data transformation that is the process of constructing a curve, or mathematical function, that has the best fit to a series of data points, possibly subject to constraints. [Wikipedia]
    
Speed = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000008")
# A physical quality inhering in a bearer by virtue of the bearer&apos;s scalar absolute value of the rate of change of the bearer&apos;s position. [PATO]
    
Color_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000014")
# A color is a composite chromatic quality composed of hue, saturation and intensity parts. [PATO]
    
Fluorescence_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000018")
# Fluorescence is a luminescence which occurs essentially only during the irradiation of a substance by electromagnetic radiation. [IUPAC]
    
Composition = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000025")
# A single physical entity inhering in an bearer by virtue of the bearer&apos;s quantities or relative ratios of subparts. [PATO]
    
Concentration_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000033")
# Concentration is a molecular quality inhering in a substance by virtue of the amount of the bearer&apos;s there is mixed with another substance. [PATO]
    
Hardness_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000048")
# A physical quality inhering in a bearer by virtue of the bearer&apos;s resistance to pressure, being broken, or pierced.
    
Morphology = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000051")
# A quality of a single physical entity inhering in the bearer by virtue of the bearer&apos;s size or shape or structure. [PATO]
    
Shape_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000052")
# A morphological quality inhering in a bearer by virtue of the bearer&apos;s ratios of distances between its features (points, edges, surfaces and also holes etc). [PATO]
    
Size_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000117")
# A morphology quality inhering in a bearer by virtue of the bearer&apos;s physical magnitude. [PATO]
    
Length_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000122")
# A 1-D extent quality which is equal to the distance between two points. [PATO]
    
Mass_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000125")
# A physical quality that inheres in a bearer by virtue of the proportion of the bearer&apos;s amount of matter. [PATO]
    
Position_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000140")
# Position is a  spatial quality inhering in a bearer by virtue of the bearer&apos;s spatial location relative to other objects in the vicinity. [PATO]
    
Structure = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000141")
# A morphology quality inhering in a bearer by virtue of the bearer&apos;s relative position, shape, arrangements and connectivity of an material entity&apos;s various parts; the pattern underlying its form. [PATO]
    
Temperature_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000146")
# A physical quality of the thermal energy of a system. [PATO]
    
Viability_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000169")
# An organismal quality inhering in a bearer or a population by virtue of the bearer&apos;s disposition to survive and develop normally or the number of surviving individuals in a given population. [PATO]
    
Viable = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000719")
# A viability quality inhering in a bearer or a population by virtue of the bearer&apos;s ability to survive or the long term survival ability of a given population. [PATO]
    
Thickness_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000915")
# A 1-D extent quality which is equal to the dimension through an object as opposed to its length or width. [PATO]
    
Volume_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000918")
# A 3-D extent quality inhering in a bearer by virtue of the bearer&apos;s amount of 3-dimensional space it occupies.
    
Width_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000921")
# A 1-D extent quality which is equal to the distance from one side of an object to another side which is opposite. [PATO]
    
Permeability = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000970")
# A structural quality inhering in a bearer by virtue of the bearer&apos;s disposition to being permeated or pervaded by a gas or liquid (as by osmosis or diffusion). [PATO]
    
Porosity = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000973")
# A permeability quality inhering in a bearer by virtue of the bearer&apos;s disposition to admit the passage of gas or liquid through pores or interstices. [PATO]
    
FullyPorous = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000984")
# A porosity quality inhering in a bearer by virtue of the bearer&apos;s being capable of admitting the passage of gas or liquid through pores or interstices. [PATO]
    
Viscosity_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0000992")
# A physical quality of a fluid inhering in a bearer by virtue of the bearer&apos;s disposition to internal resistance to flow. [PATO]
    
MassDensity_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001019")
# A physical quality which inheres in a bearer by virtue of some influence is exerted by the bearer&apos;s mass per unit size.
    
Pressure_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001025")
# A physical quality that inheres in a bearer by virtue of the bearer&apos;s amount of force per unit area it exerts.
    
Force_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001035")
# A physical quality inhering in a bearer by virtue of the bearer&apos;s rate of change of momentum. [PATO]
    
Concentrated = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001159")
# A concentration that is relatively high. [Allotrope]
    
Diluted = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001161")
# A concentration which is relatively low. [PATO]
    
Strength_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001230")
# A quality inhering in a bearer by virtue of the bearer&apos;s power or force.
    
Wavelength_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001242")
# A physical quality which is equal to the distance between repeating units of a wave pattern. [PATO]
    
ElectromagneticRadiationQuality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001291")
# A physical quality that inheres in an bearer by virtue of how that bearer interacts with electromagnetic radiation. [PATO]
    
OpticalQuality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001300")
# An EM radiation quality in which the EM radiation is within the fiat range of the spectrum visible deemed to be light. [PATO]
    
Area_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001323")
# An area is a 2-D extent quality inhering in a bearer by virtue of the bearer&apos;s two dimensional extent. [PATO]
    
Diameter_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001334")
# A length quality which is equal to the length of any straight line segment that passes through the center of a circle and whose endpoints are on the circular boundary. [PATO]
    
AngularVelocity_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001413")
# A physical quality inhering in a bearer by virtue of the rate of the bearer&apos;s angular movement about an axis; the angle rotated in a given time. [PATO]
    
Alive = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001421")
# A viability quality inhering in a bearer by virtue of the bearer&apos;s condition before death. [PATO]
    
Dead = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001422")
# A viability quality inhering in a bearer by virtue of the cessation of the bearer&apos;s life. [PATO]
    
FlowRate_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001574")
# A physical quality inhering in a bearer by virtue of the bearer&apos;s motion through a surface per time. [Allotrope]
    
Conductivity_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001585")
# A physical quality inhering in a bearer by virtue of the bearer&apos;s disposition to transmit of an entity through a medium. [PATO]
    
Depth_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001595")
# A 1-D extent quality inhering in a bearer by virtue of the bearer&apos;s downward or backward or inward dimenision. [PATO]
    
MolarMass_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001681")
# A physical quality that inheres in a homogeneous substance containing 6.02 x 10^23 atoms or molecules. [PATO]
    
ElectricalConductivity_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001757")
# Electrical conductivity is the quality inhered in a conductor that is the reciprocal of resistivity. [IUPAC]
    
Ph_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001842")
# A concentration quality inhering in a bearer by virtue of the bearer&apos;s containing acid (hydrogen ions). [PATO]
    
MovementQuality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001906")
# A physical quality inhering in a bearer by virtue of the bearer&apos;s participation in movement. [PATO]
    
OrganismalQuality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0001995")
# A quality that inheres in an entire organism or part of an organism. [PATO]
    
Osmolality_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002027")
# A concentration quality inhering in a bearer by virtue of the bearer&apos;s amount of osmoles of solute per kilogram of solvent. [PATO]
    
FluidFlowRate_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002243")
# A physical quality inhering in a fluid (liquid or gas) by virtue of the amount of fluid which passes through a given surface per unit time. [PATO]
    
MassFlowRate_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002244")
# A flow rate quality inhering in a substance by virtue of the mass of substance which passes through a given surface per unit time. [PATO]
    
Radius_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0002390")
# A length quality which is equal to the length of any straight line segment that passes from the center of a circle to any endpoint on the circular boundary. The radius is half of the diameter. [PATO]
    
Humidity_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/PATO_0015009")
# A quality inhering in air by virtue of the partial pressure exerted by the bearer&apos;s water vapour content. [PATO]
    