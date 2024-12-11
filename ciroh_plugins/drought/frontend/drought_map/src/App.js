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