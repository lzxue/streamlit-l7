import React from 'react';
import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from 'streamlit-component-lib';
import { LarkMap,RasterLayer } from '@antv/larkmap';

const L7Component: React.FC<ComponentProps> = (props) => {
  const { style, options } = props.args;
  return (
    <LarkMap style={{height:400,...style}} mapType = {options.mapType || 'map'} onSceneLoaded={() => {
      Streamlit.setFrameHeight(style.height)
    }}>
    <RasterLayer
        source={{
          data:   'https://tiles{1-3}.geovisearth.com/base/v1/img/{z}/{x}/{y}?format=webp&tmsIds=w&token=b2a0cfc132cd60b61391b9dd63c15711eadb9b38a9943e3f98160d5710aef788',
          parser: { type: 'rasterTile', tileSize: 256, zoomOffset: 0 },
        }}
      />
    </LarkMap>

  )
};

export const L7 = withStreamlitConnection(L7Component)
