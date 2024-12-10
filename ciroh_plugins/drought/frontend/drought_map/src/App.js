import React, { useRef, useEffect, useState, createContext, useContext } from 'react';
import Map from 'ol/Map';
import View from 'ol/View';
import { Tile as TileLayer, Vector as VectorLayer } from 'ol/layer';
import OSM from 'ol/source/OSM';
import VectorSource from 'ol/source/Vector';
import GeoJSON from 'ol/format/GeoJSON';
import { Fill, Stroke, Style } from 'ol/style';
import 'ol/ol.css';

///////////////////////////////////
// MapContext and custom hook
///////////////////////////////////
const MapContext = createContext(null);

export const useMap = () => {
  return useContext(MapContext);
};


const MapProvider = ({ children }) => {
  const [map, setMap] = useState(null);
  const mapRef = useRef();

  useEffect(() => {
    if (!map) {
      const initialMap = new Map({
        target: mapRef.current,
        view: new View({
          center: [-98.5795, 39.8283], // Approximate center of the US (in lon/lat)
          zoom: 4,
          projection: 'EPSG:3857', // Default projection for OSM
        }),
        layers: [
          new TileLayer({
            source: new OSM(),
          }),
        ],
      });
      setMap(initialMap);
    }
  }, [map]);

  return (
    <MapContext.Provider value={map}>
      <div ref={mapRef} style={{ width: '100%', height: '100vh' }}>
        {children}
      </div>
    </MapContext.Provider>
  );
};

///////////////////////////////////
// MapWithLayers Component
///////////////////////////////////
const MapWithLayers = () => {
  const map = useMap();

  useEffect(() => {
    if (!map) return;

    // Fetch the GeoJSON data and add a vector layer
    const url = 'https://droughtmonitor.unl.edu/data/json/usdm_20241203.json';

    fetch(url)
      .then(response => response.json())
      .then(geojsonData => {
        const geojsonFormat = new GeoJSON();
        const features = geojsonFormat.readFeatures(geojsonData, {
          featureProjection: 'EPSG:3857',
        });

        const vectorSource = new VectorSource({
          features: features,
        });

        const droughtStyle = new Style({
          fill: new Fill({ color: 'rgba(255, 0, 0, 0.3)' }),
          stroke: new Stroke({ color: '#ff0000', width: 1 }),
        });

        const vectorLayer = new VectorLayer({
          source: vectorSource,
          style: droughtStyle,
        });

        map.addLayer(vectorLayer);
      })
      .catch(error => {
        console.error('Error loading GeoJSON data:', error);
      });
  }, [map]);

  return null;
};


const MapComponent = () => {
  return (
    <MapProvider>
      <MapWithLayers />
    </MapProvider>
  );
};

export default MapComponent;
