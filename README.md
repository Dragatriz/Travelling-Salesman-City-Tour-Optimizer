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

## 📁 Project Structure

TSP/
├── tsp.py # Main script
├── places.csv # Sample input file
├── route.geojson # Generated output file
└── README.md # Project documentation


---

## 📥 Input Format

The input file (`places.csv`) must be a CSV with the following columns:

Name,Lat,Lon

perl
Copy
Edit

### 🔍 Example:

```csv
Name,Lat,Lon
Eiffel Tower,48.8584,2.2945
Louvre Museum,48.8606,2.3376
Notre-Dame,48.8529,2.3500
Arc de Triomphe,48.8738,2.2950
🧪 Usage
▶️ Run the program:
bash
Copy
Edit
python tsp.py --csv places.csv --start "Eiffel Tower" --return-trip
✅ Sample Output:
pgsql
Copy
Edit
Optimal tour (returns to start):
1) Eiffel Tower
2) Louvre Museum
3) Notre-Dame
4) Arc de Triomphe
5) Eiffel Tower

Total distance: 12.4 km
Route written to route.geojson

🌍 Visualize Your Route
Open https://geojson.io and drag route.geojson into the map.

Or import it into Google Maps → My Maps → Import.

Or view in any GeoJSON-compatible map viewer or GIS software.

🧱 Requirements
Python 3.x

No external libraries required (uses only Python standard library)

🚀 Future Enhancements (Optional Ideas)
🗺️ Matplotlib-based route plot (scatter + arrows)

🤖 Simulated Annealing or Genetic Algorithm support

🕒 Time window / availability filtering

🌐 Web app or GUI interface

🧪 Unit testing for modules (distance.py, tsp_solver.py, etc.)

👨‍💻 Author
Denis
B.Tech IT Student
Project: TSP City Tour Optimizer
Year: 2025
