import React, {memo} from "react";

import {
  Map,
  View,
  Layer,
  Layers,
  Controls,
  LegendControl,
  LayersControl,
  Overlays,
  OverLay,
} from 'backlayer';

import {
  DemoLayers,
  DemoViewConfig,
  DemoMapConfig,
  DemoLegend,
  DemoOverlays,
} from 'backlayer/demo';

const MapComponent = (
  { 
    mapConfig = DemoMapConfig, 
    viewConfig = DemoViewConfig, 
    layers = DemoLayers, 
    legend = DemoLegend,
    overlays= DemoOverlays,
  }) => {

  return (
    <Map {...mapConfig} >
        <View {...viewConfig} />
        <Layers>
          {layers &&
          layers.map((config, index) => (
            <Layer key={index} config={config} />
          ))}
        </Layers>
        <Controls>
            <LayersControl />
            <LegendControl items={legend} />
        </Controls>
        <Overlays>
          {overlays && 
          overlays.map((config, index) => (
            <OverLay key={index} {...config.props}></OverLay>
          ))
          }

        </Overlays>
    </Map>
  );
}

export default memo(MapComponent);