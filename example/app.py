import inspect
import textwrap

import streamlit as st
from demos import ST_DEMOS

def main():
    st.title("Streamlit L7 Map Demo")
    with st.sidebar:
        st.header("Configuration")
        api_options = list(ST_DEMOS.keys())
        selected_demo = st.selectbox(
            label="Choose your preferred demo:",
            options=api_options,
        )
    demo = ST_DEMOS[selected_demo]
    demo()
    
    sourcelines, _ = inspect.getsourcelines(demo)
    with st.expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))
        
if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit L7 Map Demo", page_icon="🌏"
    )
    main()
    with st.sidebar:
        st.markdown("---")
        content = """
        ### Powered by
        - [LarkMap A React toolkit for geospatial visualization based on L7.](https://github.com/antvis/larkmap)
        - [L7 Large-scale WebGL-powered Geospatial data visualization analysis framework.](https://github.com/antvis/l7)
        """
        st.markdown(content)
        