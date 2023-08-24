
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
TermGranularity = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001221")
# Term granularity relates an entity to an instance of granularity that describes the level of granularity that a term belongs to. [Allotrope]
    