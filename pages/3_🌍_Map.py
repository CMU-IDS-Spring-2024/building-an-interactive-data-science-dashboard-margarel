import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Map")
st.markdown("This interactive dashboard supports the exploration of trends of the locations involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as filter locations by the number of incidents.")

st.markdown("Ignore until Assignment 3c")

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)
df.incident_zip = pd.to_numeric(df['incident_zip'], errors='coerce')



