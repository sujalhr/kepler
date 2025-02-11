import streamlit as st
import pandas as pd
from keplergl import KeplerGl

# Step 1: Read the CSV file
# Ensure 'places.csv' exists in the same directory and has 'lat', 'lng', and 'lead_time' columns.
df = pd.read_csv("places.csv")

# Step 2: Create Kepler.gl configuration for the heatmap
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
                        "color": [255, 153, 31],  # Orange color for the layer
                        "columns": {
                            "lat": "lat",
                            "lng": "lng"
                        },
                        "isVisible": True,
                        "visConfig": {
                            "radius": 25,  # Controls the spread of heat
                            "intensity": 1,  # Controls heatmap intensity
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
                            "threshold": 0.1  # Minimum value to consider
                        },
                        "visualChannels": {
                            "weightField": {"name": "lead_time", "type": "integer"},
                            "weightScale": "linear"
                        }
                    }
                }
            ]
        }
    }
}

# Step 3: Initialize KeplerGl Map with Data and Configuration
map_ = KeplerGl(height=400, data={"Lead Time Heatmap": df}, config=config)

# Step 4: Display Map in Streamlit
st.title("Heatmap of Lead Time")
st.write("Visualizing the Lead Time Heatmap using Kepler.gl in Streamlit.")

# Embed the Kepler.gl map into the Streamlit app
st.components.v1.html(map_._repr_html_(), height=800)
