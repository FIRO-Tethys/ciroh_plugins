# WMS URLs
wms_urls = {
    "atlas_base_url": "http://ndmc-001.unl.edu:8080/cgi-bin/mapserv.exe?map=/ms4w/apps/BaseLayers/service/base_layers_dra_3857.map",
    "usdm_wms_base_url": "http://ndmc-001.unl.edu:8080/cgi-bin/mapserv.exe?map=/ms4w/apps/usdm/service/",
    "vegdri_wms_url": "https://dmsdata.cr.usgs.gov/geoserver/quickdri_vegdri_conus_week_data/vegdri_conus_week_data/wms",
    "quickdri_wms_url": "https://dmsdata.cr.usgs.gov/geoserver/quickdri_quickdri_conus_week_data/quickdri_conus_week_data/wms",
    "waterwatch_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_water_watch_today/wms",
    "precipdays_7_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_precipcdd7_conus_1_day_data/wms",
    "precipdays_30_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_preciprd30_conus_1_day_data/wms",
    "totprecip_7_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_preciptp7_conus_1_day_data/wms",
    "totprecip_30_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_preciptp30_conus_1_day_data/wms",
    "drydays_7_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_precipcdd7_conus_1_day_data/wms",
    "drydays_30_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_precipcdd30_conus_1_day_data/wms",
    "last_precip_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_precipdsr_conus_1_day_data/wms",
    "usdm_curr_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_drought/wms",
    "nat_land_cover_2019_url": "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2019_Land_Cover_L48/wms",
    "radar_wms_url": "https://gis.ncdc.noaa.gov/arcgis/rest/services/geo/radar_coverage/MapServer/WMSServer",
    "usdm_wms_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_drought/wms",
    "drought_out_url_esri_wms": "https://idpgis.ncep.noaa.gov/arcgis/services/NWS_Climate_Outlooks/cpc_drought_outlk/MapServer/WMSServer",
    "precip_out_url_esri_wms": "https://idpgis.ncep.noaa.gov/arcgis/services/NWS_Climate_Outlooks/cpc_6_10_day_outlk/WMSServer",
    "temp_out_url_esri_wms": "https://idpgis.ncep.noaa.gov/arcgis/rest/services/NWS_Climate_Outlooks/cpc_6_10_day_outlk/WMSServer"
}

# WFS URLs
wfs_urls = {
    "waterwatch_wfs_url": "https://edcintl.cr.usgs.gov/geoserver/quickdri_water_watch_today/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=quickdri_water_watch_today%3Awater_watch_today&outputFormat=application%2Fjson",
    "usdm_current_wfs_url": "https://dservices5.arcgis.com/0OTVzJS4K09zlixn/arcgis/services/USDM_current/WFSServer?service=wfs&request=GetFeature&typeName=USDM_current&outputFormat=GEOJSON"
}

# ESRI URLs
esri_urls = {
    "county_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/Counties/FeatureServer/",
    "climdiv_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/Climate_Divisions/FeatureServer/",
    "climhub_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/Climate_Hubs/FeatureServer/",
    "fema_rgn_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/FEMA_Regions/FeatureServer/",
    "huc2_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/HUC_2_digit/FeatureServer/",
    "nws_rgn_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/NWS_Regions/FeatureServer/",
    "nws_wfo_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/NWS_WFO/FeatureServer/",
    "rcc_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/Regional_Climate_Centers/FeatureServer/",
    "rfc_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/River_Forecast_Centers/FeatureServer/",
    "us_states_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/States/FeatureServer/",
    "urban_area_url_esri": "https://services5.arcgis.com/0OTVzJS4K09zlixn/arcgis/rest/services/Urban_Areas/FeatureServer/"
}

json_urls = {
    "usdm": "https://droughtmonitor.unl.edu/data/json/usdm"
}
# KML URLs
kml_urls = {
    "usgs_strm_real_url_kml": "https://waterwatch.usgs.gov/index.php?m=real&w=kml&r=us&regions=all2"
}

# NIDIS URLs
nidis_urls = {
    "nidis_base_url": "https://storage.googleapis.com/noaa-nidis-drought-gov-data/current-conditions/tile/v1/",
}
