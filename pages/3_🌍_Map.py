import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Map")
st.markdown("This interactive dashboard supports the exploration of trends of the locations involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as filter locations by the number of incidents.")

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)
df.incident_zip = pd.to_numeric(df['incident_zip'], errors="coerce")

alleghenyCounty = pd.read_csv("data/zipcodes_AlleghenyCounty.csv")
zipcodes = set(alleghenyCounty["ZIPCODE"])
filtered_df = df[df["incident_zip"].isin(zipcodes)]


location = pd.read_csv("data/zipcodes_latlon.csv")

merge = pd.merge(filtered_df, location[["ZIP", "LAT", "LNG"]], how = "left", left_on = "incident_zip", right_on = "ZIP")
merge = merge.dropna(subset=['LAT'])
df_cleaned = merge.rename(columns = {"LNG": "LON"})
print(df_cleaned) #cleaned data with zip and lat and long added to the dataset

# Dataset with the amount of cases in each zipcode
cases = df_cleaned.groupby("incident_zip").size().reset_index(name = "case_count")
print(cases)



# Filters
st.subheader("Filters")
col1, col2 = st.columns(2)

# Date range
min_time = df_cleaned["death_date_and_time"].min().to_pydatetime() # Finding the minimum year value
max_time = df_cleaned["death_date_and_time"].max().to_pydatetime() # Finding the maximum year value

sel_time = col1.slider("Range", min_value=min_time, max_value=max_time, value=(min_time, max_time))
print(sel_time)

# Number of cases
min_cases = cases['case_count'].min()
max_cases = cases['case_count'].max()
selected_cases = col2.slider('Select number of cases range', min_cases, max_cases, (min_cases, max_cases))

# Dynamically updated size
def sizes_change(df_cleaned, start_date, end_date):
    filtered_data = df_cleaned[(df_cleaned['death_date_and_time'] >= start_date) & (df_cleaned['death_date_and_time'] <= end_date)]

    cases = filtered_data.groupby("incident_zip").size().reset_index(name = "case_count")

    sizes = cases['case_count'].tolist()
    sizes = [count ** 2 for count in cases['case_count']]

    return sizes


print(sizes_change(df_cleaned, sel_time[0], sel_time[1]))






st.subheader("Map")

red = 255
green = 0
blue = 0
alpha = 0.25

color = (red, green, blue, alpha)

st.map(df_cleaned, 
    #    latitude = "LAT",
    #    longitude = "LON",
       color = color,
       size = sizes_change(df_cleaned, sel_time[0], sel_time[1]),
    #    size = 2000,
       use_container_width = True)
