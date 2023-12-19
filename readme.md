<h1 align="center">
  <b>streamlit L7</b>
</h1>

<div align="center">

[L7](https://github.com/antvis/L7) is a visualization grammar for dashboard building, data exploration and storytelling.



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
    "type": "interval",
    "data": [
        { "genre": 'Sports', "sold": 275 },
        { "genre": 'Strategy', "sold": 115 },
        { "genre": 'Action', "sold": 120 },
        { "genre": 'Shooter', "sold": 350 },
        { "genre": 'Other', "sold": 150 },
    ],
    "encode": {
        "x": "genre",
        "y": "sold",
        "color": "genre",
    }
}

L7(options=options, style=None, key="streamlit_L7")
```


## API

Now, There is only one API for `streamlit-L7`, named `L7`, see the `options` in [L7 Spec API](https://L7.antv.antgroup.com/manual/core/api).

| Property | Description                                                                                                     | Type                  | Default |
| -------- | --------------------------------------------------------------------------------------------------------------- | --------------------- | ------- |
| options  | the [options](https://L7.antv.antgroup.com/manual/core/api) for the visualization, say `chart.options(options)` | `L7options` \| `null` | -       |
| style    | the style of the container                                                                                      | `CSSProperties`       | -       |


## Development

- Build frontend code by running `npm run build` in fold `streamlit_L7/frontend`.
- Run the example by running `streamlit run app.py` in root dir.


## License

MIT@[lzxue](https://github.com/lzxue).
