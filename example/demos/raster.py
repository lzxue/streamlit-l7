import rasterio
from rasterio.warp import transform_bounds
from pyproj import CRS
import streamlit as st
import pandas as pd
import pyarrow as pa
import streamlit as st
from streamlit_l7 import l7

import streamlit.components.v1 as components

# Function to update the bands combination of the layer
def setBands(options, new_bands):
    options['layers'][0]['source'] = {"data": '', "parser": {"type": 'rgb', "bands": new_bands}}
    return options

# Function to render the raster map
def renderRasterMap():
    # Open the GeoTIFF file
    with rasterio.open("example/static/LC08_3857_clip_2.tif") as src:
        # Read raster data
        raster_data = src.read()
        target_crs = CRS.from_epsg(4326)
        # Get geospatial metadata
        crs = src.crs
        width = src.width
        height = src.height
        
        left, bottom, right, top = src.bounds
        minlon, minlat, maxlon, maxlat = transform_bounds(crs, target_crs, left, bottom, right, top)
        st.write(minlon, minlat, maxlon, maxlat)
        raster_data = src.read()
        table_data = []
        for index, band in enumerate(raster_data):
            table_data.append(('band_'+str(index), pa.array(band.flatten(), type=pa.uint16())))
        df = pd.DataFrame(dict(table_data))
        
        dataMeta = dict(
            width=width,
            height=height,
            extent=[minlon, minlat, maxlon, maxlat],
            crs=crs.to_dict(),
            count=src.count,
        )

        options = {
            "mapType": 'Map',
            "mapOptions": {
                "center": [120.210792, 30.246026],
                "zoom": 9,
            },
            "layers": [
                {
                "type": 'raster',
                "autoFit": True,
                "source": {
                    "data": '',
                    "parser": {
                    "type": 'rgb',
                    "bands": [3, 2, 1]
                    }
                },
                "style": {
                    "opacity": 1,
                }
                }
            ]
        }

        st.markdown("### Landsat 8 Visualization")
        st.markdown("#### False-Color Infrared Image")
        st.markdown("Create a false-color image using the Near-Infrared (NIR), Red, and Green bands. Commonly, use bands 5-4-3 for Landsat 8.")
        l7(options=setBands(options,[4,3,2]),data=df, dataMeta= dataMeta, style={"height": 400}, key="streamlit-l7-1")
        st.markdown("#### RGB Image")
        st.markdown("Combine the Red, Green, and Blue bands into a standard RGB image. Typically, use bands 4-3-2 for Landsat 8.")
        l7(options=setBands(options,[3,2,1]),data=df, dataMeta= dataMeta, style={"height": 400}, key="streamlit-l7-2")
        st.markdown("#### Soil and Vegetation Image")
        st.markdown("Highlight both soil and vegetation features by combining the SWIR, Red, and Green bands. Use bands 7-4-3 for Landsat 8.")
        l7(options=setBands(options,[6,3,2]),data=df, dataMeta= dataMeta, style={"height": 400}, key="streamlit-l7-3")
        st.markdown("#### Natural Color Image (Alternate)")
        st.markdown("Create a natural color image with a different combination. Use the Blue, Green, and Red bands. Use bands 2-3-4 for Landsat 8.")
        l7(options=setBands(options,[1,2,3]),data=df, dataMeta= dataMeta, style={"height": 400}, key="streamlit-l7-4")      
        st.markdown("#### Urban Image")
        st.markdown("Highlight urban features by combining the Red, Green, and Blue bands. Use bands 6-5-4 for Landsat 8. Urban areas appear bright, and vegetation appears in shades of red.")
        l7(options=setBands(options,[5,4,3]),data=df, dataMeta= dataMeta, style={"height": 400}, key="streamlit-l7-5") 

# 在 Streamlit 应用中添加 DEMO
ST_Raster_DEMOS = {
    "Raster: Basic Map": (
        renderRasterMap
    ),
}
