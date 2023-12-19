<h1 align="center">
  <b>streamlit L7</b>
</h1>

<div align="center">

[L7](https://github.com/antvis/L7) is a visualization grammar for dashboard building, data exploration and storytelling.

This project was created to allow us to render [L7](https://github.com/antvis/L7) charts in streamlit. [Live Demo](https://antv-L7.streamlit.app/).

![examples](https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*_GfqQoRCqQkAAAAAAAAAAAAADmJ7AQ/fmt.webp)

[![PyPI version](https://badge.fury.io/py/streamlit-L7.svg)](https://badge.fury.io/py/streamlit-L7)
[![Build Status](https://github.com/antvis/L7/workflows/build/badge.svg?branch=v5)](https://github.com/antvis//actions)
[![Coverage Status](https://img.shields.io/coveralls/github/antvis/L7/v5.svg)](https://coveralls.io/github/antvis/L7?branch=v5)
[![npm Version](https://img.shields.io/npm/v/@antv/L7.svg)](https://www.npmjs.com/package/@antv/L7)
[![npm Download](https://img.shields.io/npm/dm/@antv/L7.svg)](https://www.npmjs.com/package/@antv/L7)
[![npm License](https://img.shields.io/npm/l/@antv/L7.svg)](https://www.npmjs.com/package/@antv/L7)

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

<img src="https://mdn.alipayobjects.com/huamei_qa8qxu/afts/img/A*XqCnTbkpAkQAAAAAAAAAAAAADmJ7AQ/fmt.webp" width="640" alt="example">


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
