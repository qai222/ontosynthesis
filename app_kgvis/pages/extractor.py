import os

import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import dash_renderjson
from dash import html, get_app, Input, Output, no_update, State
from dash import register_page, dcc

from app_extractor.data.data_dump import METER
from app_extractor.extract_openai import extract_openai
from app_extractor.rdf_to_cyto import rdf_to_cyto
from ontosynthesis.visualize.cyto import JsonTheme

# page meta
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
EXTRACTOR_CACHE_FOLDER = os.path.join(THIS_DIR, "extractor_cache")
PAGE_ID_HEADER = "EXTRACTOR__"  # id header for components in this page
PAGE_PATH = "/extractor"  # relative url
PAGE_DESCRIPTION = "Extractor"  # appears in navbar
DATA_SAMPLE_JSON = "../../app_extractor/data/data_hackathon.json"
DATA_SAMPLE_JSON = os.path.join(THIS_DIR, DATA_SAMPLE_JSON)
AVAILABLE_ONTOLOGIES = [
    "OntoReaction",
    # "SOO"
]
ONTOLOGY_FILE_PATHS = {
    "OntoReaction": os.path.join(THIS_DIR, "../../app_extractor/OntoReaction.owl"),
    # "SOO": os.path.join(THIS_DIR, "../../app_extractor/soo.owl")
}
# TODO finalize the ontologies we are acutally going to use

# page setup
app = get_app()
register_page(__name__, path=PAGE_PATH, description=PAGE_DESCRIPTION)
cyto.load_extra_layouts()
from app_extractor.data.data_dump import UnstructuredReactionDescription
from ontosynthesis.utils import json_load

DATA_SAMPLES = json_load(DATA_SAMPLE_JSON)
DATA_SAMPLES = [UnstructuredReactionDescription(**d) for d in DATA_SAMPLES]
TEXT_TO_SAMPLE_ID = {d.text.strip(): d.identifier for d in DATA_SAMPLES}
DATA_SAMPLES = {d.identifier: d for d in DATA_SAMPLES}

# page components
#### first column
COMPONENT_ID_ontology_selector = f"{PAGE_ID_HEADER}ONTOLOGY_SELECTOR"
component_ontology_selector = dbc.InputGroup(
    [
        dbc.InputGroupText("Target Ontology"),
        dbc.Select(
            options=AVAILABLE_ONTOLOGIES,
            value=AVAILABLE_ONTOLOGIES[0],
            id=COMPONENT_ID_ontology_selector,
        ),
    ]
)

COMPONENT_ID_apikey_input = f"{PAGE_ID_HEADER}APIKEY_INPUT"
component_apikey_input = dbc.InputGroup(
    [
        dbc.InputGroupText("API Key"),
        dbc.Input(id=COMPONENT_ID_apikey_input, type="password"),
    ], className="mt-2"
)
COMPONENT_ID_sample_text_selector = f"{PAGE_ID_HEADER}SAMPLE_TEXT_SELECTOR"
component_sample_text_selector = dcc.Dropdown(
    options=["Select a sample or start typing..."] + sorted(DATA_SAMPLES.keys()),
    value="Select a sample or start typing...",
    id=COMPONENT_ID_sample_text_selector,
)
COMPONENT_ID_sample_text_box = f"{PAGE_ID_HEADER}SAMPLE_TEXT_BOX"
component_sample_text_box = dbc.Textarea(
    id=COMPONENT_ID_sample_text_box,
    value="",
    placeholder="Select a sample or start typing...",
    className="mt-2 h-50",
)
COMPONENT_ID_sample_text_tags = f"{PAGE_ID_HEADER}SAMPLE_TEXT_TAGS"
component_sample_text_tags = html.Div(id=COMPONENT_ID_sample_text_tags)

COMPONENT_ID_extract_button = f"{PAGE_ID_HEADER}EXTRACT_BUTTON"

FIRST_COLUMN = html.Div(
    [
        html.H5(f"Extraction Input", className="text-center mt-3"),
        component_ontology_selector,
        component_apikey_input,
        html.H5(f"Unstructured Text", className="text-center mt-3"),
        component_sample_text_selector,
        component_sample_text_box,
        html.Div(
            children=[dbc.Button("Extract", id=COMPONENT_ID_extract_button, className="mt-3")],
            className="d-grid gap-2"
        ),
        component_sample_text_tags,
    ],
    className="col-3 px-2 overflow-auto",
    style={'height': 'calc(100vh - 100px)'},  # minus header bar height
)

#### second column
COMPONENT_ID_cyto = f"{PAGE_ID_HEADER}CYTO"
component_cyto = cyto.Cytoscape(
    id=COMPONENT_ID_cyto,
    layout={
        # 'name': 'dagre',
        'name': 'cose',
        'nodeDimensionsIncludeLabels': True,
        'animate': False,
        'animationDuration': 1000,
        'rankDir': 'LR',
        'align': 'UL',
    },
    style={
        'width': '100%',
        'height': '100%'
    },
    responsive=True,
)
COMPONENT_ID_cyto_selection_display = f"{PAGE_ID_HEADER}CYTO_SELECTION_DISPLAY"
component_cyto_selection_display = html.Div(id=COMPONENT_ID_cyto_selection_display, className="overflow-auto")

SECOND_COLUMN = html.Div(
    [
        html.H5(f"Extracted KG", className="text-center mt-3"),
        html.Div(
            [
                html.Div(component_cyto, className="h-75 border border-success"),
                html.Div(component_cyto_selection_display,
                         className="h-25 overflow-auto border border-primary mt-3 px-2"),
            ], style={"height": "calc(100vh - 200px)"}
        )
    ],
    className="col-4 px-2 overflow-auto",
    style={'height': 'calc(100vh - 100px)'},  # minus header bar height
)

#### third column
COMPONENT_ID_output_box = f"{PAGE_ID_HEADER}OUTPUT_BOX"
component_output_box = html.Div(
    id=COMPONENT_ID_output_box,
    className="mt-2 border border-secondary overflow-auto",
    style={"height": "calc(100vh - 184px)"},
)

THIRD_COLUMN = html.Div(
    [
        html.H5(f"Extracted RDF", className="text-center mt-3"),
        component_output_box,
    ],
    # className="col-lg-4 px-2 overflow-auto border border-primary",
    className="col-5 px-2 overflow-auto",
    style={'height': 'calc(100vh - 100px)'},  # minus header bar height
)

# page layout
layout = html.Div(
    [
        dbc.Row(
            [
                FIRST_COLUMN,
                SECOND_COLUMN,
                THIRD_COLUMN,
            ],
            # style={"width": "100%", "height": "100%"}
        )
    ],
    # className="container",
    style={
        "width": "calc(100vw - 100px)",
    }
)


# util functions
def extract_call(
        unstructured_data: UnstructuredReactionDescription,
        api_key: str, ontology_name="OntoReaction") -> tuple[str, str]:
    cached_rdf = f"{unstructured_data.identifier}--{ontology_name}.rdf"
    cached_rdf = os.path.join(EXTRACTOR_CACHE_FOLDER, cached_rdf)
    # TODO this is cache by identifier, better hook up to a database
    if os.path.isfile(cached_rdf) and os.path.getsize(cached_rdf) > 0:
        with open(cached_rdf, "r") as f:
            s = f.read()
        return cached_rdf, s
    else:
        rdf_string = extract_openai(unstructured_data, api_key=api_key, ontology_name=ontology_name)
        with open(cached_rdf, "w") as f:
            f.write(rdf_string.strip())
        return cached_rdf, rdf_string


def get_tag_badges(data: UnstructuredReactionDescription):
    color_table = {
        METER.LOW.value: "success",
        METER.MEDIUM.value: "warning",
        METER.HIGH.value: "danger",
    }
    try:
        complexity_color = color_table[data.complexity.value]
    except AttributeError:
        complexity_color = "secondary"
    try:
        specificity_color = color_table[data.specificity.value]
    except AttributeError:
        specificity_color = "secondary"
    badges = [
        dbc.Badge(f"Complexity: {data.complexity}", color=complexity_color, className="me-1 mt-2"),
        dbc.Badge(f"Specificity: {data.specificity}", color=specificity_color, className="me-1 mt-2"),
        dbc.Badge(f"Origin: {data.origin}", color="secondary", className="me-1 mt-2"),
    ]
    return html.H4(badges)


# Callback functions
@app.callback(
    Output(COMPONENT_ID_sample_text_box, 'value'),
    Output(COMPONENT_ID_sample_text_tags, 'children'),
    Input(COMPONENT_ID_sample_text_selector, 'value'),
)
def display_sample(sample_text_id):
    if sample_text_id in DATA_SAMPLES:
        data = DATA_SAMPLES[sample_text_id]
    else:
        data = UnstructuredReactionDescription(text="", origin="user provided")
    return data.text, get_tag_badges(data)


@app.callback(
    Output(COMPONENT_ID_output_box, 'children'),
    Output(COMPONENT_ID_cyto, 'elements'),
    Output(COMPONENT_ID_cyto, 'stylesheet'),
    State(COMPONENT_ID_sample_text_box, 'value'),
    State(COMPONENT_ID_ontology_selector, 'value'),
    State(COMPONENT_ID_apikey_input, 'value'),
    Input(COMPONENT_ID_extract_button, 'n_clicks')
)
def run_extract(unstructured_text, ontology_name, api_key, n_clicks):
    if n_clicks:
        try:
            unstructured = DATA_SAMPLES[TEXT_TO_SAMPLE_ID[unstructured_text.strip()]]
        except KeyError:
            unstructured = UnstructuredReactionDescription(text=unstructured_text, origin="user provided")
        rdf_file_path, rdf_file_content = extract_call(unstructured, api_key=api_key, ontology_name=ontology_name)
        display_text = f'''
```xml
{rdf_file_content}
```
        '''
        cyto_data = rdf_to_cyto(rdf_file_path, ONTOLOGY_FILE_PATHS[ontology_name])
        display = dcc.Markdown(display_text, id=str(hash(display_text)),
                               className="overflow-auto")  # magic to deal with highlight js bug
        return display, cyto_data['nodes'] + cyto_data['edges'], cyto_data['style']
    return no_update


@app.callback(Output(COMPONENT_ID_cyto_selection_display, 'children'),
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
    return dash_renderjson.DashRenderjson(data=data, max_depth=-1, theme=JsonTheme, invert_theme=True)
