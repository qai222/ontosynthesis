
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
has_duration = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000072")
# Time is a measure in which events can be ordered from the past through the present into the future, and also the measure of durations of events and the intervals between them. [Wikipedia]
    
increment = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000180")
# The difference between two discrete points next to each other in a range of discrete values. [Allotrope]
    
selects = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000197")
# A planned process selects a participant if the participant is chosen to influence the process towards some objective but is itself not essentially changed by a process. [Allotrope]
    
refines = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000234")
# This relation indicates that the subject is a more concrete instance of the object. [Allotrope]
    
minimum = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000314")
# The lowest value of a range or a set of values. [Allotrope]
    
maximum = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000331")
# Highest value of a range. [Allotrope]
    
output_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000353")
# Relates an output entity such as a material or information object with a process that exists at the end of the process. [Allotrope]
    
input_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000354")
# Relates an input entity such a material entity or information object with a process that exists at the start of the process. [Allotrope]
    
is_condition_for = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000355")
# A condition that restricts an entity. [Allotrope]
    
has_ingredient = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000365")
# An ingredient is a material that enters into a compound or is part of any combination or mixture. [Allotrope]
    
has_shape = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000386")
# Inverse of SHACL targets e.g. sh:targetClass or sh:targetNode. [Allotrope]
    
has_scope = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000388")
# A scope defines a situation or context in which a dependent entity such as a condition or contextual role occurs or is valid. [Allotrope]
    
has_output = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000395")
# Relates a process with a continuant that participates in the process and exists at the end of the process. [Allotrope]
    
has_input = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000399")
# Relates a process with a continuant that participates in the process and exists at the start of the process. [Allotrope]
    
has_condition = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000408")
# An entity has a condition that restricts the entity in some way. [Allotrope]
    
has_data_input = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000542")
# Relates a process with an information object that participates in a process and exists the start of the process. [Allotrope]
    
has_data_output = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000544")
# Relates a process with an information object that participates in the process and exists the end of the process. [Allotrope]
    
has_material_output = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000546")
# The material that is output of the process. [Allotrope]
    
has_item = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000551")
# This property links a collection to a member item. [Allotrope]
    
data_input_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000553")
# Inverse of &apos;has data input&apos;. [Allotrope]
    
material_input_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000554")
# Inverse of &apos;has material input&apos;. [Allotrope]
    
maximum_exclusive = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000557")
# The highest value of a range excluding the boundary value. [Allotrope]
    
maximum_inclusive = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000558")
# The highest value of a range including the boundary value. [Allotrope]
    
minimum_exclusive = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000560")
# The lowest value of a range or set of values excluding the boundary value. [Allotrope]
    
minimum_inclusive = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000561")
# The lowest value of a range or set of values including the boundary value. [Allotrope]
    
has_material_input = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000696")
# Refers to the material entity that is an input of a process. [Allotrope]
    
has_log = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000834")
# The relation between a process and its log. A log is a steadily updated information object containing data of events in time such as process executions. [Allotrope]
    
component_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000939")
# A physical object that is a component that is a physical part of another physical object that is a system. [Allotrope]
    
composed_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000940")
# The property specifies of which kind of general portion of material something is built of. [Allotrope]
    
has_component = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000972")
# A physical object that forms a system that has as part a physical entity that is one of its components. [Allotrope]
    
has_port = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000974")
# Relation between a system and a component of it that has the role of a port in the system though which material, energy or information flows in or out of the system. [Allotrope]
    
has_capability = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0000976")
# The relation of an entity to a description of it which refers to the qualification of an entity to perform a certain function. [Allotrope]
    
contains = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0001048")
# The relation between a container and its physical content. A material entity a contains a material entity b if b is located in some cavity of a. [Allotrope]
    
contained_in = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0001049")
# Inverse of contains. [Allotrope]
    
has_classification = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0001154")
# A classification is a kind of categorization in order to differentiate between different classes of objects. [Allotrope]
    
connected_to_source = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0001178")
# A system that is attached to another system by an ingoing port. [Allotrope]
    
connected_to_destination = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0001179")
# A system that is attached to another system by an outgoing port. [Allotrope]
    
has_reference = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0001550")
# Reference object relates an entity A to some entity B that is taken as a reference for A in a certain context. [Allotrope]
    
satisfies = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002674")
# The relation between a proposition about of a portion of reality and a process asserting that the process is described truthfully by the description. [Allotrope]
    
by_way_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002677")
# The relation between a function with an objective and another function that when realized acts as a proxy to achieve the objective of the first. [Allotrope]
    
tracks_quality = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002682")
# A relation between a process profile and a changing determinable quality of some participant of the process of the profile. [Allotrope]
    
quantified_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002684")
# Relation of something that is quantified by some quantity value which expresses it relative to some other thing. [Allotrope]
    
quality_tracked_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002685")
# The relation between a quality and a process profile in which the quality is changing. [Allotrope]
    
process_quantified_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002686")
# Relation of some process that is quantified by some quantity value which expresses its duration relative to other process or a temporal aggregation function on the quantification of a quality of some participant over this duration. [Allotrope]
    
profile_mean_quantified_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002687")
# The quantity value that is the result of averaging a quality of some participant of the process over the duration of the process or the quantification of the participant&apos;s quality at the temporal granularity of the duration of the process. [Allotrope]
    
profile_maximum_quantified_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002688")
# The temporal maximum quantified by is the maximum of the quantification of some quality of a participant that occurred during the process. [Allotrope]
    
profile_minimum_quantified_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002689")
# The temporal minimum quantified by is the minimum of the quantification of some quality of a participant that occurred during the process. [Allotrope]
    
quality_quantified_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002690")
# Quantification of some determinate quality which expresses it relative to some other (known) determinate quality. [Allotrope]
    
has_range = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002696")
# Relation to a data item that describes the boundaries of possible or existing qualities, process profiles or process durations that can be ordered. [Allotrope]
    
describes = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002699")
# Describes is a property of an entity which has the ability to indicate or denote certain characteristics in another entity. [Allotrope]
    
quality_profile_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002703")
# The relation of a process profile of some changing quality to a process. [Allotrope]
    
specifies = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002704")
# Specifies is a relation between a specification and the object specified. [Allotrope]
    
has_identifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002716")
# The relation of an entity to an identifier that denotes it. [Allotrope]
    
identifies = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002717")
# The relation of an identifier to the entity it denotes. [Allotrope]
    
occurrent_quantified_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002718")
# Occurrent quantified by relates an occurrent entity with an information content entity that is a quantification of the occurrent (duration, rate). [Allotrope]
    
item_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002720")
# In collection relates an item to a collection entity. [Allotrope]
    
quality_influenced_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002722")
# Inverse of quality influences. [Allotrope]
    
quality_influences = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002723")
# Holds between qualities a and b  such that if a process changes the quality to some other instance a&apos; then for some a&apos; it is necessary that b changes to another instance b&apos;. [Allotrope]
    
quality_strongly_influences = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002724")
# Holds between qualities a and b  such that if a process changes the quality to some other instance a&apos; != a then for all a&apos; it is necessary that b changes to another instance b&apos; != b. [Allotrope]
    
quality_strongly_influenced_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002725")
# Inverse of quality strongly influences. [Allotrope]
    
contextual_role_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002726")
# Inverse of has contextual role. [Allotrope]
    
lacks = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002727")
# Property describing the absence of a particular in relation to another particular depending on its spatio-temporal existence. [Allotrope]
    
facet_implemented_as = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002729")
# The relation between the abstract facet and a specific information that represents the facet. [Allotrope]
    
has_contextual_role = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002730")
# The relation between an information object and its contextual role. [Allotrope]
    
in_process = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002731")
# The relation between a conceptual role and the process where the contextual role is realized. [Allotrope]
    
data_output_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002734")
# Inverse of &apos;has data output&apos;. [Allotrope]
    
material_output_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002735")
# Inverse of &apos;has material output&apos;. [Allotrope]
    
has_proposition = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002736")
# The relation between a representation and its content independent of form. [Allotrope]
    
has_representation_form = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002737")
# The relation between the information and the way it is represented. [Allotrope]
    
has_effort_component = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002740")
# Has effort component relates an energy with its quality of effort. [Allotrope]
    
has_flow_component = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002741")
# Has flow component relates an energy with its quality of flow. [Allotrope]
    
has_information_derived_from = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002744")
# An information content entity has information derived from some other information content entity, if there is a data processing that transforms the other into it, either transforming the representational form or the content. [Allotrope]
    
affects = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002745")
# P has direct input c if and only if c is a participant in p, c is present at the start of p, and the state of c is modified during p, c is present at the end of p. [Allotrope]
    
consumes = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002748")
# P has output c if and only if c is a participant in p, c is present at the start of p, and c is not present at the end of p. [Allotrope]
    
targets = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002750")
# A planned process targets a continuant if the continuant is a participant in the process and it in important part of towards the main objective of the process&apos; plan. [Allotrope]
    
has_proper_part = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002793")
# Has proper part is an antisymmetric, irreflexive (normally transitive) relation between a whole and a distinct part. [SIO]
    
facet_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002800")
# Facet of relates two information content entities where one information content entity is an aspect of the other one. [Allotrope]
    
has_categorical_value = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002801")
# Has categorical value is a facet that relates an information content entity to a code that describes a category for classification. [Allotrope]
    
has_description = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002802")
# Has description relates an entity to an information content entity that is its description. [Allotrope]
    
has_facet = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002803")
# Relation between an information content entity and some part of it called a facet that is covers some general aspect of information context. [Allotrope]
    
has_specification = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002805")
# Has specification relates an entity to an information content entity that is its specification. [Allotrope]
    
classifies = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002806")
# The relation between a classification and something that is grouped by the classification. [Allotrope]
    
implements_facet = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002807")
# Inverse of facet concretized as. [Allotrope]
    
quantifies = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002816")
# The relation of an information object to an entity that gives some indication of magnitude of a quality, information facet or process. [Allotrope]
    
index_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002819")
# The relation between an index and the entity in an aggregate or list it denotes. [Allotrope]
    
has_index = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002820")
# The relation between an object and an index that denotes the object within an aggregate the object is member of. [Allotrope]
    
proxy_for = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002821")
# The relation between a proxy entity and a target entity where the target entity is a real participant in some process or the subject of an information content entity but is not referenced directly, but instead the proxy is used as a surrogate or representation for it. [Allotrope]
    
has_concept = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002822")
# The relation an entity and an associated SKOS concept. [Allotrope]
    
has_direct_part = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002832")
# A core relation that holds between a whole and a proper part without an intermediate part at a level of granularity. [Allotrope]
    
is_followed_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002833")
# Is followed by is a relation between entities that are items in an ordered sequence. For each pair of entities P, S being a member of the sequence, there exists an ordering function o so that o(P) &lt; o(S). Iff o(P) &lt; o(S) then P is followed by S. [Allotrope]
    
follows = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002834")
# Follows is a relation between entities that are items in an ordered sequence. For each pair of entities P, S being a member of the sequence, there exists an ordering function o so that o(P) &lt; o(S).  Iff o(S) &gt; o(P) the S follows P. [Allotrope]
    
is_immediately_followed_by = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002835")
# Is immediately followed by is a relation between entities that are items in an ordered sequence. For each pair of entities P, S being a member of the sequence, there exists an ordering function o so that o(P) &lt; o(S).  Iff for members P, S of the sequence, there is no member I that o(P) &lt; o(I) &lt; o(S), then P is immediately followed by S. [Allotrope]
    
immediately_follows = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002836")
# Immediately follows is a relation between entities that are items in an ordered sequence. For each pair of entities P, S being a member of the sequence, there exists an ordering function o so that o(P) &lt; o(S).  Iff for members P, S of the sequence, there is no member I that o(S) &gt; o(I) &gt; o(P), then S follows P. [Allotrope]
    
relation_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002837")
# Relation of is a relation of a relational entity to the referred entities. [Allotrope]
    
relates_to = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002838")
# Relates to is a relation between a directed relational entity to the target of the relation. [Allotrope]
    
relates_from = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002839")
# Relates from is a relation between a directed relational entity to the source of the relation. [Allotrope]
    
defines = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002842")
# The relation between a definition and the entity that is defined by it. [Allotrope]
    
has_definition = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002843")
# Has definition relates an entity to an information content entity that is its definition. [Allotrope]
    
ingredient_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002845")
# Inverse of has ingredient. [Allotrope]
    
proper_part_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002846")
# Inverse of has proper part. [Allotrope]
    
direct_part_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002847")
# Inverse of has direct part. [Allotrope]
    
observes = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002848")
# A process observing process p observes a process q if p produces information about the process q, such as the duration, or about some independent continuant participating in q in an important active or passive role. [Allotrope]
    
applies = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002849")
# An entity applies a specification or mathematical function, if the specification specifies the entity and the entity conforms or follows the specification. [Allotrope]
    
fulfills = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002853")
# A relation between a realizable entity and a requirement, that states that the process or process boundary that realizes it, satisfies all conditions of the requirement. [Allotrope]
    
is_log_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002855")
# The relation between a log  and the process the log is describing. [Allotrope]
    
is_capability_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002856")
# The relation between a capability proposition and the subject it is about. [Allotrope]
    
related_by_order_to = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002858")
# A relation between entities that are ordered into a list. [Allotrope]
    
target_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002863")
# A continuant is target of a planned process if the continuant is a participant in the process and it in important part of towards the main objective of the process&apos; plan. [Allotrope]
    
selected_in = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002864")
# A continuant is selected or used in planned process if the participant is chosen to influence the process towards some objective but is itself not essentially changed by a process. [Allotrope]
    
has_state = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002875")
# Has state is a relation between an continuant c and a state s where the c participates in s and s is expressed in the same way in terms of c at all times during s. [Allotrope]
    
state_of = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002876")
# A relation between a state s and a continuant c where the c is a participant of s and s is expressed in the same way in terms of c at all times during s. [Allotrope]
    
has_statistic_datum_role = onto.search_one(iri="http://purl.allotrope.org/ontologies/property#AFX_0002878")
# The relation between an information content object and its statistic datum role. [Allotrope]
    
preceded_by = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000062")
# X is preceded by y if and only if the time point at which y ends is before or equivalent to the time point at which x starts. Formally: x preceded by y if and only if ω(y) &lt;= α(x), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point. [RO]
    
precedes = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000063")
# X precedes y if and only if the time point at which x ends is before or equivalent to the time point at which y starts. Formally: x precedes y if and only if ω(x) &lt;= α(y), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point. [RO]
    
occurs_in = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000066")
# b occurs_in c =def b is a process and c is a material entity or immaterial entity&amp; there exists a spatiotemporal region r and b occupies_spatiotemporal_region r.&amp; forall(t) if b exists_at t then c exists_at t &amp; there exist spatial regions s and s’ where &amp; b spatially_projects_onto s at t&amp; c is occupies_spatial_region s’ at t&amp; s is a proper_continuant_part_of s’ at t [RO]
    
contains_process = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000067")
# inverse of occurs in
    
located_at = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000083")
# b located at r means that r is a spatial region in which independent continuant b is exactly located. [BFO]
    
exists_at = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000108")
# b exists_at t means: b is an entity which exists at some temporal region t. [BFO]
    
has_occurrent_part = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000117")
# b has occurrent part c =Def. b has part c &amp; b and c are occurrents.
    
has_proper_occurrent_part = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000118")
# B has_proper_occurrent_part c =Def. b has_occurrent_part c &amp; b and c are not identical. [BFO]
    
occupies_spatiotemporal_region = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000130")
# p occupies_spatiotemporal_region s. This is a primitive relation between an occurrent p and the spatiotemporal region s which is its spatiotemporal extent. [BFO]
    
part_of_occurrent = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000132")
# b occurrent_part_of c =Def. b is a part of c &amp; b and c are occurrents. [BFO]
    
proper_part_of_occurrent = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000138")
# B proper_occurrent_part_of c =Def. b occurrent_part_of c &amp; b and c are not identical. [BFO]
    
temporal_part_of = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000139")
# B temporal_part_of c =Def.b occurrent_part_of c &amp; &amp; for some temporal region t, b occupies_temporal_region t &amp; for all occurrents d, t (if d occupies_temporal_region t &amp; t? occurrent_part_of t then (d occurrent_part_of a iff d occurrent_part_of b)). [BFO]
    
during_which_exists = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000157")
# inverse of exists at [BFO]
    
history_of = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000184")
# b history_of c if c is a material entity or site and b is a history that is the unique history of c
    
has_history = onto.search_one(iri="http://purl.obolibrary.org/obo/BFO_0000185")
# inverse of history of
    
denotes = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000219")
# Denotes is a primitive, instance-level, relation obtaining between an information content entity and some portion of reality. Denotation is what happens when someone creates an information content entity E in order to specifically refer to something. The only relation between E and the thing is that E can be used to &apos;pick out&apos; the thing. This relation connects those two together. Freedictionary.com sense 3: To signify directly; refer to specifically [IAO]
    
has_grain = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000643")
# The relation of the cells in the finger of the skin to the finger, in which an indeterminate number of grains are parts of the whole by virtue of being grains in a collective that is part of the whole, and in which removing one granular part does not nec- essarily damage or diminish the whole. Ontological Whether there is a fixed, or nearly fixed number of parts - e.g. fingers of the hand, chambers of the heart, or wheels of a car - such that there can be a notion of a single one being missing, or whether, by contrast, the number of parts is indeterminate - e.g., cells in the skin of the hand, red cells in blood, or rubber molecules in the tread of the tire of the wheel of the car. [OBI]
    
is_grain_of = onto.search_one(iri="http://purl.obolibrary.org/obo/OBI_0000645")
# A relation between granular parts and the whole of which they are a part. Granular parts have indeterminate number such that removing one granular part does not necessarily damage or diminish the whole. [OBI]
    
bearer_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000053")
# A relation between an independent continuant (the bearer) and a specifically dependent continuant (the dependent), in which the dependent specifically depends on the bearer for its existence. [RO]
    
participates_in = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000056")
# A relation between a continuant and a process, in which the continuant is somehow involved in the process [RO]
    
has_participant = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000057")
# A relation between a process and a continuant, in which the continuant is somehow involved in the process [RO]
    
concretized_by = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000058")
# A relationship between a generically dependent continuant and a specifically dependent continuant, in which the generically dependent continuant depends on some independent continuant in virtue of the fact that the specifically dependent continuant also depends on that same independent continuant. A generically dependent continuant may be concretized as multiple specifically dependent continuants. [RO]
    
concretizes = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000059")
# A relationship between a specifically dependent continuant and a generically dependent continuant, in which the generically dependent continuant depends on some independent continuant in virtue of the fact that the specifically dependent continuant also depends on that same independent continuant. Multiple specifically dependent continuants can concretize the same generically dependent continuant. [RO]
    
function_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000079")
# A relation between a function and an independent continuant (the bearer), in which the function specifically depends on the bearer for its existence. [RO]
    
quality_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000080")
# Inverse of has quality [RO]
    
role_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000081")
# A relation between a role and an independent continuant (the bearer), in which the role specifically depends on the bearer for its existence. [RO]
    
has_function = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000085")
# A relation between an independent continuant (the bearer) and a function, in which the function specifically depends on the bearer for its existence. [RO]
    
has_quality = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000086")
# A relation between an independent continuant (the bearer) and a quality, in which the quality specifically depends on the bearer for its existence. [RO]
    
has_role = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000087")
# A relation between an independent continuant (the bearer) and a role, in which the role specifically depends on the bearer for its existence [RO]
    
has_disposition = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000091")
# A relation between an independent continuant (the bearer) and a disposition, in which the disposition specifically depends on the bearer for its existence, [RO]
    
disposition_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0000092")
# Inverse of has disposition [RO]
    
derives_from = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0001000")
# A relation between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity. [RO]
    
derives_into = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0001001")
# A relation between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity. [RO]
    
location_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0001015")
# a relation between two independent continuants, the location and the target, in which the target is entirely within the location [RO]
    
located_in = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0001025")
# A relation between two independent continuants, the target and the location, in which the target is entirely within the location. [RO]
    
occurrent_part_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002012")
# A part of relation that applies only between occurrents. [RO]
    
before_or_simultaneous_with = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002081")
# Primitive instance level timing relation between events [RO]
    
simultaneous_with = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002082")
# t1 simultaneous_with t2 iff:= t1 before_or_simultaneous_with t2 and not (t1 before t2) [RO]
    
before = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002083")
# t1 before t2 iff:= t1 before_or_simulataneous_with t2 and not (t1 simultaneous_with t2) [RO]
    
ends_after = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002086")
# X ends_after Y iff: end(Y) before_or_simultaneous_with end(X) [RO]
    
immediately_preceded_by = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002087")
# X immediately_preceded_by Y iff: end(X) simultaneous_with start(Y) [RO]
    
immediately_precedes = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002090")
# X immediately_precedes_Y iff: end(X) simultaneous_with start(Y) [RO]
    
starts_during = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002091")
# X starts_during Y iff: (start(Y) before_or_simultaneous_with start(X)) AND (start(X) before_or_simultaneous_with end(Y)) [RO]
    
happens_during = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002092")
# X happens_during Y iff: (start(Y) before_or_simultaneous_with start(X)) AND (end(X) before_or_simultaneous_with end(Y)) [RO]
    
ends_during = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002093")
# X ends_during Y iff: ((start(Y) before_or_simultaneous_with end(X)) AND end(X) before_or_simultaneous_with end(Y). [RO]
    
overlaps = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002131")
# x overlaps y if and only if there exists some z such that x has part z and z part of y [RO]
    
continuous_with = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002150")
# X continuous_with Y if and only if X and Y share a fiat boundary. [RO]
    
spatially_disjoint_from = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002163")
# A is spatially_disjoint_from B if and only if they have no parts in common [RO]
    
connected_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002170")
# a is connected to b if and only if a and b are discrete structure, and there exists some connecting structure c, such that c connects a and b [RO]
    
connects = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002176")
# C connects a if and only if there exist some b such that a and b are similar parts of the same system, and c connects b, specifically, c connects a with b. When one structure connects two others it unites some aspect of the function or role they play within the system. [IAO]
    
attached_to_part_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002177")
# A is attached to part of b if a is attached to b, or a is attached to some p, where p is part of b. [IAO]
    
regulates = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002211")
# Process(P1) regulates process(P2) iff: P1 results in the initiation or termination of P2 OR affects the frequency of its initiation or termination OR affects the magnitude or rate of output of P2. [RO]
    
negatively_regulates__process_to_process = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002212")
# Process(P1) negatively regulates process(P2) iff: P1 terminates P2, or P1 descreases the the frequency of initiation of P2 or the magnitude or rate of output of P2. [RO]
    
positively_regulates__process_to_process = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002213")
# Process(P1) positively regulates process(P2) iff: P1 initiates P2, or P1 increases the the frequency of initiation of P2 or the magnitude or rate of output of P2. [RO]
    
capable_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002215")
# A relation between a material entity (such as a cell) and a process, in which the material entity has the ability to carry out the process. [RO]
    
capable_of_part_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002216")
# C stands in this relationship to p if and only if there exists some p&apos; such that c is capable_of p&apos;, and p&apos; is part_of p. [RO]
    
actively_participates_in = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002217")
# X actively participates in y if and only if x participates in y and x realizes some active role [RO]
    
has_active_participant = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002218")
# X has participant y if and only if x realizes some active role that inheres in y [RO]
    
surrounded_by = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002219")
# X surrounded_by y if and only if (1) x is adjacent to y and for every region r that is adjacent to x, r overlaps y (2) the shared boundary between x and y occupies the majority of the outermost boundary of x [RO]
    
adjacent_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002220")
# X adjacent to y if and only if x and y share a boundary. [RO]
    
surrounds = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002221")
# Inverse of surrounded by [RO]
    
temporally_related_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002222")
# A relation that holds between two occurrents. This is a grouping relation that collects together all the Allen relations. [RO]
    
starts = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002223")
# Inverse of starts with [RO]
    
starts_with = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002224")
# X starts with y if and only if x has part y and the time point at which x starts is equivalent to the time point at which y starts. Formally: α(y) = α(x) and ω(y) &lt; ω(x), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point. [RO]
    
ends = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002229")
# Inverse of ends with [RO]
    
ends_with = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002230")
# X ends with y if and only if x has part y and the time point at which x ends is equivalent to the time point at which y ends. Formally: α(y) &gt; α(x) and ω(y) = ω(x), where α is a function that maps a process to a start point, and ω is a function that maps a process to an end point. [RO]
    
acts_upstream_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002263")
# C involved in regulation of p if c enables &apos;p&apos; and p&apos; causally upstream of p [RO]
    
acts_upstream_of_or_within = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002264")
# C acts upstream of or within p if c is enables &apos;p&apos; and p&apos; causally upstream of or within p [RO]
    
inheres_in_part_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002314")
# Q inheres in part of w if and only if there exists some p such that q inheres in p and p part of w. [RO]
    
mereotopologically_related_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002323")
# A mereological relationship or a topological relationship [RO]
    
contributes_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002326")
# if and only if exists c&apos;, p&apos; c part_of c&apos; and c&apos; capable_of p and c capable_of p&apos; and p&apos; part_of p then c contributes_to p [RO]
    
functionally_related_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002328")
# This is a grouping relation that collects relations used for the purpose of connecting structure and function. [RO]
    
involved_in = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002331")
# C involved_in p if and only if c enables some process p&apos;, and p&apos; is part of p [RO]
    
regulates_levels_of__process_to_entity = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002332")
# P regulates levels of c if p regulates some amount (PATO:0000070) of c [RO]
    
enabled_by = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002333")
# inverse of enables [RO]
    
negatively_regulated_by = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002335")
# Inverse of negatively regulates [RO]
    
positively_regulated_by = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002336")
# Inverse of positively regulates [RO]
    
related_via_localization_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002337")
# A relationship that holds via some process of localization. [RO]
    
has_target_start_location = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002338")
# This relationship holds between p and l when p is a transport or localization process in which the outcome is to move some cargo c from some initial location l to some destination. [RO]
    
has_target_end_location = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002339")
# This relationship holds between p and l when p is a transport or localization process in which the outcome is to move some cargo c from a an initial location to some destination l. [RO]
    
results_in_transport_along = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002341")
# Holds between p and l when p is a transportation or localization process and the outcome of this process is to move c from one location to another, and the route taken by c follows a path that is aligned_with l. [RO]
    
results_in_transport_across = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002342")
# Holds between p and m when p is a transportation or localization process and the outcome of this process is to move c from one location to another, and the route taken by c follows a path that crosses m. [RO]
    
member_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002350")
# Inverse of has member
    
has_member = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002351")
# Has member is a mereological relation between a collection and an item. [RO]
    
attached_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002371")
# A is attached to b if and only if a and b are discrete objects or object parts, and there are physical connections between a and b such that a force pulling a will move b, or a force pulling b will move a. [IAO]
    
spatially_coextensive_with = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002379")
# X spatially_coextensive_with y if and only if x and y have the same location [RO]
    
causally_downstream_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002404")
# inverse of upstream of [RO]
    
immediately_causally_downstream_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002405")
# inverse of immediately causally upstream of
    
causally_upstream_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002411")
# P is causally upstream of q if and only if p precedes q and p and q are linked in a causal chain [RO]
    
immediately_causally_upstream_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002412")
# P is immediately causally upstream of q if and only if both (a) p immediately precedes q and (b) p is causally upstream of q. In addition, the output of p must be an input of q. [RO]
    
causally_upstream_of_or_within = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002418")
# P &apos;causally upstream or within&apos; q if and only if (1) the end of p is before the end of q and (2) the execution of p exerts some causal influence over the outputs of q; i.e. if p was abolished or the outputs of p were to be modified, this would necessarily affect q. [RO]
    
involved_in_regulation_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002428")
# C involved in regulation of p if c is involved in some &apos;p&apos; and p&apos; regulates some p [RO]
    
involved_in_or_involved_in_regulation_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002431")
# C involved in or regulates p if and only if either (i) c is involved in p or (ii) c is involved in regulation of p [RO]
    
interacts_with = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002434")
# A relationship that holds between two entities in which the processes executed by the two entities are causally connected. [RO]
    
partner_in = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002461")
# relation used for defining interaction relations. An interaction relation holds when there is an interaction event with two partners. In a directional interaction, one partner is deemed the subject, the other the target [RO]
    
subject_participant_in = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002462")
# relation used for defining interaction relations; the meaning of s &apos;subject participant in&apos; p is determined by the type of p, where p must be a directional interaction process. [RO]
    
target_participant_in = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002463")
# Relation used for defining interaction relations; the meaning of s &apos;target participant in&apos; p is determined by the type of p, where p must be a directional interaction process [RO]
    
causal_agent_in_process = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002500")
# A relationship between a material entity and a process where the material entity has some causal role that influences the process. [RO]
    
causal_relation_between_processes = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002501")
# P is causally related to q if and only if p or any part of p and q or any part of q are linked by a chain of events where each event pair is one of direct activation or direct inhibition. p may be upstream, downstream, part of or a container of q. [RO]
    
depends_on = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002502")
# Being determined, based or contingent on something. [Allotrope]
    
towards = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002503")
# Q towards e2 if and only if q is a relational quality such that q inheres-in some e, and e != e2 and q is dependent on e2 [RO]
    
has_intermediate = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002505")
# P has intermediate c if and only if p has parts p1, p2 and p1 has output c, and p2 has input c [RO]
    
determined_by__system_to_material_entity = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002507")
# S determined by f if and only if s is a type of system, and f is a material entity that is part of s, such that f exerts a strong causal influence on the functioning of s, and the removal of f would cause the collapse of s. [RO]
    
determined_by_part_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002509")
# S &apos;determined by part of&apos; w if and only if there exists some f such that (1) s &apos;determined by&apos; f and (2) f part_of w, or f=w. [RO]
    
sequentially_related_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002514")
# A relation that holds between two entities that have the property of being sequences or having sequences. [RO]
    
sequentially_adjacent_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002515")
# x is sequentially adjacent to y if and only if x and y do not overlap and if there are no base units intervening between x and y [RO]
    
has_start_sequence = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002516")
# x has start sequence y if the start of x is identical to the start of y, and x has y as a subsequence [RO]
    
is_start_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002517")
# inverse of has start sequence [RO]
    
has_end_sequence = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002518")
# x has end sequence y if the end of x is identical to the end of y, and x has y as a subsequence [RO]
    
is_end_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002519")
# inverse of has end sequence [RO]
    
bounds_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002522")
# x bounds the sequence of y if and only if the upstream-most part of x is upstream of or coincident with the upstream-most part of y, and the downstream-most part of x is downstream of or coincident with the downstream-most part of y [RO]
    
is_bound_by_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002523")
# inverse of bounds sequence of [RO]
    
has_subsequence = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002524")
# x has subsequence y if and only if all of the sequence parts of x are sequence parts of y [RO]
    
is_subsequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002525")
# inverse of has subsequence [RO]
    
overlaps_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002526")
# x overlaps the sequence of x if and only if x has a subsequence z and z is a subsequence of y. [RO]
    
does_not_overlap_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002527")
# x does not overlaps the sequence of x if and only if there is no z such that x has a subsequence z and z is a subsequence of y. [RO]
    
is_upstream_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002528")
# inverse of downstream sequence of [RO]
    
is_downstream_of_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002529")
# x is downstream of the sequence of y if and only if either (1) x and y have sequence units, and all units of x are downstream of all units of y, or (2) x and y are sequence units, and x is either immediately downstream of y, or transitively downstream of y. [RO]
    
is_immediately_downstream_of_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002530")
# x is immediately downstream of the sequence of y if and only if either (1) x and y have sequence units, and all units of x are downstream of all units of y, and x is sequentially adjacent to y, or (2) x and y are sequence units, in which case the immediately downstream relation is primitive and defined by context: for DNA bases, y would be adjacent and 5&apos; to y [RO]
    
is_immediately_upstream_sequence_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002531")
# inverse of immediately downstream of [RO]
    
causally_influences__material_entity_to_material_entity = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002566")
# Holds between materal entities a and b if the activity of a is causally upstream of the activity of b, or causally upstream of a an activity that modifies b [RO]
    
conduit_for = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002570")
# X is a conduit for y if and only if y overlaps through the lumen_of of x, and y has parts on either side of the lumen of x. [RO]
    
has_part_structure_that_is_capable_of = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002584")
# S &apos;has part structure that is capable of&apos; p if and only if there exists some part x such that s &apos;has part&apos; x and x &apos;capable of&apos; p [RO]
    
causal_relation_between_material_entity_and_a_process = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002595")
# A relationship that holds between a material entity and a process in which causality is involved, with either the material entity or some part of the material entity exerting some influence over the process, or the process influencing some aspect of the material entity. [RO]
    
is_marker_for = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002607")
# C is marker for d if and only if the presence or occurrence of d is correlated with the presence of occurrence of c, and the observation of c is used to infer the presence or occurrence of d. Note that this does not imply that c and d are in a direct causal relationship, as it may be the case that there is a third entity e that stands in a direct causal relationship with c and d. [RO]
    
related_via_dependence_to = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002609")
# A relationship that holds between two entities, where the relationship holds based on the presence or absence of statistical dependence relationship. The entities may be statistical variables, or they may be other kinds of entities such as diseases, chemical entities or processes. [RO]
    
correlated_with = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0002610")
# A relationship that holds between two entities, where the entities exhibit a statistical dependence relationship. The entities may be statistical variables, or they may be other kinds of entities such as diseases, chemical entities or processes. [RO]
    
produces = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0003000")
# a produces b if some process that occurs_in a has_output b, where a and b are material entities. [RO]
    
produced_by = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0003001")
# inverse of produces
    
causes_or_contributes_to_condition = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0003302")
# A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure) and a condition (a phenotype or disease), where the entity has some causal or contributing role that influences the condition. [RO]
    
causes_condition = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0003303")
# A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure) and a condition (a phenotype or disease), where the entity has some causal role for the condition. [RO]
    
contributes_to_condition = onto.search_one(iri="http://purl.obolibrary.org/obo/RO_0003304")
# A relationship between an entity (e.g. a genotype, genetic variation, chemical, or environmental exposure) and a condition (a phenotype or disease), where the entity has some contributing role that influences the condition. [RO]
    