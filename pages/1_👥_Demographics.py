import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Demographics")
st.markdown("This interactive dashboard supports the exploration of the demographics (age, gender, and race) of the people involved in fatal accidental overdoses in Allegheny County.  You can filter by the year of the overdose incident, as well as the primary drug present in the incident.")

df = pd.read_csv("D:\Semester1@CMU\InteractiveDataScience\HW3a\data\overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

# to make the visualizations more meaningful, we unabbreviate the race and sex columns

df['race'] = df['race'].str.replace('W','White')
df['race'] = df['race'].str.replace('B','Black')
df['race'] = df['race'].str.replace('H|A|I|M|O|U','Other', regex=True) #there are very few non-white/back decedents in this dataset, so we merge the remaining categories to 'other'
df.dropna(subset = ['race'], inplace=True)  #get rid of nulls

df['sex'] = df['sex'].str.replace('M','Male')
df['sex'] = df['sex'].str.replace('F','Female')

st.subheader("Filters")

#insert filters here
#type of 'case_year' is int, we need to convert it to make better interactions and visualiazations
df['year_date'] = pd.to_datetime((df['case_year']).astype(str) + '-06-01')
min_year = df['year_date'].dt.year.min()
max_year = df['year_date'].dt.year.max()

#Year Range Slider
year_range = st.slider(
    'Select Year Range', 
    min_value=min_year, 
    max_value=max_year, 
    value=(min_year, max_year)
)

#Primary Drug Selection
selected_drugs = st.multiselect(
    'Select Primary Drug',
    options=list(df['combined_od1'].unique()),
    default=list(df['combined_od1'].unique())
)

filtered_df = df[(df['year_date'].dt.year >= min_year) & (df['year_date'].dt.year <= max_year)]
if selected_drugs:
    filtered_df = filtered_df[filtered_df['combined_od1'].isin(selected_drugs)]

st.subheader("Visualizations")

#insert visualizations here

#Year Histogram
year_histogram = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X('year(year_date):O', title='Year'),
    y='count():Q',
    color=alt.Color('year(year_date):O', scale=alt.Scale(scheme='category20b')),
    tooltip=[alt.Tooltip('year(year_date):O', title='Year'), 'count()']
).properties(
    title='Year Distribution of Fatal Accidental Overdoses',
    width=800,  
    height=400
)
st.altair_chart(year_histogram, use_container_width=True)

#Age Histogram
age_histogram = alt.Chart(filtered_df).mark_bar().encode(
    x='age:Q',
    y='count():Q',
    color=alt.Color('age:Q', scale=alt.Scale(scheme='blues')),#higher age with deeper color
    tooltip=['age', 'count()']
).properties(
    title='Age Distribution of Fatal Accidental Overdoses'
)
st.altair_chart(age_histogram, use_container_width=True)

#Gender Bar Chart
gender_bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='sex:N',
    y='count():Q',
    color=alt.Color('sex:N', scale=alt.Scale(domain=['Male', 'Female'],range=['lightblue', 'pink'])),#set the color for each gender, make it more intuitive
    tooltip=['sex', 'count()']
).properties(
    title='Gender Distribution of Fatal Accidental Overdoses'
)
st.altair_chart(gender_bar_chart, use_container_width=True)

#Race Bar Chart
race_bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x='race:N',
    y='count():Q',
    color=alt.Color('race:N', scale=alt.Scale(domain=['Black', 'Other','White'],range=['black', 'tan', 'whitesmoke'])),#set colors according to the race
    tooltip=['race', 'count()']
).properties(
    title='Race Distribution of Fatal Accidental Overdoses'
)
st.altair_chart(race_bar_chart, use_container_width=True)


