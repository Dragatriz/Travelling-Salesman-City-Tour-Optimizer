#!/usr/bin/env python3

import csv
import math
import json
import argparse
from collections import namedtuple

Place = namedtuple('Place', ['name', 'lat', 'lon'])

def read_places(csv_file):
    places = []
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            places.append(Place(row['Name'], float(row['Lat']), float(row['Lon'])))
    return places

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def compute_distance_matrix(places):
    n = len(places)
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                dist[i][j] = haversine(places[i].lat, places[i].lon, places[j].lat, places[j].lon)
    return dist

def greedy_tsp(dist_matrix, start_index=0):
    n = len(dist_matrix)
    visited = [False]*n
    path = [start_index]
    visited[start_index] = True
    
    for _ in range(n-1):
        last = path[-1]
        next_city = min((dist_matrix[last][j], j) for j in range(n) if not visited[j])[1]
        path.append(next_city)
        visited[next_city] = True
    return path

def two_opt(path, dist_matrix):
    n = len(path)
    improved = True
    while improved:
        improved = False
        for i in range(1, n - 2):
            for j in range(i + 1, n):
                if j - i == 1:
                    continue
                a, b = path[i - 1], path[i]
                c, d = path[j - 1], path[j % n]
                if dist_matrix[a][c] + dist_matrix[b][d] < dist_matrix[a][b] + dist_matrix[c][d]:
                    path[i:j] = reversed(path[i:j])
                    improved = True
        if not improved:
            break
    return path

def total_distance(path, dist_matrix):
    dist = 0
    for i in range(len(path)-1):
        dist += dist_matrix[path[i]][path[i+1]]
    return dist

def export_geojson(places, path, filename='route.geojson'):
    coordinates = [[places[i].lon, places[i].lat] for i in path]
    geojson = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "geometry": {
                "type": "LineString",
                "coordinates": coordinates
            },
            "properties": {
                "name": "TSP route"
            }
        }]
    }
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(geojson, f, indent=2)

def find_start_index(places, start_name):
    for i, p in enumerate(places):
        if p.name.lower() == start_name.lower():
            return i
    raise ValueError(f"Start place '{start_name}' not found.")

def main():
    parser = argparse.ArgumentParser(description="TSP City Tour Optimizer")
    parser.add_argument('--csv', required=True, help='CSV file with places')
    parser.add_argument('--start', required=True, help='Start place name')
    parser.add_argument('--return-trip', action='store_true', help='Return to start place')
    args = parser.parse_args()

    places = read_places(args.csv)
    dist_matrix = compute_distance_matrix(places)
    start_index = find_start_index(places, args.start)

    path = greedy_tsp(dist_matrix, start_index)
    path = two_opt(path, dist_matrix)

    if args.return_trip:
        path.append(start_index)

    dist = total_distance(path, dist_matrix)

    print("Optimal tour{}:".format(" (returns to start)" if args.return_trip else ""))
    for i, idx in enumerate(path, 1):
        print(f"{i}) {places[idx].name}")
    print(f"Total distance: {dist:.1f} km")

    export_geojson(places, path)
    print("Route written to route.geojson")

if __name__ == '__main__':
    main()
