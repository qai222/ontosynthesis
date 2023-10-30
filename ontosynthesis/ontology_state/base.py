from __future__ import annotations

from owlready2 import get_ontology, ObjectProperty, TransitiveProperty

ONTOLOGY_STATE = get_ontology("http://ontosynthesis.org/state.owl")

with ONTOLOGY_STATE:
    class has_part(ObjectProperty, TransitiveProperty):
        python_name = "has_part"
