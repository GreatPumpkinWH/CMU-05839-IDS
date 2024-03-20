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

## Questions of part a

### 1.Did you notice any interesting patterns or trends in the dataset?
When we choose primary drug as Alcohol, at earlier years there is a noticeable upward trend, particularly from around 2010 to 2017 where there is a significant rise.The year 2017 appears to have the highest count of records, which stands out as a peak in overdoses. After 2017, there is an apparent decline in the number of overdoses. Maybe some form of intervention or change in circumstances that affected these numbers.

### 2.Was it possible to understand how the dataset was different in the earlier years versus the more recent years? 

#### 1.If so, what were some differences?  

#### 2。If not, how would you suggest changing the dashboard to make differences easier to find?
Yes, it was. For example, we compare the age distribution of 2007-2010 with the age distribution of 2020-2023, we can found that although both histograms show a similar distribution with a peak in the middle age ranges, the peak age of 2020-2023 is smaller than the peak age of 2007-2010.And the number of overdose records for the Black race has increased when comparing earlier years to more recent years.

### 3.Did you discover any filters that demonstrated big differences from the overall dataset among the demographics (such as age, race, or gender)?

Doxepin. The age distribution of overall dataset is that the number of male  involved in fatal accidental overdoses in Allegheny County is much higher than the number of female. But when we select primary drug as Doxepin, we can see that the number of female is higher than the number of male.

### 4.Are there any other features you wish were present in your dashboard to either make discovery easier or to explore alternative aspects of the dataset?

Yes. We can add incident zip code to integrate a map to visualize geographic patterns which could reveal regional trends or hotspots. And I think adding the total number of people by gender, race, and age for different years can indeed provide a more comprehensive view of the dataset. 

## Questions of part b
### 1.
I discovered that in addition to the few drugs that account for the majority of fatalities, many other substances actually contribute to a very small number of deaths annually, as depicted by very low and flat graphs in the dataset, and the changes in this segment are not very pronounced in the chart, suggesting that our analysis may ought to primarily focus on the few categories of drugs that constitute the majority of fatalities. Additionally, the trends in the number of deaths caused by different drugs may vary significantly, some of which is stale while other may crease or decrease apparently.
### 2.

Yes, there are some differences.
Comparing the situation in earlier years with more recent ones, we observe that the annual fatality numbers for some drugs have remained relatively stable, such as Clonazepam and Methadone. However, for others, there was a noticeable increase in recent years compared to earlier ones, such as Fentanyl and Cocaine. Additionally, compared to earlier years, recent years have seen a decline in the number of fatalities for some substances, such as Alcohol.

### 3.

Age: We can compute mean death age of each year. Maybe we can find some interesting trend of this feature.
Combined_OD2: This variable could indicate the secondary drug involved in an overdose incident. Analyzing primary and secondary drugs together could provide insights into common drug combinations that result in overdoses.

## Questions of part c
### 1.
There appears to be a high concentration of overdose incidents in the central urban areas around Pittsburgh, particularly in neighborhoods like North Side and South Side. And the suburban areas surrounding Pittsburgh seem to have fewer overdose incidents, as evidenced by the smaller circles or lack of circles in those areas on the map

### 2.
Key differences in the earlier years versus the more recent years are that the overdose incidents have transitioned from being relatively spread out geographically to becoming much more concentrated and densely packed within the central Pittsburgh neighborhoods in recent years.

### 3.
Demographic filters such as age, gender, race/ethnicity could reveal important trends and help identify high-risk populations for targeted intervention efforts.
Drug type filter can help explore overdoses that inform targeted harm reduction strategies.