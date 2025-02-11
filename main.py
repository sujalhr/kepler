import streamlit as st
import pandas as pd
from keplergl import KeplerGl

# Sample Data
data = {
    "latitude": [37.77, 34.05, 40.71],
    "longitude": [-122.42, -118.24, -74.00],
    "magnitude": [3.4, 4.2, 2.8],
    "place": ["San Francisco", "Los Angeles", "New York"]
}
df = pd.DataFrame(data)

# Initialize Kepler.gl Map
map_1 = KeplerGl()
map_1.add_data(data=df, name="Sample Data")

# Save Kepler.gl map as HTML
map_1.save_to_html(file_name="kepler_map.html")

# Display Kepler.gl map in Streamlit
st.title("Kepler.gl Map in Streamlit")
st.markdown("Below is the Kepler.gl visualization rendered as HTML.")

# Read and Display the Kepler.gl HTML file
with open("kepler_map.html", "r") as f:
    html_content = f.read()
st.components.v1.html(html_content, height=700)
