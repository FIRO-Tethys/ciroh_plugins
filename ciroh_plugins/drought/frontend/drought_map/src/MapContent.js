import React, { useEffect, Fragment} from 'react';
import { Vector as VectorLayer } from 'ol/layer';
import VectorSource from 'ol/source/Vector';
import GeoJSON from 'ol/format/GeoJSON';
import { usdmStyle } from './lib/layerStyles';
import {
  View,
  Layer,
  Layers,
  Controls,
  LayersControl,
  LegendControl,
  useMapContext
} from 'backlayer';


const MapComponentContent = (
    { 
        viewConfig, 
        layers, 
        extraLayers,
        legend 
    }
) => {
    console.log(legend)
    const { map } = useMapContext();
    useEffect(() => {
      if (!map) return;
        // Fetch the GeoJSON data and add a vector layer
        const vectorSource = new VectorSource({
          features: new GeoJSON().readFeatures(extraLayers[0],{
            dataProjection: 'EPSG:4326',    // GeoJSON data is in EPSG:4326
            featureProjection: 'EPSG:3857'  // Map is displayed in EPSG:3857
          }),
        });
        const vectorLayer = new VectorLayer({
          source: vectorSource,
          name: 'USDM Archive',
          zIndex: 100,
          style: function (feature) {
            var classify = feature.get('DM');
            return usdmStyle[classify];
          }
        });
  
        map.addLayer(vectorLayer);
    }, [map,extraLayers]);


    return (
      <Fragment>
        <View {...viewConfig} />
        <Layers>
          {layers && layers.map((config, index) => (
            <Layer key={index} config={config} />
          ))}
        </Layers>
        <Controls>
            <LayersControl />
            <LegendControl items={legend} />
        </Controls>
      </Fragment>
    );
  };

export default MapComponentContent;