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

# Date Range Slider
min_time = df['death_date_and_time'].min().to_pydatetime() # Finding the minimum year value
max_time = df['death_date_and_time'].max().to_pydatetime() # Finding the maximum year value


sel_time = col1.slider('Range', min_value = min_time, max_value = max_time, value = (min_time, max_time))

# st.write(filter_df)


# Drug Selector
st.subheader("Top Prevalent Drugs")

# Number input widget for selecting the number of drug area charts to display
num_drugs = st.number_input("Select Number of Top Drugs", min_value=1, max_value=20, value=8, step=1)

# Calculate the count of incidents for each drug within the selected date range
filtered_df = df[(df['death_date_and_time'] >= sel_time[0]) & (df['death_date_and_time'] <= sel_time[1])]
drug_counts = filtered_df['combined_od1'].value_counts().reset_index()
drug_counts.columns = ['Drug', 'Count']
top_drugs = drug_counts.head(num_drugs)

# Display top prevalent drugs
st.write("Top Prevalent Drugs within Selected Date Range:")
st.write(top_drugs)




# Visualizations
st.subheader("Visualizations")

# Compute the count of incidents for each drug for each year
drug_year_counts = filtered_df.groupby([filtered_df['death_date_and_time'].dt.year, 'combined_od1']).size().reset_index(name='count')

# Create a list to store the individual charts
charts = []

# Iterate over each drug to create an area chart
for drug in top_drugs['Drug']:
    # Filter data for the current drug
    drug_data = drug_year_counts[drug_year_counts['combined_od1'] == drug]
    
    # Create area chart for the current drug
    chart = alt.Chart(drug_data).mark_area().encode(
        x='death_date_and_time:O',
        y='count:Q',
        color=alt.Color('combined_od1:N', legend=None),  # Each drug will have a unique color
        tooltip=['death_date_and_time:O', 'count:Q']
    ).properties(
        width=500,
        height=300,
        title=drug
    )
    
    # Append the chart to the list
    charts.append(chart)

# Combine individual charts into a single row using Altair's Row() function
combined_chart = alt.vconcat(*charts)

# Display the combined chart
st.altair_chart(combined_chart, use_container_width=True)