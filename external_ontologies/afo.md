1. load `afo` from `external_ontologies/afo/AFO-2023_06/afo/voc/afo/REC/2023/06/afo.ttl`
2. - `afo_inferred_by_qai`
      - sync reasoner
      - in protege, `File` -> `Exported inferred`
      - save as `owx_dump/afo.owx` (`OWL/XML`)
      - run `sed -i "s#mailto:#mailto://#" *.owx` to correct email addresses
   - `afo`
      - dump `afo` to `owx_dump` using `protege -> gather ontologies`, choose `OWL/XML`. 
      - Use `localize.sh` to edit import paths in the dumped `ttl` files. 
        - the dumped files are actually `OWL/XML` but suffixes are `ttl`, likely b/c `afo` was opened as a `ttl`
3. Use `to_owlready2.py` to export ontology classes as `owlready2` python classes. 
By default, it makes a dir named `ontologies` and the classes are dumped in `__init__.py`.
Move it to `ontosynthesis/resource/afo.py`