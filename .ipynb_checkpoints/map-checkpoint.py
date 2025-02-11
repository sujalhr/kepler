import streamlit as st
import pandas as pd
import keplergl
import json

def main():
    st.title('Kepler GL Map Visualization')

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        # Read the CSV file
        try:
            df = pd.read_csv(uploaded_file)
            
            # Display column names to help user select correct columns
            st.write("Columns in your dataset:")
            st.write(df.columns.tolist())

            # Allow user to select lat and lng columns
            lat_col = st.selectbox("Select lat Column", df.columns)
            lng_col = st.selectbox("Select lng Column", df.columns)

            # Visualization type selection
            viz_type = st.selectbox("Select Visualization Type", 
                                    ["Heatmap", "Point", "Arc", "Cluster"])

            # Create map configuration based on selection
            if st.button('Generate Map'):
                # Create Kepler GL map
                map_1 = keplergl.KeplerGl(height=600)
                
                # Add data to the map
                map_1.add_data(data=df, name='uploaded_data')

                # Configure map based on visualization type
                config = {
                    "version": "v1",
                    "config": {
                        "visState": {
                            "layers": [
                                {
                                    "id": f"{viz_type.lower()}_layer",
                                    "type": viz_type.lower(),
                                    "config": {
                                        "dataId": "uploaded_data",
                                        "label": f"{viz_type} Layer",
                                        "columns": {
                                            "lat": lat_col,
                                            "lng": lng_col
                                        },
                                        "isVisible": True,
                                        "visConfig": {
                                            "opacity": 0.8,
                                            "colorRange": {
                                                "colors": [
                                                    "#0000FF",  # Blue (cold)
                                                    "#00FF00",  # Green (medium)
                                                    "#FF0000"   # Red (hot)
                                                ]
                                            },
                                            "radius": 20  # Adjust the radius
                                        }
                                    }
                                }
                            ]
                        }
                    }
                }

                # Apply configuration
                map_1.config = config

                # Display the map
                st.write(map_1)

                # Option to download the map configuration
                map_config = json.dumps(map_1.config, indent=2)
                st.download_button(
                    label="Download Map Configuration",
                    data=map_config,
                    file_name="kepler_map_config.json",
                    mime="application/json"
                )

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.error("Please ensure your CSV file is correctly formatted")

    else:
        st.info("Please upload a CSV file to begin")

    # Additional information
    st.sidebar.header("How to Use")
    st.sidebar.info("""
    1. Upload a CSV file with lat and lng columns
    2. Select the correct lat and lng columns
    3. Choose a visualization type
    4. Click 'Generate Map' to create your visualization
    """)

if __name__ == "__main__":
    main()

# Installation instructions
"""
Required packages:
pip install streamlit pandas keplergl

Run the app:
streamlit run app.py
"""