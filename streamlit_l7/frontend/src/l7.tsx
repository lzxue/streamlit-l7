import React from 'react';
import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from 'streamlit-component-lib';
import { LarkMap } from '@antv/larkmap';
import type { IMapOptions } from './map'
import { renderLayers, renderLegends, renderControls } from './map'


const DefaultMapOptions: IMapOptions = {
  mapType: 'Map',
  layers: [{
    type: 'raster',
    source: {
      data: 'https://tiles{1-3}.geovisearth.com/base/v1/img/{z}/{x}/{y}?format=webp&tmsIds=w&token=b2a0cfc132cd60b61391b9dd63c15711eadb9b38a9943e3f98160d5710aef788',
      parser: { type: 'rasterTile', tileSize: 256, zoomOffset: 0 },
    },
  }],
  controls: [],
  legends: [],
}

const L7Component: React.FC<ComponentProps> = (props) => {
  const { style, options } = props.args as { style: any; options: IMapOptions };
  const newOptions = { ...DefaultMapOptions, ...options };
  const { layers = [], controls = [], legends = [],onSceneLoaded, ...SceneOptions } = newOptions;
  return (
    <LarkMap style={{ height: 400, ...style }}  {...SceneOptions} onSceneLoaded={(e) => {
      Streamlit.setFrameHeight((style.height || 400)+ 10)
      if (SceneOptions.onLoaded)
        SceneOptions.onLoaded(e)

    }}>
      {
        renderLayers(layers)
      }
      {
        renderLegends(legends)
      }
      {
        renderControls(controls)
      }

    </LarkMap>

  )
};

export const L7 = withStreamlitConnection(L7Component)
