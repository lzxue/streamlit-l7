import React from 'react';
import {
    PointLayer,
    LineLayer,
    PolygonLayer,
    RasterLayer,
    HeatmapLayer,
    TextLayer,
    BubbleLayer,
    ChoroplethLayer,
    IconFontLayer,
    IconImageLayer,
    FlowLayer,
    LogoControl,
    ZoomControl,
    ScaleControl,
    FullscreenControl,
    GeoLocateControl,
    ExportImageControl,
    MouseLocationControl,
    LayerSwitchControl,
    MapThemeControl,
    LegendCategories,
    LegendIcon,
    LegendProportion,
    LegendRamp
} from '@antv/larkmap';

import type {
    LarkMapProps,
    PointLayerProps,
    LineLayerProps,
    PolygonLayerProps,
    RasterLayerProps,
    HeatmapLayerProps,
    TextLayerProps,
    BubbleLayerProps,
    ChoroplethLayerProps,
    IconFontLayerProps,
    IconImageLayerProps,
    FlowLayerProps,
    LogoControlProps,
    ZoomControlProps,
    ScaleControlProps,
    FullscreenControlProps,
    GeoLocateControlProps,
    ExportImageControlProps,
    MouseLocationControlProps,
    LayerSwitchControlProps,
    MapThemeControlProps,
    LegendCategoriesProps,
    LegendIconProps,
    LegendProportionProp,
    LegendRampProps


} from '@antv/larkmap';
export type ILayerType =
    PointLayerProps & { type: 'point' }
    | LineLayerProps & { type: 'line' }
    | PolygonLayerProps & { type: 'polygon' }
    | RasterLayerProps & { type: 'raster' }
    | HeatmapLayerProps & { type: 'heatmap' }
    | TextLayerProps & { type: 'text' }
    | BubbleLayerProps & { type: 'bubble' }
    | ChoroplethLayerProps & { type: 'choropleth' }
    | IconFontLayerProps & { type: 'iconfont' }
    | IconImageLayerProps & { type: 'iconimage' }
    | FlowLayerProps & { type: 'flow' };
export type IControlType = LogoControlProps & { type: 'logo' }
    | ZoomControlProps & { type: 'zoom' }
    | ScaleControlProps & { type: 'scale' }
    | FullscreenControlProps & { type: 'fullscreen' }
    | GeoLocateControlProps & { type: 'geolocate' }
    | ExportImageControlProps & { type: 'exportimage' }
    | MouseLocationControlProps & { type: 'mouselocation' }
    | LayerSwitchControlProps & { type: 'layerswitch' }
    | MapThemeControlProps & { type: 'maptheme' };
export type ILegendType = LegendCategoriesProps & { type: 'categories' }
    | LegendIconProps & { type: 'icon' }
    | LegendProportionProp & { type: 'proportion' }
    | LegendRampProps & { type: 'ramp' };
export interface IMapOptions extends LarkMapProps {
    /**
     * 图层配置
     */
    layers?: ILayerType[];
    controls?: IControlType[];
    legends?: ILegendType[];
}

export function renderLayers(layers: ILayerType[]) {
    return layers.map((layer,index) => {
        switch (layer.type) {
            case 'point':
                return <PointLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'line':
                return <LineLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'polygon':
                return <PolygonLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'raster':
                return <RasterLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'heatmap':
                return <HeatmapLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'text':
                return <TextLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'bubble':
                return <BubbleLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'choropleth':
                return <ChoroplethLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'iconfont':
                return <IconFontLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'iconimage':
                return <IconImageLayer key={`${layer.type}_${index}`} {...layer} />;
            case 'flow':
                return <FlowLayer key={`${layer.type}_${index}`} {...layer} />;
            default:
                return null;
        }
        
    });

}

export function renderControls(controls: IControlType[]) {
    return controls.map((control,index) => {
        switch (control.type) {
            case 'logo':
                return <LogoControl key={`${control.type}_${index}`} {...control} />;
            case 'zoom':
                return <ZoomControl key={`${control.type}_${index}`} {...control} />;
            case 'scale':
                return <ScaleControl key={`${control.type}_${index}`} {...control} />;
            case 'fullscreen':
                return <FullscreenControl key={`${control.type}_${index}`} {...control} />;
            case 'geolocate':
                return <GeoLocateControl key={`${control.type}_${index}`} {...control} />;
            case 'exportimage':
                return <ExportImageControl key={`${control.type}_${index}`} {...control} />;
            case 'mouselocation':
                return <MouseLocationControl key={`${control.type}_${index}`} {...control} />;
            case 'layerswitch':
                return <LayerSwitchControl key={`${control.type}_${index}`} {...control} />;
            case 'maptheme':
                return <MapThemeControl key={`${control.type}_${index}`} {...control} />;
            default:
                return null;
        }
    });
}

export function renderLegends(legends: ILegendType[]) {
    return legends.map((legend,index) => {
        switch (legend.type) {
            case 'categories':
                return <LegendCategories key={`${legend.type}_${index}`} {...legend} />;
            case 'icon':
                return <LegendIcon key={`${legend.type}_${index}`} {...legend} />;
            case 'proportion':
                return <LegendProportion key={`${legend.type}_${index}`} {...legend} />;
            case 'ramp':
                return <LegendRamp key={`${legend.type}_${index}`} {...legend} />;
            default:
                return null;
        }
    });
}
