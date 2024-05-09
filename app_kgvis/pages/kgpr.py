import glob
import os

import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import dash_renderjson
from dash import html, get_app, Input, Output
from dash import register_page

from ontosynthesis.visualize.cyto import STYLE_SHEET, load_owl, get_world_summary, export_cyto_data, JsonTheme

# page meta
PAGE_ID_HEADER = "PR__"  # id header for components in this page
PAGE_PATH = "/kgr"  # relative url
PAGE_DESCRIPTION = "KGR"  # appears in navbar
DATA_FOLDER_RELATIVE = "../../examples/*/"
WORLD_FILE_EXTENSION = ".owl"

# page setup
app = get_app()
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(THIS_DIR, DATA_FOLDER_RELATIVE)
world_files = sorted(glob.glob(f"{DATA_FOLDER}/*{WORLD_FILE_EXTENSION}"))
register_page(__name__, path=PAGE_PATH, description=PAGE_DESCRIPTION)
cyto.load_extra_layouts()

# demo world
world_file = world_files[0]
world_name = os.path.basename(world_file)
world = load_owl(world_file)
CYTO_NODES, CYTO_EDGES, CYTO_NODE_CLASSES = export_cyto_data(world, direct=True)

# page components
COMPONENT_ID_cyto = f"{PAGE_ID_HEADER}CYTO"
component_cyto = cyto.Cytoscape(
    id=COMPONENT_ID_cyto,
    layout={
        'name': 'dagre',
        'nodeDimensionsIncludeLabels': True,
        'animate': True,
        'animationDuration': 1000,
        'rankDir': 'LR',
        'align': 'UL',
    },
    style={
        'width': '100%',
        'height': '100%'
    },
    className="border-primary border",
    elements=CYTO_NODES + CYTO_EDGES,
    stylesheet=STYLE_SHEET,
    responsive=True,
)

COMPONENT_ID_world_summary = f"{PAGE_ID_HEADER}WORLD_SUMMARY"
component_world_summary = html.Div(id=COMPONENT_ID_world_summary, children=[get_world_summary(world, CYTO_NODES)])
COMPONENT_ID_selection_display = f"{PAGE_ID_HEADER}SELECTION_DISPLAY"
component_selection_display = html.Div(id=COMPONENT_ID_selection_display)
COMPONENT_ID_query = f"{PAGE_ID_HEADER}QUERY"
component_query = html.Div(id=COMPONENT_ID_query)
COMPONENT_ID_filter = f"{PAGE_ID_HEADER}FILTER"
component_filter = html.Div(id=COMPONENT_ID_filter)

# page layout
layout = html.Div(
    [
        dbc.Row(
            [
                html.Div(
                    [
                        html.H5(f"WORLD: {world_name}", className="text-center mt-3"),
                        component_world_summary,
                        component_selection_display
                    ],
                    className="col-lg-4 px-2 overflow-auto",
                    style={'height': 'calc(100vh - 100px)'},  # minus header bar height
                ),
                html.Div(
                    id=f"{PAGE_ID_HEADER}CYTO_DIV",
                    children=[component_cyto],
                    className="col-lg-8 px-2",
                    style={'height': 'calc(100vh - 100px)'},  # minus header bar height
                ),
                # html.Div(
                #     [
                #         html.H5("SPARQL Query", className="text-center mt-3"),
                #         component_selection_display,
                #     ],
                #     className="col-lg-3 px-2",
                # ),
            ]
        )

    ], style={"width": "calc(100vw - 100px)"}
)


@app.callback(Output(COMPONENT_ID_selection_display, 'children'),
              Input(COMPONENT_ID_cyto, 'selectedNodeData'),
              Input(COMPONENT_ID_cyto, 'selectedEdgeData'),
              )
def display_selected(node_data_list, edge_data_list):
    if not node_data_list:
        node_data_list = []
    if not edge_data_list:
        edge_data_list = []
    data_list = node_data_list + edge_data_list
    if not data_list:
        return []
    data = data_list[-1]
    if data is None:
        return []
    children = [
        html.Hr(),
        html.H5("Individual Details", className="text-center mt-3"),
        dash_renderjson.DashRenderjson(data=data, max_depth=-1, theme=JsonTheme, invert_theme=True),
    ]
    return children
