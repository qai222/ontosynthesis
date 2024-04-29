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
