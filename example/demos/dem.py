
import rasterio
from rasterio.warp import transform_bounds
from pyproj import CRS
import streamlit as st
import pandas as pd
import pyarrow as pa
import streamlit as st
from streamlit_l7 import l7

import streamlit.components.v1 as components

# _component_func = components.declare_component(
#     "l7",
#     # Pass `url` here to tell Streamlit that the component will be served
#     # by the local dev server that you run via `npm run start`.
#     # (This is useful while your component is in development.)
#     url="http://localhost:3001",
# )
# def l7(options, data =None, dataMeta = None, style=None, key=None):
#     component_value = _component_func(options=options, data=data, dataMeta=dataMeta, style=style, key=key)
#     return component_value


def renderDemMap() :
    # 打开 GeoTIFF 文件
    with rasterio.open("example/static/china_dem.tif") as src:
        # 读取栅格数据
        raster_data = src.read()  # 读取第一个波段的数据
        target_crs = CRS.from_epsg(4326)
        # 获取地理元数据
        crs = src.crs  # 坐标参考系统 
        width = src.width  # 宽度
        height = src.height  # 高度
        
        left, bottom, right, top = src.bounds  # 边界框
        minlon, minlat, maxlon, maxlat = transform_bounds(crs, target_crs, left, bottom, right, top)  # 边界框
        st.write( minlon, minlat, maxlon, maxlat)  # 边界框
        raster_data = src.read()
        table_data = []
        for index, band in enumerate(raster_data):
            table_data.append(('band_'+str(index), pa.array(band.flatten(), type=pa.int32())))
        df = pd.DataFrame(dict(table_data))
        
        dataMeta =dict(
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
                        "type": 'raster',
                    }
                },
                "style": {
                    'opacity': 1,
                    'clampLow': False,
                    'clampHigh': False,
                    'domain': [0, 10000],
                    'rampColors': {
                        'type':'custom',
                        'colors': ['#b2182b','#d6604d','#f4a582','#fddbc7','#f7f7f7','#d1e5f0','#92c5de','#4393c3','#2166ac'],
                        'positions': [0, 50, 200, 500, 2000, 3000, 4000, 5000, 8000,10000],
                    },
                }
                }
            ]
        }
        # st.write(options)
        st.markdown("### 高程图")
        l7(options=options,data=df, dataMeta= dataMeta, style={"height": 400}, key="streamlit-l7-1")
            
ST_Raster_DEM_DEMOS = {
    "Raster: Dem Map": (
        renderDemMap
    ),
}