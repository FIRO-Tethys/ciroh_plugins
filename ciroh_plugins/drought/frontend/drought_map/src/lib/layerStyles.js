// Importing OpenLayers style modules
import Style from 'ol/style/Style';
import Stroke from 'ol/style/Stroke';
import Fill from 'ol/style/Fill';
import Circle from 'ol/style/Circle';
import RegularShape from 'ol/style/RegularShape';

//Basic styles
var styleBorder000000 = new Style({
    stroke: new Stroke({
        color: '#000000',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderCCCCCC = new Style({
    stroke: new Stroke({
        color: '#CCCCCC',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderFF0000 = new Style({
    stroke: new Stroke({
        color: '#FF0000',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder00FF00 = new Style({
    stroke: new Stroke({
        color: '#00FF00',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder0000FF = new Style({
    stroke: new Stroke({
        color: '#0000FF',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderFFFF00 = new Style({
    stroke: new Stroke({
        color: '#FFFF00',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderFFFFFF = new Style({
    stroke: new Stroke({
        color: '#FFFFFF',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderF00000 = new Style({
    stroke: new Stroke({
        color: '#F00000',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder0F0000 = new Style({
    stroke: new Stroke({
        color: '#0F0000',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder1E90FF = new Style({
    stroke: new Stroke({
        color: '#1E90FF',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder00008B = new Style({
    stroke: new Stroke({
        color: '#00008B',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder008B8B = new Style({
    stroke: new Stroke({
        color: '#008B8B',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder8A2BE2 = new Style({
    stroke: new Stroke({
        color: '#8A2BE2',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder8B4513 = new Style({
    stroke: new Stroke({
        color: '#8B4513',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder006400 = new Style({
    stroke: new Stroke({
        color: '#006400',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderA9A9A9 = new Style({
    stroke: new Stroke({
        color: '#A9A9A9',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderB8860B = new Style({
    stroke: new Stroke({
        color: '#B8860B',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderB22222 = new Style({
    stroke: new Stroke({
        color: '#B22222',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderF08080 = new Style({
    stroke: new Stroke({
        color: '#F08080',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderFF4500 = new Style({
    stroke: new Stroke({
        color: '#FF4500',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderFFA500 = new Style({
    stroke: new Stroke({
        color: '#FFA500',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderFF00FF = new Style({
    stroke: new Stroke({
        color: '#FF00FF',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder555555 = new Style({
    stroke: new Stroke({
        color: '#555555',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorder00FFFF = new Style({
    stroke: new Stroke({
        color: '#00FFFF',
        width: 1
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

//----CoCoRaHS Styles----
var cocorahsStyle0 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(110, 110, 110, 0)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 0)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});
var cocorahsStyle1 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(186, 110, 110, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(130, 0, 0, 1)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});
var cocorahsStyle2 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(234, 146, 146, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(250, 0, 0, 1)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});
var cocorahsStyle3 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(232, 188, 112, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(230, 170, 45, 1)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});
var cocorahsStyle4 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(221, 221, 221, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(187, 187, 187, 1)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});
var cocorahsStyle5 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(113, 200, 105, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 170, 0, 1)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});
var cocorahsStyle6 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(111, 135, 232, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 40, 255, 1)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});
var cocorahsStyle7 = new Style({
    image: new RegularShape({
        radius: 5,
        fill: new Fill({
            color: 'rgba(186, 121, 228, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(130, 0, 220, 1)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});

var cocorahsStyleHighlight = new Style({
    image: new RegularShape({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 255, 255, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 245, 245, 1)',
            width: 2
        }),
        points: 3,
        radius: 10,
        angle: 0
    })
});

var cocorahsStyle = {
    'Severely Dry': cocorahsStyle1,
    'Moderately Dry': cocorahsStyle2,
    'Mildly Dry': cocorahsStyle3,
    'Near Normal': cocorahsStyle4,
    'Mildly Wet': cocorahsStyle5,
    'Moderately Wet': cocorahsStyle6,
    'Severely Wet': cocorahsStyle7,
}

var cocorahsStyleDyn = {
    'Severely Dry': cocorahsStyle1,
    'Moderately Dry': cocorahsStyle2,
    'Mildly Dry': cocorahsStyle3,
    'Near normal': cocorahsStyle4,
    'Mildly Wet': cocorahsStyle5,
    'Moderately Wet': cocorahsStyle6,
    'Severely Wet': cocorahsStyle7,
}

var cocorahsStyle0Sq = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(110, 110, 110, 0)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 0)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});
var cocorahsStyle1Sq = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(115, 0, 0, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});
var cocorahsStyle2Sq = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(215, 48, 39, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});
var cocorahsStyle3Sq = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(252, 141, 89, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});
var cocorahsStyle4Sq = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(133, 133, 133, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});
var cocorahsStyle5Sq = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(115, 223, 255, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});
var cocorahsStyle6Sq = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(0, 112, 255, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});
var cocorahsStyle7Sq = new Style({
    image: new RegularShape({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 38, 115, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});

var cocorahsStyleHighlightSq = new Style({
    image: new RegularShape({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 255, 255, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 245, 245, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4
    })
});

var cocorahsStyleDynSq = {
    'Severely Dry': cocorahsStyle1Sq,
    'Moderately Dry': cocorahsStyle2Sq,
    'Mildly Dry': cocorahsStyle3Sq,
    'Near Normal': cocorahsStyle4Sq,
    'Mildly Wet': cocorahsStyle5Sq,
    'Moderately Wet': cocorahsStyle6Sq,
    'Severely Wet': cocorahsStyle7Sq,
}

//----CMOR Styles----
var cmorStyle0 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(110, 110, 110, 0)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 0)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});
var cmorStyle1 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(186, 110, 110, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(130, 0, 0, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});
var cmorStyle2 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(234, 146, 146, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(250, 0, 0, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});
var cmorStyle3 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(232, 188, 112, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(230, 170, 45, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});
var cmorStyle4 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(221, 221, 221, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(187, 187, 187, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});
var cmorStyle5 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(113, 200, 105, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 170, 0, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});
var cmorStyle6 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(111, 135, 232, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 40, 255, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});
var cmorStyle7 = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(186, 121, 228, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(130, 0, 220, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});

var cmorStyleHighlight = new Style({
    image: new RegularShape({
        fill: new Fill({
            color: 'rgba(0, 255, 255, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 245, 245, 1)',
            width: 2
        }),
        points: 4,
        radius: 10,
        angle: Math.PI / 4,
    })
});

var cmorStyle = {
    'SeverelyDry': cmorStyle1,
    'ModeratelyDry': cmorStyle2,
    'MildlyDry': cmorStyle3,
    'NearNormal': cmorStyle4,
    'MildlyWet': cmorStyle5,
    'ModeratelyWet': cmorStyle6,
    'SeverelyWet': cmorStyle7,
}

var cmorStyleMt = {
    'Severely_Dry': cmorStyle1,
    'Moderately_Dry': cmorStyle2,
    'Mildly_Dry': cmorStyle3,
    'Near_Normal': cmorStyle4,
    'Mildly_Wet': cmorStyle5,
    'Moderately_Wet': cmorStyle6,
    'Severely_Wet': cmorStyle7,
}

var cmorStyle0Cir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 255, 0, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});
var cmorStyle1Cir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(115, 0, 0, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 1
        })
    })
});
var cmorStyle2Cir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(215, 48, 39, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 1
        })
    })
});
var cmorStyle3Cir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(252, 141, 89, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 1
        })
    })
});
var cmorStyle4Cir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(133, 133, 133, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 1
        })
    })
});
var cmorStyle5Cir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(115, 223, 255, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 1
        })
    })
});
var cmorStyle6Cir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 255, 255, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});
var cmorStyle7Cir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 38, 115, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 1)',
            width: 1
        })
    })
});

var cmorStyleHighlightCir = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 255, 255, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 245, 245, 1)',
            width: 1
        })
    })
});

var cmorStyleCir = {
    'SeverelyDry': cmorStyle1Cir,
    'ModeratelyDry': cmorStyle2Cir,
    'MildlyDry': cmorStyle3Cir,
    'NearNormal': cmorStyle4Cir,
    'MildlyWet': cmorStyle5Cir,
    'ModeratelyWet': cmorStyle6Cir,
    'SeverelyWet': cmorStyle7Cir,
}

var cmorStyleMtCir = {
    'Severely_Dry': cmorStyle1Cir,
    'Moderately_Dry': cmorStyle2Cir,
    'Mildly_Dry': cmorStyle3Cir,
    'Near_Normal': cmorStyle4Cir,
    'Mildly_Wet': cmorStyle5Cir,
    'Moderately_Wet': cmorStyle6Cir,
    'Severely_Wet': cmorStyle7Cir,
}

//---- Grasscast map colors
var styleRedGC = new Style({
    fill: new Fill({
        color: 'rgba(255, 10, 10, 0.5)'
    }),
});
var styleOrangeGC = new Style({
    fill: new Fill({
        color: 'rgba(255, 116, 61, 0.5)'
    }),
});
var styleYellowGC = new Style({
    fill: new Fill({
        color: 'rgba(255, 255, 0, 0.5)'
    }),
});
var styleLimegreenGC = new Style({
    fill: new Fill({
        color: 'rgba(0, 255, 0, 0.5)'
    }),
});
var styleLightBlueGC = new Style({
    fill: new Fill({
        color: 'rgba(0, 255, 255, 0.5)'
    }),
});
var styleBlueGC = new Style({
    fill: new Fill({
        color: 'rgba(0, 128, 255, 0.5)'
    }),
});
var styleDarkBlueGC = new Style({
    fill: new Fill({
        color: 'rgba(0, 0, 204, 0.5)'
    }),
});
var styleWhiteGC = new Style({
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0.5)'
    }),
});
var defStyleGC = new Style({
    stroke: new Stroke({
        color: '#ff0000',
        width: 2
    })
});



//----USDM Styles----
var styleUsdmD0 = new Style({
    fill: new Fill({
        color: 'rgba(255, 255, 0, 1)'
    }),
});

var styleUsdmD1 = new Style({
    fill: new Fill({
        color: 'rgba(252, 211, 127, 1)'
    }),
});

var styleUsdmD2 = new Style({
    fill: new Fill({
        color: 'rgba(255, 170, 0, 1)'
    }),
});

var styleUsdmD3 = new Style({
    fill: new Fill({
        color: 'rgba(230, 0, 0, 1)'
    }),
});

var styleUsdmD4 = new Style({
    fill: new Fill({
        color: 'rgba(115, 0, 0, 1)'
    }),
});

var styleUsdmD0Outline = new Style({
    fill: new Fill({
        color: 'rgba(0, 0, 0, 0)'
    }),
    stroke: new Stroke({
        color: 'rgba(255, 255, 0, 1)',
        width: 2
    }),
});

var styleUsdmD1Outline = new Style({
    fill: new Fill({
        color: 'rgba(0, 0, 0, 0)'
    }),
    stroke: new Stroke({
        color: 'rgba(252, 211, 127, 1)',
        width: 2
    }),
});

var styleUsdmD2Outline = new Style({
    fill: new Fill({
        color: 'rgba(0, 0, 0, 0)'
    }),
    stroke: new Stroke({
        color: 'rgba(255, 170, 0, 1)',
        width: 2
    }),
});

var styleUsdmD3Outline = new Style({
    fill: new Fill({
        color: 'rgba(0, 0, 0, 0)'
    }),
    stroke: new Stroke({
        color: 'rgba(230, 0, 0, 1)',
        width: 2
    }),
});

var styleUsdmD4Outline = new Style({
    fill: new Fill({
        color: 'rgba(0, 0, 0, 0)'
    }),
    stroke: new Stroke({
        color: 'rgba(115, 0, 0, 1)',
        width: 2
    }),
});

var styleUsdmHide = new Style({
    fill: new Fill({
        color: 'rgba(0, 0, 0, 0)'
    }),
});

var styleUsdmMask = new Style({
    fill: new Fill({
        color: 'rgba(255, 255, 255, 1)'
    }),
    stroke: new Stroke({
        color: 'rgba(255, 255, 255, 1)',
        width: 1
    })
});


/*var usdmStyle = {
    '0': styleUsdmD0,
    '1': styleUsdmD1,
    '2': styleUsdmD2,
    '3': styleUsdmD3,
    '4': styleUsdmD4
}*/

var usdmStyle = {
    '0': styleUsdmD0,
    '1': styleUsdmD1,
    '2': styleUsdmD2,
    '3': styleUsdmD3,
    '4': styleUsdmD4
}

var usdmStyleOutline = {
    '0': styleUsdmD0Outline,
    '1': styleUsdmD1Outline,
    '2': styleUsdmD2Outline,
    '3': styleUsdmD3Outline,
    '4': styleUsdmD4Outline
}

var styleUsdmD0Pnt = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 255, 0, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleUsdmD1Pnt = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(252, 211, 127, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleUsdmD2Pnt = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 170, 0, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleUsdmD3Pnt = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(230, 0, 0, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleUsdmD4Pnt = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(115, 0, 0, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleUsdmNoDataPnt = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(128, 128, 128, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleUsdmNonePnt = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 255, 255, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var usdmStylePnt = {
    '1': styleUsdmD0Pnt,
    '2': styleUsdmD1Pnt,
    '3': styleUsdmD2Pnt,
    '4': styleUsdmD3Pnt,
    '5': styleUsdmD4Pnt,
    '6': styleUsdmNonePnt,
    '7': styleUsdmNoDataPnt
}

var styleDraClimate = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 255, 0, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleDraHydro = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 0, 255, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleVdaPhoto = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 0, 0, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var styleStationHighlight = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 255, 255, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(0, 245, 245, 1)',
            width: 1
        })
    })
});

var styleStationHighlightAlt = new Style({
    image: new Circle({
        radius: 7,
        fill: new Fill({
            color: 'rgba(192, 192, 192, 1)'
        }),
        stroke: new Stroke({
            color: 'rgba(128, 128, 128, 1)',
            width: 1
        })
    })
});

var cntyStyle = new Style({
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 1)',
        width: 2
    })
});

var tribal_land_style = new Style({
    fill: new Fill({
        color: '#008000'
    })
});

var fed_land_style = new Style({
    fill: new Fill({
        color: '#F08080'
    })
});

var clusterStyle = new Style({
    stroke: new Stroke({
        color: 'rgba(255, 0, 0, 1)',
        width: 2
    })
});

var rma_style = new Style({
    stroke: new Stroke({
        color: '#00dd00',
        width: 2
    })
});

var state_style_2 = new Style({
    stroke: new Stroke({
        color: '#a9a9a9',
        width: 2
    })
});

var stationsDefaultStyle = new Style({
    image: new Circle({
        radius: 2,
        fill: new Fill({
            color: 'rgba(0, 255, 0, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })

});

var stationsHighlightStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 255, 255, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 200, 200, 1)',
            width: 1
        })
    })

});

var stationsSelectedStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 0, 0, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(192, 0, 0, 1)',
            width: 1
        })
    })

});

var stationsZoomDefaultStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 255, 0, 1)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var circleStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(110, 110, 110, 0)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 0)',
            width: 1
        })
    })
});

var circleFF0000 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FF0000',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var circle00FF00 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#00FF00',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var circle0000FF = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#0000FF',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var circleFF00FF = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FF00FF',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var circle00FFFF = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#00FFFF',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var circleFFFF00 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FFFF00',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});


//----Water Watch Styles----
var waterwatchStyle0 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 255, 255, 0)',
        }),
        stroke: new Stroke({
            color: 'rgba(0, 0, 0, 1)',
            width: 1
        })
    })
});

var waterwatchStyle1 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 0, 0, 1)',
        })
    })
});
var waterwatchStyle2 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(177, 33, 33, 1)',
        })
    })
});
var waterwatchStyle3 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 164, 0, 1)',
        })
    })
});
var waterwatchStyle4 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 255, 0, 1)',
        })
    })
});
var waterwatchStyle5 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(64, 223, 208, 1)',
        })
    })
});
var waterwatchStyle6 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(0, 0, 255, 1)',
        })
    })
});
var waterwatchStyle7 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(1, 1, 1, 1)',
        })
    })
});

var waterwatchStyle = {

    '0': waterwatchStyle0,
    '1': waterwatchStyle1,
    '2': waterwatchStyle2,
    '3': waterwatchStyle3,
    '4': waterwatchStyle4,
    '5': waterwatchStyle5,
    '6': waterwatchStyle6,
    '7': waterwatchStyle7,

};


//---Precip Outlook Styles----
var pcpOutAbv33 = new Style({
    fill: new Fill({
        color: 'rgba(150, 207, 128, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutAbv40 = new Style({
    fill: new Fill({
        color: 'rgba(179, 217, 171, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutAbv50 = new Style({
    fill: new Fill({
        color: 'rgba(72, 174, 56, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutAbv60 = new Style({
    fill: new Fill({
        color: 'rgba(57, 124, 94, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutAbv70 = new Style({
    fill: new Fill({
        color: 'rgba(0, 142, 64, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutAbv80 = new Style({
    fill: new Fill({
        color: 'rgba(40, 85, 61, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutAbv90 = new Style({
    fill: new Fill({
        color: 'rgba(40, 85, 23, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});
var pcpOutBel33 = new Style({
    fill: new Fill({
        color: 'rgba(240, 212, 147, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutBel40 = new Style({
    fill: new Fill({
        color: 'rgba(215, 166, 76, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutBel50 = new Style({
    fill: new Fill({
        color: 'rgba(186, 108, 50, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutBel60 = new Style({
    fill: new Fill({
        color: 'rgba(155, 80, 49, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutBel70 = new Style({
    fill: new Fill({
        color: 'rgba(147, 70, 57, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutBel80 = new Style({
    fill: new Fill({
        color: 'rgba(128, 64, 0, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutBel90 = new Style({
    fill: new Fill({
        color: 'rgba(80, 48, 48, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});

var pcpOutEc33 = new Style({
    fill: new Fill({
        color: 'rgba(175, 174, 175, 0)',
    }),
    stroke: new Stroke({
        color: 'rgba(192, 192, 192, 0)',
        width: 1
    })
});



var trendsStyle = {

    '-1': new Style({
        image: new Circle({
            radius: 2,
            fill: new Fill({
                color: 'rgba(255, 0, 0, 1)',
            }),
            stroke: new Stroke({
                color: 'rgba(255, 255, 255, 1)',
                width: 1
            })
        })
    }),
    '0': new Style({
        image: new Circle({
            radius: 2,
            fill: new Fill({
                color: 'rgba(162, 162, 162, 1)',
            }),
            stroke: new Stroke({
                color: 'rgba(255, 255, 255, 1)',
                width: 1
            })
        })
    }),
    '1': new Style({
        image: new Circle({
            radius: 2,
            fill: new Fill({
                color: 'rgba(0, 0, 255, 1)',
            }),
            stroke: new Stroke({
                color: 'rgba(255, 255, 255, 1)',
                width: 1
            })
        })
    })

};

var trendsStyleZoom = {

    '-1': new Style({
        image: new Circle({
            radius: 5,
            fill: new Fill({
                color: 'rgba(255, 0, 0, 1)',
            }),
            stroke: new Stroke({
                color: 'rgba(255, 255, 255, 1)',
                width: 1
            })
        })
    }),
    '0': new Style({
        image: new Circle({
            radius: 5,
            fill: new Fill({
                color: 'rgba(162, 162, 162, 1)',
            }),
            stroke: new Stroke({
                color: 'rgba(255, 255, 255, 1)',
                width: 1
            })
        })
    }),
    '1': new Style({
        image: new Circle({
            radius: 5,
            fill: new Fill({
                color: 'rgba(0, 0, 255, 1)',
            }),
            stroke: new Stroke({
                color: 'rgba(255, 255, 255, 1)',
                width: 1
            })
        })
    })

};


//Area Percent USDM
var stylePercent0 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#ffffff',
    }),
});

var stylePercent1 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#feebe2',
    }),
});

var stylePercent2 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#fbb4b9',
    }),
});

var stylePercent3 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#f768a1',
    }),
});

var stylePercent4 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#c51b8a',
    }),
});

var stylePercent5 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#7a0177',
    }),
});

//Area DSCI
var styleDsci0 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#ffffff',
    }),
});

var styleDsci1 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#ffffb2',
    }),
});

var styleDsci2 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#fecc5c',
    }),
});

var styleDsci3 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#fd8d3c',
    }),
});

var styleDsci4 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#f03b20',
    }),
});

var styleDsci5 = new Style({
    stroke: new Stroke({
        color: '#aaaaaa',
        width: 1
    }),
    fill: new Fill({
        color: '#bd0026',
    }),
});

//----Station SPI Style----
var pntSpiStyle0 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#aaa',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle1 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#820000',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle2 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#BE0000',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle3 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FA0000',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle4 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FA8228',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle5 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#E6AF2D',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle6 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FFFFFF',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle7 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#00AA00',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle8 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#0028FF',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle9 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#8200DC',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle10 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#A000C8',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

var pntSpiStyle11 = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FA00FA',
        }),
        stroke: new Stroke({
            color: '#393939',
            width: 1
        })
    })
});

//Station styles
var stationCocorahsStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#00FF00',
        }),
        stroke: new Stroke({
            color: '#228B22',
            width: 1
        })
    })
});

var stationAcisStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FF0000',
        }),
        stroke: new Stroke({
            color: '#B22222',
            width: 1
        })
    })
});

var stationHcdnStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#0000FF',
        }),
        stroke: new Stroke({
            color: '#00008B',
            width: 1
        })
    })
});

var stationRawsStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FFFF00',
        }),
        stroke: new Stroke({
            color: '#DAA520',
            width: 1
        })
    })
});

var stationScanStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FF00FF',
        }),
        stroke: new Stroke({
            color: '#4B0082',
            width: 1
        })
    })
});

var stationSnotelStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#00FFFF',
        }),
        stroke: new Stroke({
            color: '#48D1CC',
            width: 1
        })
    })
});

var stationWellsStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#FF8C00',
        }),
        stroke: new Stroke({
            color: '#cc7000',
            width: 1
        })
    })
});

var stationReservoirsStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: '#008000',
        }),
        stroke: new Stroke({
            color: '#004d00',
            width: 1
        })
    })
});

var stationHiddenStyle = new Style({
    image: new Circle({
        radius: 5,
        fill: new Fill({
            color: 'rgba(255, 255, 255, 0.0)',

        }),
        stroke: new Stroke({
            color: 'rgba(255, 255, 255, 0.0)',
            width: 1
        })
    })
});

var styleBorderUsdmCounty = new Style({
    stroke: new Stroke({
        color: '#000000',
        width: 0.5
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderUsdmMajRivers = new Style({
    stroke: new Stroke({
        color: '#19afff',
        width: 1.5
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleUsdmLakes = new Style({
    stroke: new Stroke({
        color: '#19afff',
        width: 1.5
    }),
    fill: new Fill({
        color: '#8dd6fc',
    }),
});

var styleBorderUsdmState = new Style({
    stroke: new Stroke({
        color: '#000000',
        width: 3
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleBorderRefUsdmState = new Style({
    stroke: new Stroke({
        color: '#000000',
        width: 1.5
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleHideBorderUsdmState = new Style({
    stroke: new Stroke({
        color: 'rgba(255, 255, 255, 0)',
        width: 0
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleOverlayUsdmState = new Style({
    stroke: new Stroke({
        color: 'rgba(255, 255, 255, 0)',
        width: 2
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 0)',
    }),
});

var styleHideOverlayUsdmState = new Style({
    stroke: new Stroke({
        color: 'rgba(255, 255, 255, 1)',
        width: 4
    }),
    fill: new Fill({
        color: 'rgba(255, 255, 255, 1)',
    }),
});

var styleFille002673 = new Style({
    stroke: new Stroke({
        color: 'rgba(255, 255, 255, 0)',
        width: 1
    }),
    fill: new Fill({
        color: '#002673',
    }),
});



export {usdmStyle}