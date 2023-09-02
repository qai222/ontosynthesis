1. Dump `afo` to `owx_dump` using `protege -> collect ontologies`, choose `OWL/XML`.
2. Use `localize.sh` to edit import paths in the dumped `ttl` files.
   1. the dumped files are actually `OWL/XML` but suffixes are `ttl`, likely b/c `afo` was opened as a `ttl`
3. Use `to_owlready2.py` to export ontology classes as `owlready2` python classes. 
By default, it makes a dir named `ontologies` and the classes are dumped in `__init__.py`.
Move it to `ontosynthesis/resource/afo.py`