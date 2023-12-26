import streamlit as st

from cnmaps import get_adm_maps
boundary = get_adm_maps(level='省',engine='geopandas')
for i in boundary:
   
