
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
DeviceSystem = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000074")
# An artificial system that is mainly composed of devices. [Allotrope]
    
PressureSensor = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000327")
# A sensor that measures the pressure. [Allotrope]
    
SampleInlet = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000462")
# A sample inlet is an in port of a measurement or separation device where sample material is passing in to the device. [Allotrope]
    
Port = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0000847")
# Connection point of a system through which flows material, energy or information. [Allotrope]
    
MeasuringSystem = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002141")
# A measuring system is a device system which has the designed function of measurement. [Allotrope]
    
PlumbingSystem = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002153")
# Plumbing is the system of pipes, tubing, drains, fittings, valves, and fixtures installed for the distribution of a liquid. [Wikipedia]
    
ArtificialSystem = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002158")
# A system that is created for a specific purpose. [Allotrope]
    
Sensor = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002184")
# A sensor is a component of a measuring system that is directly affected by a phenomenon, body, or substance carrying a quantity to be measured. [Allotrope]
    
InPort = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002190")
# An in port is a port in a device where material is flowing into the system boundary. [Allotrope]
    
OutPort = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002191")
# An out port is a port in a device where material is flowing out of the system boundary. [Allotrope]
    
DataSystem = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002232")
# A data system is an artificial  system of physical devices and software running on it designed to process information or control. [Allotrope]
    
LaboratoryInformationManagementSystem = onto.search_one(iri="http://purl.allotrope.org/ontologies/equipment#AFE_0002234")
# A laboratory information management system is a data system used in laboratories to manage laboratory operations. [Allotrope]
    
NaturalSystem = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001059")
# A system that can be discovered in nature. [Allotrope]
    
Signal = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001004")
# An information content entity that is an input or output in a process at the boundary of a system. The signal is sent or received via ports of the system. The signal conveys information about the behavior or attributes of some phenomenon. [Allotrope]
    
Noise = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001170")
# An information content entity that describes the unwanted random and systematic fluctuations to the signal that limit the ability to detect a signal contribution of interest. [Allotrope]
    
Signal_communication = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001964")
# A signal is information transported over an communication channel. [Allotrope]
    
PortRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000083")
# A site that is part of a system has the port role if a component is connected to other components or systems at the site and material or energy can flow at the site. [Allotrope]
    
ComponentRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000096")
# An granular part of an object aggregate that plays the role of a system. [Allotrope]
    
SystemRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000101")
# A role of an object aggregate that consists of multiple components that are causally integrated. [Allotrope]
    
SubsystemRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000102")
# Parts of a system that are a building a system on its own. [Allotrope]
    
SystemBondRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000146")
# A system bond is the role of a site where two components are connected via their ports. At this site energy or material can flow. [Allotrope]
    
PhysicalSignalRole = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000159")
# A signal is a role of some material entity that disposed to provide information. In the physical world, any quantity exhibiting variation in time or variation in space (such as an image) is potentially a signal that might provide information on the status of a physical system, or convey a message between observers, among other possibilities. [Allotrope, Wikipedia]
    
InitialResponse = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000275")
# The initial response is the role of an outgoing signal as it was generated raw without signal processing from a processing component. [Allotrope]
    
PrimaryResponse = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000276")
# The primary response is the role of an outgoing signal that serves the intended main function of the system. [Allotrope]
    
ReferenceSignal = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000335")
# Reference signal is the role of a signal that relates to another signal as reference for comparison. [Allotrope]
    
System = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002577")
# A material entity consisting of multiple components that are causally integrated. [RO]
    