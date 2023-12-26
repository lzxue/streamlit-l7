import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    print("Running in development mode.")
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

def l7(options, data =None, dataMeta = None, style=None, key=None):
    component_value = _component_func(options=options, data=data, dataMeta=dataMeta, style=style, key=key)
    return component_value

def st_l7(options,data = None, dataMeta =None, style=None, key=None):
    return l7(options, data, dataMeta,style,  key=key)
