import streamlit as st
from streamlit_l7 import l7

def renderChoroplethMap() :
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


ST_Choropleth_DEMOS = {
    "Choropleth: Basic": (
        renderChoroplethMap
    ),
}