import os
import streamlit.components.v1 as components

_RELEASE = False

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
        "mapType":'Map'
    }

    l7(options=options, style={ "height": 400}, key="streamlit-l7")