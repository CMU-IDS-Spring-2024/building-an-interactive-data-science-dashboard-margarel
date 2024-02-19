import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.title("Demographics")
st.markdown("This interactive dashboard supports the exploration of the demographics (age, gender, and race) of the people involved in fatal accidental overdoses in Allegheny County.  You can filter by the year of the overdose incident, as well as the primary drug present in the incident.")

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

# to make the visualizations more meaningful, we unabbreviate the race and sex columns

df['race'] = df['race'].str.replace('W','White')
df['race'] = df['race'].str.replace('B','Black')
df['race'] = df['race'].str.replace('H|A|I|M|O|U','Other', regex=True) #there are very few non-white/back decedents in this dataset, so we merge the remaining categories to 'other'
df.dropna(subset = ['race'], inplace=True)  #get rid of nulls

df['sex'] = df['sex'].str.replace('M','Male')
df['sex'] = df['sex'].str.replace('F','Female')



# Filters
st.subheader("Filters")

col1, col2 = st.columns(2)

# Year Widget
min_year = df['case_year'].min() # Finding the minimum year value
max_year = df['case_year'].max() # Finding the maximum year value


sel_years = col1.slider('Select Year Range', min_value = min_year, max_value = max_year, value = (min_year, max_year))

# st.write(filter_df)


# Drug Selector
drugs = sorted(df['combined_od1'].unique())
sel_drugs = col2.multiselect('Select Primary Drug(s)', options = drugs)



filter_df = df[(df['case_year'] >= sel_years[0]) & (df['case_year'] <= sel_years[1])]
if sel_drugs:
    filter_df = filter_df[filter_df['combined_od1'].isin(sel_drugs)]

# st.write(filter_df)

# Visualizations
st.subheader("Visualizations")

#insert visualizations here
case_year = filter_df['case_year'].value_counts().reset_index()
case_year.columns = ['Year', 'Incident Count']

# Year Histogram
year_hist = alt.Chart(case_year).mark_bar().encode(
    x='Year:O',
    y='Incident Count:Q'
).properties(
    title='Distribution of Fatal Accidental Overdoses by Year',
    width=600,
    height=400
)

st.write(year_hist)

#col3, col4, col5 = st.columns(3)

# Age Histogram
age_hist = alt.Chart(filter_df).mark_bar().encode(
    y=alt.Y('age:Q', bin=alt.Bin(maxbins=30), title='Age'),
    x=alt.X('count():Q', title='Incident Count'),
    tooltip=['count()']
).properties(
    title='Distribution of Fatal Accidental Overdoses by Age',
    width=600,
    height=400
)

st.write(age_hist)


# Gender Bar Chart
gender_counts = filter_df['sex'].value_counts().reset_index()
gender_counts.columns = ['Gender', 'Incident Count']

gender_bar_chart = alt.Chart(gender_counts).mark_bar().encode(
    y='Gender:N',
    x='Incident Count:Q'
).properties(
    title='Count of Fatal Accidental Overdoses by Gender',
    width=600,
    height=400
)

st.write(gender_bar_chart)


# Race Bar Chart
race_counts = filter_df['race'].value_counts().reset_index()
race_counts.columns = ['Race', 'Incident Count']

race_bar_chart = alt.Chart(race_counts).mark_bar().encode(
    y='Race:N',
    x='Incident Count:Q'
).properties(
    title='Count of Fatal Accidental Overdoses by Race',
    width=600,
    height=400
)

st.write(race_bar_chart)

##############3
#sorted(df['combined_od1'].unique())

# Count occurrences of each drug
drug_counts = filter_df['combined_od1'].value_counts().reset_index()
drug_counts.columns = ['Drug', 'Count']

# Select the top 10 drugs
top_10_drugs = drug_counts.head(10)

# Sort the top 10 drugs by count in descending order
top_10_drugs = top_10_drugs.sort_values(by='Count', ascending=False)

# Create a bar chart using Altair
top_10_drugs_chart = alt.Chart(top_10_drugs).mark_bar().encode(
    x=alt.X('Drug:N', sort='-y'),
    y='Count:Q'
).properties(
    title='Top 10 Most Used Drugs',
    width=600,
    height=400
)

# Display the chart
st.write(top_10_drugs_chart)