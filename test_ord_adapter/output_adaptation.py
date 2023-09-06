from __future__ import annotations

from owlready2 import sync_reasoner_hermit

from ontosynthesis.base import ONTO
from ontosynthesis.ord_adapter import adapt_reaction, Reaction

with open("../test_reaction/test_reaction.json", "r") as f:
    test_reaction = Reaction().from_json(f.read())

process = adapt_reaction(test_reaction)

ONTO.save("test_reaction_without_infer.owl", format="rdfxml")
with ONTO:
    sync_reasoner_hermit(infer_property_values=True)
    # TODO close world lead to `OwlReadyInconsistentOntologyError`
    # TODO owl:sameAs is not inferred here, while it can be inferred in protege, exportation does not include them,
    #  see https://github.com/protegeproject/protege/issues/3
    # increase mem in src if oom
ONTO.save("test_reaction_with_infer.owl", format="rdfxml")
