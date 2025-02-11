Project Overview: 

The project focused on developing an interactive heatmap visualization that dynamically ren-
ders geographic data based on user-selected parameters, specifically filtering lead time data by
week.


Key Technical Implementations
•Data Loading:
– Utilized Pandas to read CSV files containing geographic and temporal data.
– Columns included latitude, longitude, lead time, and week information.
•Interactive Filtering Mechanism:
– Implemented a Streamlit slider for week selection.
– Dynamically filtered data based on user-selected week.
– Provided real-time updates to the heatmap visualization.
•Kepler.gl Map Configuration:
– Created custom configuration for a heatmap layer.
– Defined color ranges and intensity parameters.
– Configured weight scaling based on lead time data
