from keplergl import KeplerGl
import pandas as pd

# Load the CSV file
csv_file = "places.csv"
df = pd.read_csv(csv_file)

# Initialize Kepler.gl map
map_1 = KeplerGl(height=600)

# Add data to the map
map_1.add_data(data=df, name="Lead Time Heatmap")

# Configure the map to display a heatmap
config = {
    "version": "v1",
    "config": {
        "visState": {
            "layers": [
                {
                    "id": "heatmap-layer",
                    "type": "heatmap",
                    "config": {
                        "dataId": "Lead Time Heatmap",
                        "label": "Heatmap of Lead Time",
                        "color": [255, 153, 31],  # Orange
                        "columns": {
                            "lat": "lat",
                            "lng": "lng"
                        },
                        "isVisible": True,
                        "visConfig": {
                            "radius": 25,  # Adjust radius as needed
                            "intensity": 1,  # Adjust intensity
                            "colorRange": {
                                "name": "Uber Viz Sequential",
                                "type": "sequential",
                                "category": "Uber",
                                "colors": [
                                    "#FFE4E4",
                                    "#FFC4C4",
                                    "#FF9494",
                                    "#FF6464",
                                    "#FF0000"
                                ]
                            },
                            "threshold": 0.1,
                        },
                    },
                    "visualChannels": {
                        "weightField": {"name": "lead_time", "type": "integer"},
                        "weightScale": "linear"
                    }
                }
            ],
            "interactionConfig": {},
            "layerBlending": "normal",
        },
        "mapState": {"bearing": 0, "latitude": 20, "longitude": 0, "pitch": 0, "zoom": 2},
        "mapStyle": {"styleType": "dark"}
    }
}

# Apply the configuration
map_1.config = config

# Save the map to an HTML file
output_file = "kepler_lead_time_heatmap.html"
map_1.save_to_html(file_name=output_file)

print(f"Heatmap saved as '{output_file}'. Open it in your browser.")
