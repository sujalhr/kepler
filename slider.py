import streamlit as st
import pandas as pd
from keplergl import KeplerGl

# Step 1: Read the CSV file
# Ensure 'places.csv' exists in the same directory and has 'lat', 'lng', 'lead_time', and 'week' columns.
df = pd.read_csv("places.csv")

# Step 2: Add a Streamlit slider for filtering based on the 'week' column
st.title("Heatmap of Lead Time")
st.write("Visualizing the Lead Time Heatmap using Kepler.gl in Streamlit.")

# Create the slider
selected_week = st.slider(
    label="Select Week",
    min_value=int(df['week'].min()),
    max_value=int(df['week'].max()),
    step=1,
    value=int(df['week'].min())  # Default to the first week
)

# Filter the dataframe based on the selected week
filtered_df = df[df['week'] == selected_week]

# Step 3: Create Kepler.gl configuration for the heatmap
config = {
    "version": "v1",
    "config": {
        "visState": {
            "layers": [
                {
                    "id": "heatmap-layer",
                    "type": "heatmap",
                    "config": {
                        "dataId": "Filtered Heatmap",
                        "label": f"Heatmap for Week {selected_week}",
                        "color": [255, 153, 31],  # Orange color for the layer
                        "columns": {
                            "lat": "lat",
                            "lng": "lng"
                        },
                        "isVisible": True,
                        "visConfig": {
                            "radius": 5,  # Controls the spread of heat
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

# Step 4: Initialize KeplerGl Map with Filtered Data and Configuration
map_ = KeplerGl(height=400, data={"Filtered Heatmap": filtered_df}, config=config)

# Step 5: Display Map in Streamlit
# Embed the Kepler.gl map into the Streamlit app
st.components.v1.html(map_._repr_html_(), height=800)

# Optional: Show the filtered dataframe below the map
st.subheader(f"Data for Week {selected_week}")
st.dataframe(filtered_df)
