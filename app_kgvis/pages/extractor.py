import os

import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
import dash_renderjson
from dash import html, get_app, Input, Output, no_update, State
from dash import register_page, dcc

from ontosynthesis.visualize.cyto import STYLE_SHEET, JsonTheme

_DUMMY_OWL_STRING = """
<owl:NamedIndividual rdf:about="#c2f9d1e9-6aaf-4532-8b44-c011b3554b9f">
  <rdf:type rdf:resource="#SOO_0000304"/>
  <rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">c2f9d1e9-6aaf-4532-8b44-c011b3554b9f</rdfs:label>
  <has_value_functional rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{"identifier": "c2f9d1e9-6aaf-4532-8b44-c011b3554b9f", "made_of": "glass", "max_capacity": {"amount_unit": "mL", "amount_value": 5000.0, "details": ""}}</has_value_functional>
</owl:NamedIndividual>

<owl:NamedIndividual rdf:about="#c9a7758c-8e26-485a-a95b-55e03e73c3fa">
  <rdf:type rdf:resource="#SOO_0000078"/>
  <SOO_0000027 rdf:resource="#c2f9d1e9-6aaf-4532-8b44-c011b3554b9f"/>
  <rdfs:label rdf:datatype="http://www.w3.org/2001/XMLSchema#string">c9a7758c-8e26-485a-a95b-55e03e73c3fa</rdfs:label>
  <has_value_functional rdf:datatype="http://www.w3.org/2001/XMLSchema#string">{"identifier": "c9a7758c-8e26-485a-a95b-55e03e73c3fa", "composition": {"chemical label: S3": {"amount_unit": "mL", "amount_value": 1000.0, "details": ""}}, "state_of_matter": ["LIQUID"], "is_contained_by": {"identifier": "c2f9d1e9-6aaf-4532-8b44-c011b3554b9f", "made_of": "glass", "max_capacity": {"amount_unit": "mL", "amount_value": 5000.0, "details": ""}}}</has_value_functional>
</owl:NamedIndividual>
"""

# page meta
PAGE_ID_HEADER = "EXTRACTOR__"  # id header for components in this page
PAGE_PATH = "/extractor"  # relative url
PAGE_DESCRIPTION = "Extractor"  # appears in navbar
DATA_SAMPLE_JSON = "../../app_extractor/data/data_hackathon.json"
AVAILABLE_ONTOLOGIES = ["SOO", "ORD", ]
# TODO finalize the ontologies we are acutally going to use

# page setup
app = get_app()
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_SAMPLE_JSON = os.path.join(THIS_DIR, DATA_SAMPLE_JSON)
register_page(__name__, path=PAGE_PATH, description=PAGE_DESCRIPTION)
cyto.load_extra_layouts()
from app_extractor.data.data_dump import UnstructuredReactionDescription
from ontosynthesis.utils import json_load

DATA_SAMPLES = json_load(DATA_SAMPLE_JSON)
DATA_SAMPLES = [UnstructuredReactionDescription(**d) for d in DATA_SAMPLES]
DATA_SAMPLES = {d.identifier: d for d in DATA_SAMPLES}

# page components
#### first column
COMPONENT_ID_ontology_selector = f"{PAGE_ID_HEADER}ONTOLOGY_SELECTOR"
component_ontology_selector = dcc.Dropdown(
    options=AVAILABLE_ONTOLOGIES,
    value=AVAILABLE_ONTOLOGIES[0],
    id=COMPONENT_ID_ontology_selector,
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
COMPONENT_ID_extract_button = f"{PAGE_ID_HEADER}EXTRACT_BUTTON"
# TODO add display for reaction complexity and specificity
FIRST_COLUMN = html.Div(
    [
        html.H5(f"Target Ontology", className="text-center mt-3"),
        component_ontology_selector,
        html.H5(f"Unstructured Text", className="text-center mt-3"),
        component_sample_text_selector,
        component_sample_text_box,
        html.Div(
            children=[dbc.Button("Extract", id=COMPONENT_ID_extract_button, className="mt-2")],
            className="d-grid gap-2"
        ),
    ],
    className="col-lg-4 px-2 overflow-auto",
    style={'height': 'calc(100vh - 100px)'},  # minus header bar height
)

#### second column
COMPONENT_ID_output_box = f"{PAGE_ID_HEADER}OUTPUT_BOX"
component_output_box = dcc.Markdown(
    id=COMPONENT_ID_output_box,
    className="mt-2",
)
SECOND_COLUMN = html.Div(
    [
        html.H5(f"Extraction Output", className="text-center mt-3"),
        component_output_box,
    ],
    # className="col-lg-4 px-2 overflow-auto border border-primary",
    className="col-lg-4 px-2 overflow-auto",
    style={'height': 'calc(100vh - 100px)'},  # minus header bar height
)

#### third column
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
    stylesheet=STYLE_SHEET,
    responsive=True,
)
COMPONENT_ID_cyto_selection_display = f"{PAGE_ID_HEADER}CYTO_SELECTION_DISPLAY"
component_cyto_selection_display = dash_renderjson.DashRenderjson(data={}, max_depth=-1, theme=JsonTheme,
                                                                  invert_theme=True)

THIRD_COLUMN = html.Div(
    [
        html.Div(component_cyto, className="h-75 border-primary border"),
        html.Div(component_cyto_selection_display, className="h-25 border-primary border")
    ],
    # className="col-lg-4 px-2 overflow-auto border border-primary",
    className="col-lg-4 px-2 overflow-auto",
    style={'height': 'calc(100vh - 100px)'},  # minus header bar height
)

# page layout
layout = html.Div(
    [dbc.Row([FIRST_COLUMN, SECOND_COLUMN, THIRD_COLUMN, ])],
    style={"width": "calc(100vw - 100px)"}
)


@app.callback(
    Output(COMPONENT_ID_sample_text_box, 'value'),
    Input(COMPONENT_ID_sample_text_selector, 'value'),
)
def display_sample(sample_text_id):
    if sample_text_id in DATA_SAMPLES:
        data = DATA_SAMPLES[sample_text_id]
    else:
        data = UnstructuredReactionDescription(text="", origin="")
    return data.text


@app.callback(
    Output(COMPONENT_ID_output_box, 'children'),
    Output(COMPONENT_ID_cyto, 'elements'),
    State(COMPONENT_ID_sample_text_box, 'value'),
    State(COMPONENT_ID_ontology_selector, 'value'),
    Input(COMPONENT_ID_extract_button, 'n_clicks')
)
def run_extract(unstructured_text, ontology_name, n_clicks):
    if n_clicks:
        syntax = "xml"
        structured_output = _DUMMY_OWL_STRING
        # TODO implement actual extraction from `unstructured_text` given an `ontology_name` (T-box)
        display = f'''
```{syntax}
{structured_output}
```
        '''
        # TODO get A-box from structured output
        # TODO get cytoscape elements for A-box
        return display, []
    return no_update
