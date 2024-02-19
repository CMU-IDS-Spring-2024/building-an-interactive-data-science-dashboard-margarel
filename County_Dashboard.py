import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

st.header("_Allegheny County_ :red[Fatal Accidental Overdoses]")

st.markdown("A series of interactive dashboards to support exploration of the Allegheny County Fatal Accidental Overdoses dataset.")

st.markdown('This data is published from the [Western Pennsylvania Regional Data Center](https://data.wprdc.org/dataset/allegheny-county-fatal-accidental-overdoses).  It describes fatal accidental overdose incidents in Allegheny County, denoting age, gender, race, drugs present, zip code of incident and zip code of residence.')

st.markdown("This is the raw data used to produce the dashboard:")

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

st.dataframe(df)

st.markdown("Please choose a dashboard using the sidebar on the left.")
