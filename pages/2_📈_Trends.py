import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv("D:\Semester1@CMU\InteractiveDataScience\HW3a\data\overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

st.title("Trends")
st.markdown("This interactive dashboard supports the exploration of trends of the primary drugs involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as select the number of top ranked primary drugs to show.")

# Set start time and end time
start_datetime, end_datetime = st.slider(
    "Select time range", 
    value=(df['death_date_and_time'].dt.date.min(), df['death_date_and_time'].dt.date.max()),
    #format='YY/MM/DD HH:mm:ss' 
)

# Filter based on death_date
filtered_df = df[(df['death_date_and_time'].dt.date >= start_datetime) & (df['death_date_and_time'].dt.date <= end_datetime)]

# Implementing the number widget
top_n = st.number_input("Select the number of top prevalent drugs", min_value=1, max_value=20, value=8)

# Group filtered data by year and primary drug 
yearly_counts = filtered_df.groupby([filtered_df['death_date_and_time'].dt.to_period('Y'), 'combined_od1']).size().reset_index(name='counts')
yearly_counts['year'] = yearly_counts['death_date_and_time'].dt.strftime('%Y')

top_drugs = yearly_counts.groupby('combined_od1')['counts'].sum().nlargest(top_n).index # Only choose top drugs

filtered_yearly_counts = yearly_counts[yearly_counts['combined_od1'].isin(top_drugs)]

# Visualization
charts = alt.Chart(filtered_yearly_counts).mark_area().encode(
    x=alt.X('year:O', title='Year of Death'), 
    y=alt.Y('counts:Q', title='Number of Overdoses'),
    color='combined_od1:N',
    row=alt.Row('combined_od1:N', title='Primary Drug')
).properties(height=200, width=600)

st.altair_chart(charts, use_container_width=True)