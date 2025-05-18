# 🗺️ Travelling Salesman City-Tour Optimizer

A Python CLI tool that solves the Travelling Salesman Problem (TSP) using a greedy heuristic and 2-opt optimization. Input a list of tourist destinations via CSV and get the most efficient route, with a GeoJSON output for visualizing in Google Maps or any mapping tool.

---

## 🚀 Features

- Reads places from a CSV file (name, latitude, longitude)
- Calculates accurate distance matrix using Haversine formula
- Greedy TSP solver with 2-opt path optimization
- Outputs:
  - Ordered tour in the console
  - Total tour distance
  - GeoJSON route file for visualization
- Optional return-to-start flag
- Clean command-line interface
