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

const formatLayerConfig = (layers: any[], data: any, meta: any) => {
  return layers.map((layer: any) => {
    const { type, source } = layer;
    const parser = source.parser;
    if (type === 'raster') {
      if (parser.type === 'rgb' || parser.type === 'raster') {
        parser.width = meta.width;
        parser.height = meta.height;
        parser.extent = meta.extent;
      }

    }
    return {
      ...layer,
      source: {
        ...source,
        data: data,
        parser

      }
    }
  })
}

const L7Component: React.FC<ComponentProps> = (props) => {
  const { style, options, data, dataMeta } = props.args as { style: any; options: IMapOptions, data: any, dataMeta: any };
  const newOptions = { ...DefaultMapOptions, ...options };
  if (data && dataMeta) {
    let rasterData = data.dataTable.data.childData.map((item: any) => {
      return item.values;
    })
    if(rasterData.length===1){
      rasterData = rasterData[0];
    }
    newOptions.layers = formatLayerConfig(newOptions.layers || [], rasterData, dataMeta)
  }
  console.log(newOptions.layers)
  const { layers = [], controls = [], legends = [], onSceneLoaded, ...SceneOptions } = newOptions;
  return (
    <LarkMap style={{ height: 400, ...style }}  {...SceneOptions} onSceneLoaded={(e) => {
      Streamlit.setFrameHeight((style.height || 400) + 10)
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
