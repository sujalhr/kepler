from keplergl import KeplerGl
import pandas as pd

# Load the CSV file with the new 'lead_time' column
csv_file = "places.csv"
df = pd.read_csv(csv_file)

# Initialize Kepler.gl map
map_1 = KeplerGl(height=600)

# Add data to the map
map_1.add_data(data=df, name="Lead Time Heatmap")

# Save the map to an HTML file
output_file = "kepler_heatmap.html"
map_1.save_to_html(file_name=output_file)

print(f"Map with 'lead_time' heatmap saved as '{output_file}'. Open it in your browser.")
