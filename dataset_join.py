# joining all three csv files into one final file for analysis purpose

import csv

# state name and abbreviation
# source: https://gist.github.com/rogerallen/1583593
us_state_to_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

# scraped
sc = dict()
with open('sc_content_full.csv') as f1:
    c = csv.reader(f1)
    counter = 1
    for i in c:
        if counter != 1:
            name = i[1]
            time = i[2]
            con = i[3]
            sc[name] = [time, con]
        counter += 1

# pop api
api = dict()
with open('api_content_full.csv') as f2:
    c = csv.reader(f2)
    counter = 1
    for i in c:
        if counter != 1:
            name = i[0].replace(' town', '').replace(' city', '').replace(' village', '').split(', ')[0]
            pop = i[1]
            state = i[0].replace(' town', '').replace(' city', '').replace(' village', '').split(', ')[1]
            if state in us_state_to_abbrev:
                state = us_state_to_abbrev[state]
            # deal with repeated name issue
            if name in api:
                # get the most popular one instead of nonname one
                if int(api[name][0]) < int(pop):
                    api[name] = [pop, state]
            else:
                api[name] = [pop, state]
        counter += 1

# cost of living
col = dict()
with open('cost_of_living.csv') as f3:
    c = csv.reader(f3)
    counter = 1
    for i in c:
        if counter != 1:
            name = i[0]
            state = i[1]
            ind = i[2]
            col[name] = [ind, state]
        counter += 1

# combining
result = dict()
for i in col:
    if i in sc and i in api and col[i][1] == api[i][1]:
        # time, congestion level, population, cost of living
        result[i] = [sc[i][0], sc[i][1], api[i][0], col[i][0]]

# output to csv
with open('DSCI510_Song_Combined.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['City Name', 'Traffic Time', 'Congestion Level', 'Population', 'Cost of Living'])
    for k in result:
        writer.writerow([k] + result[k])