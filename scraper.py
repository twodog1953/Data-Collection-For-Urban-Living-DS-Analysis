# scraping process
from bs4 import BeautifulSoup
import requests
import csv

def csv_write(file_name, lst):
    with open(file_name, 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['Country Rank', 'City Name', 'Time lost(Hour)', 'Congestion Level'])
        for k in range(len(lst[0])):
            temp = []
            for o in range(len(lst)):
                temp.append(lst[o][k])
            writer.writerow(temp)

def scrape(url):
    content = requests.get(url)
    soup = BeautifulSoup(content.content, 'html.parser')
    # all columns
    country_rank = soup.find_all('td', class_="CountryRankingTable__td CountryRankingTable__td--country-rank")
    time_lost = soup.find_all('td', class_="CountryRankingTable__td CountryRankingTable__td--time-lost")
    city_name = soup.find_all('td', class_="CountryRankingTable__td CountryRankingTable__td--city-name")
    congestion_level = soup.find_all('div', class_="CountryRankingTable__congestion-value")
    tot_lst = [country_rank, city_name, time_lost, congestion_level]

    organized_lst = []
    counter = 0
    for j in tot_lst:
        organized_lst.append([])
        for i in j:
            if counter != 2:
                organized_lst[-1].append(i.get_text())
            else:
                temp = i.get_text().split()
                # print(temp)
                organized_lst[-1].append(temp[0])
        counter += 1
    # csv_write(path + '/' + 'sc_content_full.csv', organized_lst)
    return organized_lst

def partial(url):
    full = scrape(url)
    new_lst = []
    for i in full:
        new_lst.append([])
        for j in range(5):
            new_lst[-1].append(i[j])
    return new_lst

def sup_command(*args):
    one = args[0]
    if one == '--scrape':
        partial_lst = partial(link)
        csv_write('sc_content_short.csv', partial_lst)
    elif one == '--static':
        two = args[1]
        full_lst = scrape(link)
        csv_write(str(two) + '/' + 'sc_content_full.csv', full_lst)

# exe
link = 'https://www.tomtom.com/en_gb/traffic-index/united-states-of-america-country-traffic/'
# a = scrape(link)

# terminal
import sys
user_input = sys.argv
if len(user_input) == 2:
    in_1 = user_input[1]
    sup_command(in_1)
elif len(user_input) == 3:
    in_1 = user_input[1]
    in_2 = sys.argv[2]
    sup_command(in_1, in_2)
elif len(user_input) == 1:
    # default mode
    labels = ['Country Rank', 'City Name', 'Time lost(Hour)', 'Congestion Level']
    default_lst = partial(link)
    temp_1 = ''
    for i in labels:
        temp_1 += str(i) + '|'
    print(temp_1)
    for j in range(len(default_lst[0])):
        temp = ''
        for k in default_lst:
            temp += str(k[j]) + '|'
        print(temp)
    print('----------')
    print("This is just a sampling. Only 5 entries are shown here. ")
    default_out = scrape(link)
    csv_write('sc_content_full.csv', default_out)
else:
    print('Wrong number of input! ')

