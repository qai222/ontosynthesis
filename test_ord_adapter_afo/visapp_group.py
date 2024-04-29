import json

import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import networkx as nx
from dash import Dash, html, Input, Output, State, Patch

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

# load world
with open("test_reaction_with_infer.json", "r") as f:
    DATA = json.load(f)

CYTO_NODES = DATA['cyto_nodes']
CYTO_EDGES = DATA['cyto_edges']
CYTO_NODES_DICT = {n['data']['id']: n for n in CYTO_NODES}
CYTO_EDGES_DICT = {n['data']['id']: n for n in CYTO_EDGES}
ORD__REACTION_ID = DATA['ord__reaction_id']


def get_cyto_edges_btw_uv(uid, vid):
    return [e for e in CYTO_EDGES if e['data']['source'] == uid and e['data']['target'] == vid]


NXG = nx.MultiDiGraph()
for n in CYTO_EDGES:
    NXG.add_edge(n['data']['source'], n['data']['target'], n['data']['predicate_python_name'])

# import urllib
# with urllib.request.urlopen('https://js.cytoscape.org/demos/colajs-graph/cy-style.json') as url:
#     STYLE_SHEET = json.loads(url.read().decode())


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
            'content': 'data(cyto_node_label)',
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
        'selector': ".process",
        'style': {
            'shape': 'rectangle',
            'background-color': 'white',
        }
    },
    {
        'selector': ".material",
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
            'line-color': 'SteelBlue',
        }
    },
    {
        "selector": "node:selected",
        "style": {
            "border-width": "6px",
            "border-color": "#AAD8FF",
            "border-opacity": "0.5",
            "background-color": "#77828C",
            "text-outline-color": "#77828C"
        }
    },
]

app = Dash(
    name=__name__,
    title="Plan Visualizer",
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

cyto.load_extra_layouts()


def get_individual_class_checklist():
    individual_classes = []
    for n in CYTO_NODES:
        individual_classes += n['data']['individual_class_label']
    individual_classes = sorted(set(individual_classes))
    options = []
    for c in individual_classes:
        opt = {"label": c, "value": c, }
        options.append(opt)

    button_group = html.Div(
        [
            dbc.Checklist(
                id="individual_class_checklist",
                className="btn-group flex-wrap",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary mb-2",
                labelCheckedClassName="active",
                options=options,
                value=[o['value'] for o in options],
            ),
        ],
        className="radio-group",
    )
    return button_group


def get_predicate_checklist():
    predicate_names = []
    for n in CYTO_EDGES:
        predicate_names.append(n['data']['predicate_python_name'])
    predicate_names = sorted(set(predicate_names))
    options = []
    for c in predicate_names:
        opt = {"label": c, "value": c, }
        options.append(opt)

    button_group = html.Div(
        [
            dbc.Checklist(
                id="predicate_name_checklist",
                className="btn-group flex-wrap",
                inputClassName="btn-check",
                labelClassName="btn btn-outline-primary mb-2",
                labelCheckedClassName="active",
                options=options,
                value=[o['value'] for o in options if "has" in o['value']] + ['preceded_by', 'quantified_by'],
            ),
        ],
        className="radio-group",
    )
    return button_group


@app.callback(
    Output('CYTO', 'stylesheet'),
    Input('CYTO', 'selectedNodeData')
)
def update_stylesheet(node_data):
    if node_data:
        selected_node_ids = [nd['id'] for nd in node_data]
        new_stylesheet = Patch()
        for selected_node_id in selected_node_ids:
            new_stylesheet.append({
                'selector': f'edge[target="{selected_node_id}"]',
                'style': {'line-color': 'red', 'color': 'red'}
            })
            new_stylesheet.append({
                'selector': f'edge[source="{selected_node_id}"]',
                'style': {'line-color': 'green', 'color': 'green'}
            })
        return new_stylesheet
    else:
        return STYLE_SHEET


@app.callback(
    Output('CYTO', 'elements'),
    Input("individual_class_checklist", "value"),
    Input("predicate_name_checklist", "value"),
    State('CYTO', 'elements'),
)
def generate_elements(
        selected_individual_classes,
        selected_predicate_names,
        elements
):
    allowed_nodes = []
    allowed_edges = []

    for node in CYTO_NODES:
        if set(node['data']['individual_class_label']).intersection(set(selected_individual_classes)):
            allowed_nodes.append(node)

    allowed_node_iris = [n['data']['id'] for n in allowed_nodes]
    for edge in CYTO_EDGES:
        if edge['data']['source'] not in allowed_node_iris or edge['data']['target'] not in allowed_node_iris:
            continue
        if edge['data']['predicate_python_name'] not in selected_predicate_names:
            continue
        allowed_edges.append(edge)

    nodes_in_edges = [e['data']['source'] for e in allowed_edges] + [e['data']['target'] for e in allowed_edges]
    allowed_nodes = [n for n in allowed_nodes if n['data']['id'] in nodes_in_edges]  # remove orphans

    return allowed_edges + allowed_nodes


app.layout = html.Div(
    [
        dbc.Row(
            [
                html.Div(
                    id="CYTO_DIV",
                    children=
                    [
                        html.H5(f"ONTOSYNTHESIS: {ORD__REACTION_ID}"),
                        html.Hr(),
                        cyto.Cytoscape(
                            id='CYTO',
                            layout={
                                'name': 'klay',
                                'nodeDimensionsIncludeLabels': True,
                                'animate': True,
                                'animationDuration': 1000,
                                'align': 'UL',
                            },
                            style={
                                'width': '100%',
                                'height': 'calc(100vh - 100px)'
                            },
                            className="border-primary border",
                            elements=CYTO_EDGES + CYTO_NODES,
                            stylesheet=STYLE_SHEET,
                            responsive=True,
                        )
                    ],
                    className="col-lg-8 px-4",
                    # style={'height': 'calc(100vh - 100px)'},  # minus header bar height
                    style={'height': '100%'},  # minus header bar height
                ),
                html.Div(
                    [
                        html.H5("Classes", className="text-center mt-3"),
                        get_individual_class_checklist(),
                        html.Hr(),
                        html.H5("Predicates", className="text-center mt-3"),
                        get_predicate_checklist(),
                        html.Hr(),
                    ],
                    className="col-lg-4 px-2",
                ),
            ]
        )

    ], style={"width": "100vw"}
)

if __name__ == '__main__':
    app.run(debug=False)
