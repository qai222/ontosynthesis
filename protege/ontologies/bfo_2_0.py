
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
Entity = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000001")
# An entity is anything that exists or has existed or will exist. [BFO]
    
Continuant = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000002")
# A continuant is an entity that persists, endures, or continues to exist through time while maintaining its identity. [BFO]
    
Occurrent = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000003")
# An occurrent is an entity that unfolds itself in time or it is the instantaneous boundary of such an entity (for example a beginning or an ending) or it is a temporal or spatiotemporal region which such an entity occupies a temporal region or occupies a spatiotemporal region. [BFO]
    
IndependentContinuant = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000004")
# b is an independent continuant if b is a continuant which is such that there is no c and no t such that b s-depends_on c at t. [BFO]
    
SpatialRegion = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000006")
# A spatial region is a continuant entity that is a continuant part of space R as defined relative to some frame R. [BFO]
    
TemporalRegion = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000008")
# A temporal region is an occurrent entity that is part of time as defined relative to some reference frame. [BFO]
    
SpatiotemporalRegion = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000011")
# A spatiotemporal region is an occurrent entity that is part of spacetime. [BFO]
    
Process = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000015")
# p is a process if p is an occurrent that has temporal proper parts and for some time t, p specifically depends on some material entity at t. [BFO]
    
Disposition = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000016")
# B is a disposition means: b is a realizable entity and b’s bearer is some material entity and b is such that if it ceases to exist, then its bearer is physically changed, and b’s realization occurs when and because this bearer is in some special physical circumstances, and this realization occurs in virtue of the bearer’s physical make-up. [BFO]
    
RealizableEntity = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000017")
# To say that b is a realizable entity is to say that b is a specifically dependent continuant that inheres in some independent continuant which is not a spatial region and is of a type instances of which are realized in processes of a correlated type.´[BFO]
    
Quality = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000019")
# A quality is a specifically dependent continuant that, in contrast to roles and dispositions, does not require any further process in order to be realized. [BFO]
    
SpecificallyDependentContinuant = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000020")
# b is a specifically dependent continuant if b is a continuant and there is some independent continuant c which is not a spatial region and which is such that b specifically depends on c at every time t during the course of b’s existence. [BFO]
    
Role = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000023")
# B is a role means: b is a realizable entity and b exists because there is some single bearer that is in some special physical, social, or institutional set of circumstances in which this bearer does not have to be and b is not such that, if it ceases to exist, then the physical make-up of the bearer is thereby changed. [BFO]
    
FiatObjectPart = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000024")
# B is a fiat object part if b is a material entity which is such that for all times t, if b exists at t then there is some object c such that b is a proper continuant part of c at t and c is demarcated from the remainder of c by a two-dimensional continuant fiat boundary. [BFO]
    
ObjectAggregate = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000027")
# B is an object aggregate means: b is a material entity consisting exactly of a plurality of objects as member parts at all times at which b exists. [BFO]
    
Site = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000029")
# B is a site means: b is a three-dimensional immaterial entity that is (partially or wholly) bounded by a material entity or it is a three-dimensional immaterial part thereof. [BFO]
    
Object = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000030")
# B is an object means: b is a material entity which manifests causal unity of one or other of the types causal unities and is of a type (a material universal) instances of which are maximal relative to this criterion of cau
    
GenericallyDependentContinuant = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000031")
# b is a generically dependent continuant if b is a continuant that generically depends on one or more other entities. [BFO]
    
Function = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000034")
# A function is a disposition that exists in virtue of the bearer’s physical make-up and this physical make-up is something the bearer possesses because it came into being, either through evolution (in the case of natural biological entities) or through intentional design (in the case of artifacts), in order to realize processes of a certain sort. [BFO]
    
ProcessBoundary = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000035")
# p is a process boundary if p is a temporal part of a process and p has no proper temporal parts. [BFO]
    
MaterialEntity = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000040")
# A material entity is an independent continuant that has some portion of matter as proper or improper continuant part. [BFO]
    
ContinuantFiatBoundary = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000140")
# B is a continuant fiat boundary if b is an immaterial entity that is of zero, one or two dimensions and does not include a spatial region as part. [BFO]
    
ProcessProfile = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000144")
# B is a process profile if there is some process c such that b is process profile of c. B is process profile of c holds when b is a proper occurrent part of c and there is some proper occurrent part d of c which has no parts in common with b and is mutually dependent on b and is such that b, c and d occupy the same temporal region. [BFO]
    
RelationalQuality = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000145")
# B is a relational quality if for some independent continuants c, d and for some time t: b is quality of c at t and b is quality of d at t. [BFO]
    
History = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000182")
# A history is a process that is the sum of the totality of processes taking place in the spatiotemporal region occupied by a material entity or site, including processes on the surface of the entity or within the cavities to which it serves as host. [BFO]
    