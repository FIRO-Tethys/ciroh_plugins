from ciroh_plugins.nwmps.gauges import NWMPSGaugesSeries


def test_create_flood_events_skips_placeholder_stage_values():
    flood_data = {
        "stageUnits": "ft",
        "categories": {
            "action": {"stage": -9999},
            "minor": {"stage": 12},
        },
    }

    shapes, annotations = NWMPSGaugesSeries.create_flood_events(flood_data)

    assert len(shapes) == 1
    assert len(annotations) == 1
    assert shapes[0]["y0"] == 12
    assert annotations[0]["text"] == "12 ft - minor"


def test_create_flood_events_skips_all_invalid_stage_values():
    flood_data = {
        "stageUnits": "ft",
        "categories": {
            "action": {"stage": " -9999.0 "},
            "minor": {"stage": ""},
            "moderate": {"stage": None},
        },
    }

    shapes, annotations = NWMPSGaugesSeries.create_flood_events(flood_data)

    assert shapes == []
    assert annotations == []
