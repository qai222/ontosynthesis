import json

import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import networkx as nx
from dash import Dash, html, Input, Output, no_update, State

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
with open("test_reaction_without_infer.json", "r") as f:
    DATA = json.load(f)

CYTO_NODES = DATA['cyto_nodes']
CYTO_EDGES = DATA['cyto_edges']
CYTO_NODES_DICT = {n['data']['id']: n for n in CYTO_NODES}


def get_cyto_edges_btw_uv(uid, vid):
    return [e for e in CYTO_EDGES if e['data']['source'] == uid and e['data']['target'] == vid]


NXG = nx.MultiDiGraph()
for n in CYTO_EDGES:
    NXG.add_edge(n['data']['source'], n['data']['target'], n['data']['predicate_python_name'])

STYLE_SHEET = [
    {
        'selector': 'edge',
        'style': {
            'opacity': 1,
            'curve-style': 'unbundled-bezier',
            'taxi-direction': 'vertical',
            'label': 'data(predicate_python_name)',
            'target-arrow-shape': 'triangle'
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
        'selector': 'node',
        'style': {
            'content': 'data(label)',
            'border-width': 2,
            'text-valign': 'center',
            'padding': "10px",
            'width': 'label',
            'height': '18px',
            'font-size': '18px'
        }
    },

    # {
    #     'selector': "." + ChemicalIdentifier.__name__,
    #     'style': {
    #         'shape': 'rectangle',
    #         'background-color': 'white',
    #         'text-background-color': 'blue',
    #     }
    # },
    # {
    #     'selector': "." + Action.__name__,
    #     'style': {
    #         'shape': 'rectangle',
    #         # 'background-color': 'none',
    #         'background-color': 'white',
    #         'color': 'red',
    #     }
    # },
    {
        'selector': ':selected',
        'style': {
            'z-index': 1000,
            'background-color': 'SteelBlue',
            'line-color': 'SteelBlue',
        }
    },

]

app = Dash(
    name=__name__,
    title="Plan Visualizer",
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

cyto.load_extra_layouts()


# @app.callback(
#     Output("INFO TAB", "children"),
#     Input("CYTO", "selectedNodeData"),
#     Input("CYTO", "selectedEdgeData"),
# )
# def update_div_info(node_data, edge_data):
#     node_attrs = []
#     edge_attrs = []
#     if node_data:
#         for d in node_data:
#             node_attrs.append(d['ele_attrs'])
#     if edge_data:
#         for d in edge_data:
#             u = d['source']
#             v = d['target']
#             attrs = {
#                 "source": u,
#                 "target": v,
#                 "predicate": d['predicate'],
#             }
#             edge_attrs.append(attrs)
#     blocks = []
#     for attrs in node_attrs + edge_attrs:
#         try:
#             header = attrs['individual class']
#         except KeyError:
#             header = attrs['predicate']
#         json_block = dash_renderjson.DashRenderjson(data=attrs, max_depth=-1,
#                                                     theme=JsonTheme, invert_theme=True),
#         block = dbc.Card(
#             [
#                 dbc.CardHeader([html.B(header, className="text-primary"), ]),
#                 dbc.CardBody(json_block),
#             ],
#             className="mb-3"
#         )
#         blocks.append(block)
#     return blocks
#


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
                value=[o['value'] for o in options if "has" in o['value']],
            ),
        ],
        className="radio-group",
    )
    return button_group


@app.callback(
    Output("CYTO_DIV", "children"),
    Input("individual_class_checklist", "value"),
    Input("predicate_name_checklist", "value"),
)
def update_cyto(selected_individual_classes, selected_predicate_names, ):
    allowed_nodes = []
    allowed_edges = []

    if selected_individual_classes is None or selected_predicate_names is None:
        return no_update

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
    allowed_nodes = [n for n in allowed_nodes if n['data']['id'] in nodes_in_edges]

    cyto_main = cyto.Cytoscape(
        id='CYTO',
        layout={
            'name': 'klay',
            'nodeDimensionsIncludeLabels': True,
            # 'animate': True,
            # 'animationDuration': 1000,
            'animate': False,
            'align': 'UL',
        },
        style={
            'width': '100%',
            'height': 'calc(100vh - 100px)'
        },
        className="border-primary border",
        elements=allowed_nodes + allowed_edges,
        stylesheet=STYLE_SHEET,
    )
    return [
        html.H5("ONTOSYNTHESIS"),
        html.Hr(),
        cyto_main
    ]


@app.callback(Output('CYTO', 'elements'),
              [Input('CYTO', 'tapNodeData')],
              [State('CYTO', 'elements'), ])
def generate_elements(nodeData, elements):
    if not nodeData:
        return no_update

    # If the node has already been expanded, we don't expand it again
    if nodeData.get('expanded'):
        return elements

    # This retrieves the currently selected element, and tag it as expanded
    for element in elements:
        if nodeData['id'] == element.get('data').get('id'):
            element['data']['expanded'] = True
            break
        this_node_id = nodeData['id']

        neighbor_node_ids = NXG.neighbors(this_node_id)
        extend_nodes = [CYTO_NODES_DICT[n] for n in neighbor_node_ids]
        extend_edges = []
        for nb in neighbor_node_ids:
            extend_edges += get_cyto_edges_btw_uv(this_node_id, nb)
        elements.extend(extend_nodes)
        elements.extend(extend_edges)

    return elements


app.layout = html.Div(
    [
        dbc.Row(
            [
                html.Div(
                    id="CYTO_DIV",
                    className="col-lg-8",
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
                    className="col-lg-4",
                ),
            ]
        )

    ], style={"width": "100vw"}
)

if __name__ == '__main__':
    app.run(debug=True)
