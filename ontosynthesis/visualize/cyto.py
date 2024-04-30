import os.path

from owlready2 import Thing, ObjectProperty, Ontology, ThingClass, ObjectPropertyClass
from owlready2 import get_ontology
from pandas._typing import FilePath
from pydantic import BaseModel
from dash import html
import dash_bootstrap_components as dbc
from collections import Counter
from ontosynthesis.base import get_property, get_data

_definition_iri = "http://www.w3.org/2004/02/skos/core#definition"

def get_world_summary(onto: Ontology, cyto_nodes: list[dict]) -> dbc.Table:
    num_of_classes = len(list(onto.classes()))
    num_of_object_properties = len(list(onto.object_properties()))
    num_of_individuals = len(list(onto.individuals()))

    cyto_classes = [node['classes'] for node in cyto_nodes]  # TODO assuming one node has only one cyto class
    unique_cyto_classes = sorted(set(cyto_classes))

    row1 =  html.Tr([html.Td("# of defined classes"), html.Td(f"{num_of_classes}")])
    row2 =  html.Tr([html.Td("# of defined object properties"), html.Td(f"{num_of_object_properties}")])
    row3 =  html.Tr([html.Td("# of asserted individuals"), html.Td(f"{num_of_individuals}")])
    rows = [row1, row2, row3]
    c_counter = Counter(cyto_classes)
    for c in unique_cyto_classes:
        row = html.Tr([html.Td(c), html.Td(f"{c_counter[c]}")])
        rows.append(row)
    table_body = [html.Tbody(rows)]
    table = dbc.Table(table_body, bordered=True,
                      hover=True,
                      responsive=True,
                      striped=True,
                      color="light"
                      )
    return table


class ClassInfo(BaseModel):
    iri: str
    ancestors: list[str]
    name: str
    definition: str

    @property
    def cyto_class(self) -> str:
        return self.name.replace(" ", "_")


class ObjectPropertyInfo(BaseModel):
    iri: str
    ancestors: list[str]
    name: str
    # domain: list[ClassInfo]
    # range: list[ClassInfo]


def load_owl(owl_file: FilePath) -> Ontology:
    # onto_path.append(os.path.dirname(os.path.abspath(owl_file)))
    onto = get_ontology(os.path.abspath(owl_file)).load()
    return onto


def get_class_info_one(cls: ThingClass, onto: Ontology):
    definition_prop = onto.search_one(iri=_definition_iri)
    if definition_prop is None:
        definition = ""
    else:
        try:
            definition = get_property(cls, definition_prop)[0]
        except IndexError:
            definition = ""
    return ClassInfo(
        iri=cls.iri,
        ancestors=[a.iri for a in cls.ancestors(include_self=False)],
        name=cls.label[0].__str__(),
        definition=definition
    )


def get_class_info(onto: Ontology) -> dict[str, ClassInfo]:
    map = dict()
    for cls in onto.classes():
        cinfo = get_class_info_one(cls, onto)
        map[cls.iri] = cinfo
    return map


def get_prop_info(onto: Ontology) -> dict[str, ObjectPropertyInfo]:
    map = dict()
    for prop in onto.object_properties():
        prop: ObjectPropertyClass
        map[prop.iri] = ObjectPropertyInfo(
            iri=prop.iri,
            ancestors=[a.iri for a in prop.ancestors(include_self=False)],
            name=prop.label[0].__str__(),
        )
    return map


def export_cyto_edge(sub: Thing, prop: ObjectProperty, obj: Thing, prop_info: dict[str, ObjectPropertyInfo]):
    relation_id = f"{sub.iri} {prop.iri} {obj.iri}"
    prop_name = prop_info[prop.iri].name
    cyto_edge = dict(
        group="edges",
        data={
            "id": relation_id,
            "source": sub.iri,
            "target": obj.iri,
            "predicate": prop.iri,
            "predicate_name": prop_name,
            # "edge_color": get_edge_color(op.predicate),
        },
        classes=prop_name.replace(" ", "_"),
    )
    return cyto_edge, relation_id


def export_cyto_node(ind: Thing, class_info: dict[str, ClassInfo], allowed_cyto_classes: list[str]):

    ind_classes = [c for c in ind.INDIRECT_is_a if isinstance(c, ThingClass)]
    this_class_info = [class_info[c.iri] for c in ind_classes if c.iri in class_info]
    this_class_info = [cinfo for cinfo in this_class_info if cinfo.cyto_class in allowed_cyto_classes][0]
    data = get_data(ind)
    cyto_node = dict(
        group="nodes",
        data={
            "id": ind.iri,
            "label": ind.name,
            "cyto_node_label": this_class_info.name,
            "individual_data": data,
            "individual_class": [class_info[c.iri].name for c in ind.is_a],
        },
        selected=False,
        selectable=True,
        grabbable=True,
        locked=False,
        classes=this_class_info.cyto_class,
    )
    return cyto_node, ind.iri


def export_cyto_data(onto: Ontology, direct: bool = True):
    class_info = get_class_info(onto)
    object_prop_info = get_prop_info(onto)

    root_classes = [v for v in class_info.values() if len(v.ancestors) == 1]
    cyto_node_classes = [c.name.replace(" ", "_") for c in root_classes]

    edge_ids = set()
    cyto_nodes = []
    cyto_edges = []
    for ind in onto.individuals():
        cyto_node, cyto_node_id = export_cyto_node(ind, class_info, cyto_node_classes)

        cyto_nodes.append(cyto_node)

        if direct:
            props = ind.get_properties()
        else:
            props = ind.INDIRECT_get_properties()
        props = [p for p in props if p.iri in object_prop_info]
        for prop in props:
            objs = get_property(ind, prop, indirect=False)
            if len(objs) == 0:
                # TODO skip empty objs for now
                continue
            for obj in objs:
                cyto_edge, cyto_edge_id = export_cyto_edge(ind, prop, obj, object_prop_info)
                if cyto_edge_id not in edge_ids:
                    cyto_edges.append(cyto_edge)
                    edge_ids.add(cyto_edge_id)
    return cyto_nodes, cyto_edges, cyto_node_classes

JsonTheme = {
    "scheme": "monokai",
    "author": "wimer hazenberg (http://www.monokai.nl)",
    "base00": "#272822",
    "base01": "#383830",
    "base02": "#49483e",
    "base03": "#75715e",
    "base04": "#a59f85",
    "base05": "#f8f8f2",
    "base06": "#f5f4f1",
    "base07": "#f9f8f5",
    "base08": "#f92672",
    "base09": "#fd971f",
    "base0A": "#f4bf75",
    "base0B": "#a6e22e",
    "base0C": "#a1efe4",
    "base0D": "#66d9ef",
    "base0E": "#ae81ff",
    "base0F": "#cc6633",
}

STYLE_SHEET = [
    {
        'selector': 'edge',
        'style': {
            'curve-style': 'unbundled-bezier',
            'taxi-direction': 'vertical',
            'label': 'data(predicate_python_name)',
            'target-arrow-shape': 'triangle',
            "opacity": "0.5",
            "line-color": "#bbb",
            # "width": "mapData(weight, 0, 1, 1, 8)",
            "overlay-padding": "3px"
        }
    },

    {
        'selector': 'edge[edge_color]',
        'style': {
            'color': 'data(edge_color)',
            'line-color': 'data(edge_color)',
            'target-arrow-color': 'data(edge_color)'
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
            # 'content': 'data(cyto_node_label)',
            'border-width': 2,
            'text-valign': 'center',
            'padding': "15px",
            # 'width': 'label',
            # 'height': '22px',
            'font-size': '18px',
            "text-halign": "center",
            "background-color": "#555",
            "text-outline-color": "#555",
            "text-outline-width": "2px",
            "color": "#fff",
            "overlay-padding": "6px",
            "z-index": "10"
        }
    },

    {
        'selector': ".material_process .composite_material_process",
        'style': {
            'shape': 'rectangle',
            'background-color': 'white',
        }
    },

    {
        'selector': ".functional_module",
        'style': {
            'shape': 'triangle',
            'background-color': 'white',
        }
    },

    {
        'selector': ".hardware_unit",
        'style': {
            'shape': 'triangle',
            'background-color': 'white',
        }
    },

    {
        'selector': ".is_preceded_by",
        'style': {
            "opacity": "1.0",
            "line-color": "#bbb",
            "width": "9",
        }
    },

    {
        'selector': ".has_material_input",
        'style': {
            "opacity": "1.0",
            "line-color": "blue",
            "width": "3",
        }
    },
    {
        'selector': ".has_separation_input",
        'style': {
            "opacity": "1.0",
            "line-color": "blue",
            "width": "3",
        }
    },
    {
        'selector': ".has_material_output",
        'style': {
            "opacity": "1.0",
            "line-color": "green",
            "width": "3",
        }
    },
    {
        'selector': ".has_separation_output",
        'style': {
            "opacity": "1.0",
            "line-color": "green",
            "width": "3",
        }
    },

    {
        'selector': ".portion_of_material",
        'style': {
            'shape': 'circle',
            'background-color': 'white',
        }
    },

    {
        'selector': ':selected',
        'style': {
            'z-index': 1000,
            'background-color': 'SteelBlue',
            'line-color': 'red',
        }
    },

    {
        "selector": "node:selected",
        "style": {
            "border-width": "6px",
            "border-color": "#AAD8FF",
            "border-opacity": "0.5",
            # "background-color": "#77828C",
            "background-color": "red",
            "text-outline-color": "#77828C"
        }
    },
]
