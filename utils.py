import json

def save_geojson(places, path):
    coords = [[places[i].lon, places[i].lat] for i in path]
    geojson = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coords
            },
            "properties": {
                "name": "Optimized Tour Route"
            }
        }]
    }
    with open("output/route.geojson", "w") as f:
        json.dump(geojson, f, indent=2)