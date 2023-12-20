import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "l7",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("l7", path=build_dir)

def l7(options, style=None, key=None):
    component_value = _component_func(options=options, style=style, key=key)
    return component_value

def st_l7(options, style=None, key=None):
    return l7(options, style, key=key)
# Add some test code to play with the component while it's in development.
# During development, we can run this just as we would any other Streamlit app.
#
# In frontend, `$ npm run start`
# `$ streamlit run streamlit_l7/__init__.py`
if not _RELEASE:
    import streamlit as st

    options = {
        "mapType": 'Map',
        "layers": [
            {
                "type": 'raster',
                "source": {
                    "data": 'https://tiles{1-3}.geovisearth.com/base/v1/ter/{z}/{x}/{y}?format=webp&tmsIds=w&token=b2a0cfc132cd60b61391b9dd63c15711eadb9b38a9943e3f98160d5710aef788',
                    "parser": {"type": 'rasterTile', "tileSize": 256, "zoomOffset": 0},
                },
            },
            {
                "type": 'raster',
                "source": {
                    "data": 'https://tiles{1-3}.geovisearth.com/base/v1/cat/{z}/{x}/{y}?format=png&tmsIds=w&token=b2a0cfc132cd60b61391b9dd63c15711eadb9b38a9943e3f98160d5710aef788',
                    "parser": {"type": 'rasterTile', "tileSize": 256, "zoomOffset": 1},
                },
            },
            {
                "type": 'choropleth',
                "autoFit": True,
                "source": {
                    "data": {
                        "type": "FeatureCollection",
                        "features": [
                            {
                            "type": "Feature",
                            "properties": {
                                "name": "矩形"
                            },
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                [
                                    [120.554285, 30.145225],
                                    [120.554285, 30.482327],
                                    [120.865317, 30.482327],
                                    [120.865317, 30.145225],
                                    [120.554285, 30.145225]
                                ]
                                ]
                            }
                            },
                            {
                            "type": "Feature",
                            "properties": {"name":"多边形"},
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                [
                                    [120.016222, 30.382493],
                                    [120.270497, 30.396202],
                                    [120.263686, 30.204106],
                                    [120.032115, 30.213916],
                                    [120.016222, 30.382493]
                                ]
                                ]
                            }
                            }
                        ]
                     },


                },
                "fillColor": {
                    "field": 'name',
                    "value": ['#fc8d59','#ffffbf','#91bfdb'],
                },
                "opacity": 0.8,
                "strokeColor": 'blue',
                "lineWidth": 1,
                "state": {
                    "active": { "strokeColor": 'green', "lineWidth": 1.5, "lineOpacity": 0.8 },
                    "select": { "strokeColor": 'red', "lineWidth": 1.5, "lineOpacity": 0.8 },
                },
                "label": {
                    "field": 'name',
                    "visible": True,
                    "style": { "fill": 'blue', "fontSize": 12, "stroke": '#fff', "strokeWidth": 2 },
                },
            },
        ],
        "controls": [
           {
            "type": 'zoom',
           },{
             "type": 'scale',
           },{
              "type": 'fullscreen'
           }
        ],
    }

    l7(options=options, style={"height": 400}, key="streamlit-l7")
