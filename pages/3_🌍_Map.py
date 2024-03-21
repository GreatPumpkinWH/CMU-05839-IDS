import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("Map")
st.markdown("This interactive dashboard supports the exploration of trends of the locations involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as filter locations by the number of incidents.")

df = pd.read_csv("d:/Semester1@CMU/InteractiveDataScience/HW3a/data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)
df.incident_zip = pd.to_numeric(df['incident_zip'], errors='coerce')

# Load the ZIP code latitude and longitude mapping
zipcodes_latlon = pd.read_csv('d:/Semester1@CMU/InteractiveDataScience/HW3a/data/zipcodes_latlon.csv')

filter_container = st.container()

#Make filter in the same row
col1, col2 = filter_container.columns(2)

with col1:
    start_datetime, end_datetime = st.slider("Date Range",
                                             min_value=df['death_date_and_time'].dt.date.min(),
                                             max_value=df['death_date_and_time'].dt.date.max(), 
                                             value=(df['death_date_and_time'].dt.date.min(), df['death_date_and_time'].dt.date.max())
                                             )

filtered_df = df[(df['death_date_and_time'].dt.date >= start_datetime) & (df['death_date_and_time'].dt.date <= end_datetime)]

# Aggregate incident counts by ZIP code
incident_counts = filtered_df.groupby('incident_zip').size().reset_index(name='incident_count')
count_max = incident_counts['incident_count'].max()
count_min = incident_counts['incident_count'].min()

with col2:
    incident_count_range = st.slider("How many cases", count_min, count_max, (count_min, count_max))

# Filter by incident count range (assuming incident_count_range is a tuple (min, max))
incident_counts = incident_counts[(incident_counts['incident_count'] >= incident_count_range[0]) & (incident_counts['incident_count'] <= incident_count_range[1])]

# Merge with ZIP code latitude and longitude data
incident_locations = pd.merge(incident_counts, zipcodes_latlon, left_on='incident_zip', right_on='ZIP', how='inner')

# Check if incident_locations is empty
if incident_locations.empty:
    st.warning("No locations found for the selected filters.")
else:
    scaling_factor = 10  # You may need to adjust this depending on your data

    # Add a new column to the DataFrame for the circle size
    incident_locations['circle_size'] = incident_locations['incident_count'] * scaling_factor

    # Create the pydeck layer with proportional circles
    layer = pdk.Layer(
        "ScatterplotLayer",
        incident_locations,
        get_position=['LNG', 'LAT'],
        get_radius='circle_size',  # Use the new circle size
        get_color=[255, 0, 0, 160],  # Use a RGBA color with some transparency
        pickable=True
    )

    # Define the view state for the map
    max_incident_location = incident_locations[incident_locations['incident_count'] == incident_locations['incident_count'].max()]
    # Set initial view state to the location with the most incidents
    view_state = pdk.ViewState(
        latitude=max_incident_location['LAT'].iloc[0],
        longitude=max_incident_location['LNG'].iloc[0],
        zoom=9,
        pitch=0
    )

    # Create the tooltip
    tooltip = {
        "html": "<b>ZIP Code:</b> {incident_zip}<br><b>Incident Count:</b> {incident_count}",
        "style": {
            "backgroundColor": "steelblue",
            "color": "white"
        }
    }

    # Create the pydeck chart
    r = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style='mapbox://styles/mapbox/light-v9',
        tooltip=tooltip
    )

    # Display the pydeck chart in Streamlit
    st.pydeck_chart(r)