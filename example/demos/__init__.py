from .map import ST_MAP_DEMOS
from .choropleth import ST_Choropleth_DEMOS
from .raster import ST_Raster_DEMOS
from .dem import ST_Raster_DEM_DEMOS
ST_DEMOS = {
     **ST_MAP_DEMOS,
     **ST_Choropleth_DEMOS,
     **ST_Raster_DEMOS,
     **ST_Raster_DEM_DEMOS
}