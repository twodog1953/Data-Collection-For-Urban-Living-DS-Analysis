DSCI 510 Homework 4:

Description: For Homework 4, I have created two datasets in the form of 4 csv file called 'sc_content_full.csv' and 'api_content_full.csv', 'cost_of_living.csv' and 'DSCI510_Song_Combined.csv'. The first three dataset is created using the 3 different data sources listed below (Data Sources Section) in this text file, and the 4th one is obtained by combining the first 3 datasets.  All the datasets will be provided along with the coding scripts. 


Requirements: Following requirements are needed to be satisfied to run this code:

Packages to be installed:
1. Beautiful Soup
2. Urllib
3. Json
5. requests

To install above packages use the following command: pip install -r requirements.txt
'requirements.txt' file has a list of all the necessary packages required to run this code


Data Sources:

1. United States of America traffic in cities (No API, needs scraping from site)
(URL: https://www.tomtom.com/en_gb/traffic-index/united-states-of-america-country-traffic/)
Explanation: I used beautiful soup and json module to scrape from the website and stuff the data in the file 'sc_content_full.csv'. This dataset reflects the general traffic conditions in a list of cities in North America in 2022. There are 7 columns available: country rank, world rank, city, time lost per year, congestion level 2021, change from 2019, change from 2020. For this project, I’ll use the time lost per year and congestion level 2021 columns for my analysis. 


2. Cost of Living in US cities in 2021: (https://advisorsmith.com/data/coli/)
Link to fetch .csv file: "https://advisorsmith.com/wp-content/uploads/2021/02/advisorsmith_cost_of_living_index.csv"
This url directly provides download for the dataset file in the format of .csv file, and its downloaded by direct_dl.py. This dataset will provide living index for different US cities, which will be used by me to combine with traffic data from the first dataset in order to analyze the potential relationship between them. 

3. Population in the US cities (API access)
URL: https://api.census.gov/data/2019/pep/population?get=NAME,POP&for=place:*&in=state:* (use API to access)
Explanation: this API provides the stats about the total population of different US cities. The data is retrieved using requests module and saved as api_content_full.csv. I’ll compare it to the traffic and cost of living data to find correlation between them. 

4. Joined Dataset (from the 3 previous dataset)
Explanation: this data set is obtained by combining all three datasets above to get a uniform dataset that's easy to analyze later. No command is needed. 

Running the code:
The code for 'pop_data_api.py' and 'scraper.py' can be run in three modes: default, scrape and static

Default mode: To run the code in default mode, type command - python3 [scripe name]
In this mode, the dataset designated for downloading will be saved, and the first 5 entries in the file will be printed in the terminal. 

Scrape mode: To run the code in scrape mode, type command python3 [script name] --scrape
In this mode, small samples (first 5 entries) representing all the three datasets are generated and printed. 

Static mode: To run the code in static mode, type command - python3 [script name] --static [save path]
In this mode, the full dataset will be downloaded just like the default mode, but nothing will be printed on terminal. Also, the file will be saved in the path designated in the command instead of in the same path as the script. Note: don't include the name of the file in the command, as its already been taken care of in the code. 
