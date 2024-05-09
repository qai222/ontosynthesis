import random
from collections import defaultdict

import matplotlib
import networkx as nx
import rdflib.term
from owlready2 import get_ontology
from rdflib import Graph

random.seed(42)
_color_list = list(matplotlib.colors.cnames.values())
random.shuffle(_color_list)


def rdf_to_cyto_elements(rdf_file_path, ontology_file_path) -> tuple[list[dict], list[dict]]:
    onto = get_ontology(ontology_file_path).load()
    abox = Graph()
    abox.parse(rdf_file_path)

    cyto_nodes = dict()
    cyto_edges = dict()
    node_data_props = defaultdict(dict)  # iri --> data properties
    node_class_dict = defaultdict(list)

    nxg = nx.MultiDiGraph()
    # record those cannot be found in tbox
    hallucination_classes = set()
    hallucination_properties = set()
    for s, p, o in abox.triples((None, None, None)):
        assert isinstance(s, rdflib.term.URIRef)
        assert isinstance(p, rdflib.term.URIRef)
        if isinstance(o, rdflib.term.Literal):
            node_data_props[str(s)][str(p)] = str(o)  # assuming functional data prop
        elif str(p) == "http://www.w3.org/1999/02/22-rdf-syntax-ns#type":  # TODO this seems too ad-hoc
            node_class_dict[str(s)].append(str(o))
            if not onto.search_one(iri=str(o)):
                hallucination_classes.add(str(o))
        else:
            nxg.add_edge(str(s), str(o), p=str(p))
            if not onto.search_one(iri=str(p)):
                hallucination_properties.add(str(p))

    nx.set_node_attributes(nxg, node_data_props)

    cyto_nodes = []
    for n, d in nxg.nodes(data=True):
        data = {
            "id": n,
            "label": n.replace(onto.base_iri, onto.name + ":"),
        }
        data.update(d)
        h_class = ""
        if set(node_class_dict[n]).intersection(hallucination_classes):
            h_class += "hallucination"
        cyto_node = dict(
            group="nodes",
            data=data,
            selected=False,
            selectable=True,
            grabbable=True,
            locked=False,
            classes=" ".join([str(hash(c)) for c in node_class_dict[n]]) + " " + h_class,  # TODO magic for now
        )
        cyto_nodes.append(cyto_node)

    cyto_edges = []
    for u, v, k, d in nxg.edges(data=True, keys=True):
        h_class = ""
        if d['p'] in (hallucination_properties):
            h_class += "hallucination"
        cyto_edge = dict(
            group="edges",
            data={
                "id": f"{u} {v} {k} {d['p']}",
                "source": u,
                "target": v,
                "predicate": d['p'],
                "predicate_name": d['p'].replace(onto.base_iri, onto.name + ":"),
            },
            classes=str(hash(d['p'])) + " " + h_class,
        )
        cyto_edges.append(cyto_edge)
    return cyto_nodes, cyto_edges


def get_style_sheet(cyto_nodes):
    node_classes = set()
    for cn in cyto_nodes:
        for c in cn['classes'].split():
            node_classes.add(c)

    ss = [
        {
            'selector': 'edge',
            'style': {
                'curve-style': 'unbundled-bezier',
                'taxi-direction': 'vertical',
                'label': 'data(predicate_name)',
                'target-arrow-shape': 'triangle',
                "opacity": "0.5",
                "line-color": "#bbb",
                # "width": "mapData(weight, 0, 1, 1, 8)",
                "overlay-padding": "3px"
            }
        },
        {
            "selector": "core",
            "style": {
                "selection-box-color": "#AAD8FF",
                "selection-box-border-color": "#8BB0D0",
                "selection-box-opacity": "0.5"
            }
        },
        {
            'selector': 'node',
            'style': {
                'content': 'data(label)',
                'border-width': 2,
                'text-valign': 'center',
                'padding': "15px",
                # 'width': 'label',
                # 'height': '22px',
                'font-size': '18px',
                "text-halign": "center",
                "background-color": "#555",
                # "text-outline-color": "#555",
                # "text-outline-width": "2px",
                # "color": "#fff",
                "overlay-padding": "6px",
                "z-index": "10"
            }
        },
        {
            'selector': ':selected',
            'style': {
                'z-index': 1000,
                'background-color': 'SteelBlue',
                'line-color': 'SteelBlue',
            }
        },
        {
            "selector": "node:selected",
            "style": {
                "border-width": "6px",
                "border-color": "SteelBlue",
                "border-opacity": "1",
                # "background-color": "#77828C",
                "background-color": "red",
                "text-outline-color": "#77828C"
            }
        },
    ]
    for i, node_class in enumerate(node_classes):
        color = _color_list[i % len(_color_list)]
        ss.append(
            {
                "selector": f".{node_class}",
                "style": {
                    "background-color": color,
                    # "color": color,
                }
                # "color": "#fff",
            }
        )
    ss.append(
        {
            'selector': '.hallucination',
            'style': {
                'text-color': 'red',
                'color': 'red',
            }
        }
    )
    return ss


def rdf_to_cyto(abox_path, tbox_path):
    cyto_nodes, cyto_edges = rdf_to_cyto_elements(abox_path, tbox_path)
    cyto_data = {
        "nodes": cyto_nodes,
        "edges": cyto_edges,
        "style": get_style_sheet(cyto_nodes)
    }
    return cyto_data
