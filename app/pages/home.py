import dash_bootstrap_components as dbc
from dash import html, get_app
from dash import register_page

register_page(__name__, path='/', description="Home")


def get_card(title: str, text: str, link_text: str, link_path: str = "#", width: int = 22):
    card = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H4(title, className="card-title"),
                    html.P(
                        text,
                        className="card-text",
                    ),
                    dbc.Button(link_text, color="primary", href=link_path),
                ]
            ),
        ],
        style={"min-width": f"{width}rem", "width": f"{width}rem"},
        className="mx-4"
    )
    return card


card_soo_viewer = get_card(
    title="Synthesis Operation Ontology",
    text="A tree view of the Synthesis Operation Ontology (SOO).",
    link_text="Ontology Viewer",
    link_path="/onto_viewer",
    width=20,
)

card_soo_repr = get_card(
    title="KG Procedure Representation",
    text="Knowledge graph representation for organic synthesis procedure.",
    link_text="Procedure Graph",
    link_path="/kgpr",
    width=20,
)

layout = dbc.Row(
    [dbc.Col(
        [
            card_soo_viewer,
            card_soo_repr,
        ],
        className="justify-content-left col-8 d-flex mx-auto mt-5"
    ),
    ],
    className="align-items-center",
    style={"min-height": "50vh"}
)

app = get_app()
