import inspect
import json
import os.path

from owlready2 import Thing, ObjectProperty, DataProperty, AnnotationProperty, Ontology
from owlready2 import get_ontology, onto_path

from ontosynthesis.base import get_property, afo

"""
error in loading may come from invalid import path
copy `external_ontologies/afo_inferred_by_qai/owx_dump/afo.owx` to the current folder as `afo.owl`
then add `onto_path.append("./")`
"""


def get_cyto_node(individual: Thing, prop_dict_annotation, prop_dict_data):
    pref_label = individual.label[0]

    data_properties = {k.python_name: v for k, v in prop_dict_data.items()}
    data_properties_as_string = ",".join([str(v) for k, v in data_properties.items()])

    if len(data_properties_as_string) > 0:
        cyto_node_label = data_properties_as_string
    else:
        cyto_node_label = pref_label

    if afo.Process in individual.INDIRECT_is_a:
        cyto_class = "process"
    elif afo.Material in individual.INDIRECT_is_a:
        cyto_class = "material"
    else:
        cyto_class = ""

    cyto_node = dict(
        group="nodes",
        data={
            "id": individual.iri,
            "label": pref_label,
            "cyto_node_label": cyto_node_label,
            "annotation_properties": {k.python_name: v for k, v in prop_dict_annotation.items()},
            "data_properties": data_properties,
            "individual_class": [c.name for c in individual.is_a],
            "individual_class_label": [c.label[0] for c in individual.is_a],
        },
        selected=False,
        selectable=True,
        grabbable=True,
        locked=False,
        classes=cyto_class,
    )
    return cyto_node, individual.iri


def get_cyto_edge(individual, prop_obj, obj):
    relation_id = f"{individual.iri} {prop_obj.iri} {obj.iri}"
    cyto_edge = dict(
        group="edges",
        data={
            "id": relation_id,
            "source": individual.iri,
            "target": obj.iri,
            "predicate": prop_obj.iri,
            "predicate_python_name": prop_obj.python_name,
            # "edge_color": get_edge_color(op.predicate),
        }
    )
    return cyto_edge, relation_id


# TODO figure out the difference between owlready search and SPARQL, use owlready for now

def onto_to_cyto(ontology: Ontology, direct=False):
    with ontology:
        return _onto_to_cyto(ontology, direct=direct)


def _onto_to_cyto(ontology: Ontology, direct=False):
    individuals = [*ontology.individuals()]

    cyto_node_ids = []
    cyto_edge_ids = []

    cyto_nodes = []
    cyto_edges = []

    for individual in individuals:
        # node_label = individual.label[0]
        # alt_labels = individual.label[1:]

        if direct:
            props = individual.get_properties()
        else:
            props = individual.INDIRECT_get_properties()

        prop_dict_annotation = dict()
        prop_dict_data = dict()

        for prop in props:
            objs = get_property(individual, prop, indirect=False)

            if issubclass(prop, AnnotationProperty):
                prop_dict_annotation[prop] = objs
            elif issubclass(prop, DataProperty):
                prop_dict_data[prop] = objs
            elif issubclass(prop, ObjectProperty):
                # TODO skip empty objs for now
                if len(objs) == 0:
                    continue
                assert all(not inspect.isclass(o) for o in objs)
                for obj in objs:
                    cyto_edge, cyto_edge_id = get_cyto_edge(individual, prop, obj)
                    if cyto_edge_id not in cyto_edge_ids:
                        cyto_edges.append(cyto_edge)
                        cyto_edge_ids.append(cyto_edge_id)
            else:
                raise TypeError

        cyto_node, cyto_node_id = get_cyto_node(individual, prop_dict_annotation, prop_dict_data)
        if cyto_node_id not in cyto_node_ids:
            cyto_nodes.append(cyto_node)
    return cyto_nodes, cyto_edges


def export_cyto(owl_filename):
    onto = get_ontology(owl_filename).load()
    nodes, edges = onto_to_cyto(onto, direct=False)
    data = {
        "cyto_nodes": nodes,
        "cyto_edges": edges,
        "ord__reaction_id": "ord-b8941b0391c44f3a9113f97f00ae3490",
    }
    out = os.path.basename(owl_filename)[:-4] + ".json"
    with open(out, "w") as f:
        json.dump(data, f)


if __name__ == '__main__':
    onto_path.append("./")
    export_cyto("test_reaction_with_infer.owl")
    export_cyto("test_reaction_without_infer.owl")
