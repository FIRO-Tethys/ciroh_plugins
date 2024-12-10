[![version](https://img.shields.io/npm/v/mfe-ol.svg?style=flat-square)](https://npmjs.org/mfe-ol)
[![min size](https://img.shields.io/bundlephobia/min/mfe-ol?style=flat-square)](https://bundlephobia.com/result?p=mfe-ol)
[![mingzip size](https://img.shields.io/bundlephobia/minzip/mfe-ol)](https://bundlephobia.com/result?p=mfe-ol)
[![license](https://img.shields.io/npm/l/mfe-ol?color=%23007a1f&style=flat-square)](https://github.com/Aquaveo/mfe-ol/blob/master/LICENSE)

[![dependancies](https://img.shields.io/librariesio/release/npm/mfe-ol?color=%23007a1f&style=flat-square)](https://libraries.io/npm/mfe-ol)
[![downloads](https://img.shields.io/npm/dm/mfe-ol?style=flat-square&color=%23007a1f)](https://npmcharts.com/compare/mfe-ol)

[![code of conduct](https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=flat-square)](https://github.com/Aquaveo/mfe-ol/blob/master/CODE_OF_CONDUCT.md)

[![stargazers](https://img.shields.io/github/stars/Aquaveo/mfe-ol?style=social)](https://github.com/Aquaveo/mfe-ol/stargazers)
[![number of forks](https://img.shields.io/github/forks/Aquaveo/mfe-ol?style=social)](https://github.com/Aquaveo/mfe-ol/fork)

###### :heart: to [auto badger](https://github.com/technikhil314/auto-badger) for making badging simple

# MFE-OL (MicroFrontEnd Module for Open Layers)

The following is a react component that serves as the UI for the map plugin from the [nwms-plugins](https://github.com/FIRO-Tethys/nwmp_plugins) for the tethysDash application.

## Getting Started

The following npm package exports a remote entry point using the [ModuleFederationPlugin](https://webpack.js.org/concepts/module-federation/) feature on webpack. This can be use as an example for an npm package that accompanies a python plugin for the tethysdash app

## Configuration

The following is the structure of this project:

```
├── package.json
├── package-lock.json
├── public
│   ├── index.html
│   └── robots.txt
├── README.md
├── src
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   └── index.js
├── structure.txt
└── webpack.config.js

3 directories, 11 files
```

The following is added to the `webpack.config.js` file:

```js
    ....
    new ModuleFederationPlugin({
      name: 'mfe_ol',
      filename: 'remoteEntry.js',
      exposes: {
        './MapComponent': './src/App', // Adjusted path to exposed module
      },
      shared: {
        'react': {
          singleton: true,
          requiredVersion: '^18.3.1',
          eager: true,
        },
        'react-dom': {
          singleton: true,
          requiredVersion: '^18.3.1',
          eager: true,
        },
      },
    }),
    new HtmlWebpackPlugin({
      template: './public/index.html'
    })
    ....
```

Similarly, please note that the `filename` can be any name. It refers to the name of the entrypoint file.

Please note that the `exposes` section will be the component that you will like to expose through the entrypoint. The `expose` section exposes the `MapComponent` that is imported in the `App.js` file.

Finally, you need to edit the `package.json` to expose the entrypoint as well

```json
  "exports": {
    ".": "./dist/bundle.js",
    "./remoteEntry": "./dist/remoteEntry.js"
  },
```

the `"."` is the main bundle, while the `"./remoteEntry"` refers to the entrypoint that will be used by the Tethysdash app.

## Use

When the package is ready to use, you need to build it and publish it.

```bash
$ npm run build
$ npm publish
```

Once published you can access the `remoteEntry.js` file on your TethysDash intake driver plugin in the following way:

```python
    def __init__(self, base_map_layer, zoom, services, huc_id, metadata=None):
        # self.mfe_unpkg_url = "http://localhost:3000/remoteEntry.js" # if you are developing
        self.mfe_unpkg_url = "https://unpkg.com/mfe-ol@latest/dist/remoteEntry.js"
        self.mfe_scope = "mfe_ol"
        self.mfe_module = "./Map"
        self.zoom = zoom
        self.huc_id = huc_id
        parts = services.split("/")
        self.service = parts[-3]
        self.layer_id = int(parts[-1])
        self.BASE_URL = "/".join(parts[:-3])
        self.base_map_layer = self.get_esri_base_layer_dict(base_map_layer)
        self.service_layer = self.get_service_layer_dict()
        self.center = self.get_center()
        self.view = self.get_view_config(center=self.center, zoom=self.zoom)
        self.map_config = self.get_map_config()
        self.legend = self.make_legend()
        self.HUC_LAYER = self.get_wbd_layer()

        super(MapVisualization, self).__init__(metadata=metadata)

    def read(self):
        logger.info("Reading map data configuration")
        layers = [self.base_map_layer, self.HUC_LAYER, self.service_layer]
        return {
            "url": self.mfe_unpkg_url,
            "scope": self.mfe_scope,
            "module": self.mfe_module,
            "props": {
                "layers": layers,
                "viewConfig": self.view,
                "mapConfig": self.map_config,
                "legend": self.legend,
            },
        }
```

## TroubleShooting

### Common Errors

Webpack not loading the shared module on the ModuleFederation plugin

```bash
_Uncaught Error: Shared module is not available for eager consumption: webpack/sharing/consume/default/react/react_
```

#### Links

- [Docs](https://webpack.js.org/concepts/module-federation/#troubleshooting)

## Some Useful Examples

- [Article](https://dev.to/devsmitra/the-complete-guide-to-micro-frontend-with-reactjs-for-2022-36b2)
- [Github](https://github.com/devsmitra/micro)
