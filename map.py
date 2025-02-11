from keplergl import KeplerGl
import pandas as pd

# File path to the CSV file
csv_file = "places.csv"

# Read the CSV file into a Pandas DataFrame
try:
    df = pd.read_csv(csv_file)
    print("CSV file loaded successfully!")
except FileNotFoundError:
    print(f"Error: File '{csv_file}' not found.")
    exit()

# Check if required columns exist
required_columns = {"lat", "lng", "place"}
if not required_columns.issubset(df.columns):
    print(f"Error: CSV file must contain columns: {', '.join(required_columns)}")
    exit()

# Initialize Kepler.gl map
map_1 = KeplerGl(height=600)

# Add data from the CSV file to the map
map_1.add_data(data=df, name="Locations Data")

# Save the map to an HTML file
output_file = "kepler_csv_map.html"
map_1.save_to_html(file_name=output_file)

print(f"Map has been saved as '{output_file}'. Open it in your browser.")
