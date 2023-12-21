import streamlit as st
from streamlit_l7 import l7

def renderBasicMap() :
    options = {
        "mapType": 'Map',
         "mapOptions": {
            "style": 'light',
            "center": [120.210792, 30.246026],
            "zoom": 9,
        },
        "layers": [
            {
                "type": 'raster',
                "source": { 
                    "data": 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                    "parser": {"type": 'rasterTile', "tileSize": 256, "zoomOffset": 0},
                },
            },
        ]
    }
    l7(options=options, style={"height": 400}, key="streamlit-l7")

ST_MAP_DEMOS = {
    "Map: Basic Map": (
        renderBasicMap
    ),
}