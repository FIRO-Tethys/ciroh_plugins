// import React, { useRef, useEffect, useState, createContext, useContext } from 'react';
// import Map from 'ol/Map';
// import View from 'ol/View';
// import OSM from 'ol/source/OSM';

import React, { useEffect} from 'react';
import 'ol/ol.css';
import {
  Map
} from 'backlayer';
import MapComponentContent from './MapContent';

const MapComponent = (
  { 
    mapConfig, 
    viewConfig, 
    layers,
    extraLayers
  }) => {


  return (
    <Map {...mapConfig} >
      <MapComponentContent viewConfig={viewConfig} layers={layers} extraLayers={extraLayers} />
    </Map>
  );
}

export default MapComponent;



// const MapContext = createContext(null);

// export const useMap = () => {
//   return useContext(MapContext);
// };


// const MapProvider = ({ children }) => {
//   const [map, setMap] = useState(null);
//   const mapRef = useRef();

//   useEffect(() => {
//     if (!map) {
//       const initialMap = new Map({
//         target: mapRef.current,
//         view: new View({
//           center: [-11807318, 4983337],
//           zoom: 4,
//           maxZoom: 11,
//           minZoom: 3,
//         }),
//         layers: [
//           new TileLayer({
//             source: new OSM(),
//           }),
//         ],
//       });
//       setMap(initialMap);
//     }
//   }, []);

//   return (
//     <MapContext.Provider value={map}>
//       <div ref={mapRef} style={ {"width": "100%", "height": "100%", "position": "relative"}}>
//         {children}
//       </div>
//     </MapContext.Provider>
//   );
// };

// ///////////////////////////////////
// // MapWithLayers Component
// ///////////////////////////////////
// const MapWithLayers = ({layers}) => {
//   const map = useMap();

//   useEffect(() => {
//     if (!map) return;
//       console.log(new GeoJSON().readFeatures(layers[0],{
//         dataProjection: 'EPSG:4326',    // GeoJSON data is in EPSG:4326
//         featureProjection: 'EPSG:3857'  // Map is displayed in EPSG:3857
//       }));

//       // Fetch the GeoJSON data and add a vector layer
//       const vectorSource = new VectorSource({
//         features: new GeoJSON().readFeatures(layers[0],{
//           dataProjection: 'EPSG:4326',    // GeoJSON data is in EPSG:4326
//           featureProjection: 'EPSG:3857'  // Map is displayed in EPSG:3857
//         }),
//       });
//       const vectorLayer = new VectorLayer({
//         source: vectorSource,
//         style: function (feature) {
//           var classify = feature.get('DM');
//           return usdmStyle[classify];
//         }
//       });

//       map.addLayer(vectorLayer);
//   }, [map]);

//   return null;
// };
// const MapComponent = ({layers}) => {
//   return (
//     <MapProvider>
//       <MapWithLayers layers={layers} />
//     </MapProvider>
//   );
// };

// export default MapComponent;