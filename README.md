# hw3-template

In this assignment, you will adopt the persona of being a data scientist for Allegheny County’s Health Department.  Your goal is to build data science tools to make it easier for the health department to understand trends of an ongoing health crisis:  fatal accidental overdoses from a variety of drugs in the county.  The Western Pennsylvania Regional Data Center publishes a monthly dataset that describes fatal accidental overdose incidents in Allegheny County, denoting age, gender, race, drugs present, zip code of incident and zip code of residence.

This data, downloaded as of September 22, 2023, is located in [data/overdose_data_092223.csv](data/overdose_data_092223.csv)

Through a series of assignments, you will build out a dashboard to support the interactive exploration and analysis of the dataset.  You will use this same repository for Assignments 3a, 3b, and 3c.  

- [ ] For Assignment 3a, Update the provided Streamlit python file, `pages/1_👥_Demographics.py`
- [ ] For Assignment 3b, Update the provided Streamlit python file, `pages/2_📈_Trends.py`
- [ ] For Assignment 3c, Update the provided Streamlit python file, `pages/3_🌍_Map.py`
- [ ] In addition, submit your Github repository URL on Canvas for each of the three assignments.

## Running the Streamlit app

You can execute the Streamlit app by running `streamlit run County_Dashboard.py`

---

## Assignment 3A Questions
1. **Did you notice any interesting patterns or trends in the dataset?**
   1. Overall, there are a few patterns present in the dataset such as: sudden spike of fatal accidents from overdoses in the years 2016 and 2017; most of the overdoses are roughly between early 30s to late 50s; and more than double of the overdose cases are male.
2. **Was it possible to understand how the dataset was different in the earlier years versus the more recent years? If so, what were some differences? If not, how would you suggest changing the dashboard to make differences easier to find?**
   1. Initially, you can tell that there is a spike in cases around 2016 and 2017 where overdose cases more than doubled in count, but nothing exactly points to a change in data collection. If there is a difference in the data, one way to dictate the change in data would be to have another parameter (column) that showcases more information.
3. **Did you discover any filters that demonstrated big differences from the overall dataset among the demographics (such as age, race, or gender)?**
   1. By going through the primary drugs, there were a few interesting deviations. 
   Fentanyl is considered a more recent drug as most of overdose cases started increasing after 2019. While there were some cases of fentanyl overdoses in 2016 and 2017, when there was a highest quantity of overdoses, most of the cases are more recent with 342 overdose cases in 2021.
   Alcohol on the other hand, had more overdose cases before 2019 with 161 incidents in 2017. The average age range is higher than the general population as well with most of the cases being roughly 50 years old while fentanyl's age range was roughly people in their 30s.
4. **Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?**
   1. Due to the large amount of unique drugs, another way to find information would be to have a top used drugs and users can test the difference among the different drugs (i.e. discover information such as fentanyl being a relatively new drug that is common to accidentally overdose on in comparison to other drugs such as heroin or alcohol).

---

## Assignment 3B Questions
1. **Did you notice any interesting patterns or trends in the dataset?**
   1. In comparison to the previous assignment, it was easier to discover what drugs were most popular during what time period as that was the main purpose. It made it easier to understand what was the main cause of fatal accidents. With this setup, it was easier to see patterns and/or a timeline of drug usage (ie. cocaine, alcohol, fentanyl being the most prominent in usage as the years go on and also cases of alprazolam and heroin throughout the years).
2. **Was it possible to understand how the dataset was different in the earlier years versus the more recent years? If so, what were some differences? If not, how would you suggest changing the dashboard to make differences easier to find?**
   1. Yes, it was possible with the dataset to understand how earlier years had different fatal drug overdoses in comparison to more recent years (such as cocaine and alcohol being more present in the earlier years while fentanyl being more present in cases in the more recent years by more than 100+ cases). However, it doesn't showcase whether or not there was a difference in data collection.
3. **Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?**
   1. Looking at the rest of the data, it would be helpful to understand where the cases are coming from and whether or not there is a pattern in location. This could reveal which specific areas have access to what type of drugs and what areas are more concentrated in fatal overdoses.

---

## Assignment 3C Questions
1. **Did you notice any interesting patterns or trends in the dataset?**
   1. 
2. **Was it possible to understand how the dataset was different in the earlier years versus the more recent years? If so, what were some differences?  If not, how would you suggest changing the dashboard to make differences easier to find?**
   1. 
3. **Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?**
   1. 