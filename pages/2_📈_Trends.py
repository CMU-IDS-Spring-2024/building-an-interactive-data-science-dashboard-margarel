import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv("data/overdose_data_092223.csv")
df.death_date_and_time = pd.to_datetime(df.death_date_and_time)

st.title("Trends")
st.markdown("This interactive dashboard supports the exploration of trends of the primary drugs involved in fatal accidental overdoses in Allegheny County.  You can filter by the date of the overdose incident, as well as select the number of top ranked primary drugs to show.")

# Filters
st.subheader("Filters")

col1, col2 = st.columns(2)

# Date Range Slider with minimum and maximum years
min_time = df["death_date_and_time"].min().to_pydatetime() # Finding the minimum year value
max_time = df["death_date_and_time"].max().to_pydatetime() # Finding the maximum year value


sel_time = col1.slider("Range", min_value = min_time, max_value = max_time, value = (min_time, max_time))

# st.write(filter_df)


# Number Input Widget to determine most popular drug in the year range
num_drugs = col2.number_input("How many top drugs?", min_value=1, max_value=20, value=8, step=1)

# Filtered data based on year range and selected drugs
filtered_df = df[(df["death_date_and_time"] >= sel_time[0]) & (df["death_date_and_time"] <= sel_time[1])]
drug_counts = filtered_df["combined_od1"].value_counts().reset_index()
drug_counts.columns = ["Drug", "Count"]
top_drugs = drug_counts.head(num_drugs)


# col2.write(top_drugs)




# Visualizations
st.subheader("Visualizations")

# Number of incidents for each drug each year
drug_year_counts = filtered_df.groupby([filtered_df["death_date_and_time"].dt.year, "combined_od1"]).size().reset_index(name = "count")

charts = []
max_count = drug_year_counts["count"].max()

for drug in top_drugs["Drug"]:
    drug_data = drug_year_counts[drug_year_counts["combined_od1"] == drug]
    
    chart = alt.Chart(drug_data).mark_area().encode(
        x = alt.X("death_date_and_time:O", title = "Fatal Overdoses per Year"),
        # y=alt.Y("count:Q", title="Count"), # Without the same y-axis
        y = alt.Y("count:Q", title = "Count", scale = alt.Scale(domain = (0, max_count), nice = False)), # With the same y-axis
        color = alt.Color("combined_od1:N", legend = None),
        # row = alt.Row("count:Q", title = "Count", header = alt.Header(labelAngle = 0)),
        # column = alt.Column("death_date_and_time:O", title = "Fatal Overdoes per Year")
    ).properties(
        width = 600,
        height = 100,
        title = drug
    )
    
    charts.append(chart)

combined_chart = alt.vconcat(*charts)
st.altair_chart(combined_chart, use_container_width=True)