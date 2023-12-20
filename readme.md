<h1 align="center">
  <b>streamlit L7</b>
</h1>

<div align="center">

[L7](https://github.com/antvis/L7) is a  Large-scale WebGL-powered Geospatial data visualization analysis framework. [Live Demo](https://l7maps.streamlit.app/)



</div>


## Installation

```
pip install streamlit-L7 
```


## Usage

```py
import streamlit as st
from streamlit_L7 import L7

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

L7(options=options, style=None, key="streamlit_L7")

```


## API

Now, There is only one API for `streamlit-L7`, named `L7`, see the `options` in [L7 React component API](https://larkmap.antv.antgroup.com/components/lark-map).

| Property | Description                                                                                                     | Type                  | Default |
| -------- | --------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| options  | the [options](https://larkmap.antv.antgroup.com/components/lark-map) for the visualization, say `chart.options(options)` | `L7options` \| `null` | -       |
| style    | the style of the container                                                                                      | `CSSProperties`       | -       |


## Development

- Build frontend code by running `npm run build` in fold `streamlit_L7/frontend`.
- Run the example by running `streamlit run app.py` in root dir.

## 

## License

MIT@[lzxue](https://github.com/lzxue).
