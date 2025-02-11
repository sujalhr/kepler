import streamlit as st
import pandas as pd
from keplergl import KeplerGl

# Streamlit App Title
st.title("Interactive Location Mapping with Kepler.gl")

# Create input fields for user to enter location details
col1, col2 = st.columns(2)
with col1:
    latitude = st.number_input("Enter Latitude", min_value=-90.0, max_value=90.0, step=0.01)
    magnitude = st.number_input("Enter Magnitude", min_value=0.0, max_value=10.0, step=0.1)

with col2:
    longitude = st.number_input("Enter Longitude", min_value=-180.0, max_value=180.0, step=0.01)
    place = st.text_input("Enter Place Name")

# Button to create map
if st.button("Create Map"):
    # Create DataFrame with user input
    data = {
        "latitude": [latitude],
        "longitude": [longitude],
        "magnitude": [magnitude],
        "place": [place]
    }
    df = pd.DataFrame(data)
    
    # Initialize Kepler.gl Map
    map_1 = KeplerGl()
    map_1.add_data(data=df, name="User Location")
    
    # Save Kepler.gl map as HTML
    map_1.save_to_html(file_name="kepler_map.html")
    
    # Read and Display the Kepler.gl HTML file
    with open("kepler_map.html", "r") as f:
        html_content = f.read()
    
    # Display the map
    st.markdown("## Generated Map")
    st.components.v1.html(html_content, height=700)

# Optional: Add some instructions or description
st.sidebar.markdown("""
### How to Use
1. Enter latitude and longitude coordinates
2. Add magnitude (if applicable)
3. Specify the place name
4. Click 'Create Map' to generate your visualization
""")