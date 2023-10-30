from __future__ import annotations

from owlready2 import get_ontology, ObjectProperty, TransitiveProperty

ONTO = get_ontology("http://ontosynthesis.org/ontosynthesis.owl")

with ONTO:
    class has_part(ObjectProperty, TransitiveProperty):
        python_name = "has_part"
