# for api request from the US Census website

import urllib.request
import json
import csv

def csv_write(file_name, lst):
    with open(file_name, 'w') as out_file:
        writer = csv.writer(out_file)
        # writer.writerow(['NAME', 'POP', 'state', 'place'])
        for k in lst:
            writer.writerow(k)


def scrape(url):
    a = urllib.request.urlopen(url)
    content = json.loads(a.read().decode())
    return content


def partial(link):
    full = scrape(link)
    new_lst = []
    for j in range(6):
        new_lst.append(full[j])
    return new_lst


def sup_command(*args):
    one = args[0]
    if one == '--scrape':
        partial_lst = partial(url)
        csv_write('api_content_short.csv', partial_lst)
    elif one == '--static':
        two = args[1]
        full_lst = scrape(url)
        csv_write(str(two) + '/' + 'api_content_full.csv', full_lst)

# para
key = 'f293aea7f6a0d7a48e92f5dd76bf4fb1a002d1b0'
# for all population in all cities in all states
url = "https://api.census.gov/data/2019/pep/population?get=NAME,POP&for=place:*&in=state:*"

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
    # labels = ['NAME', 'POP', 'state', 'place']
    default_lst = partial(url)
    temp_1 = ''
    # for i in labels:
    #     temp_1 += str(i) + '|'
    # print(temp_1)
    for j in range(len(default_lst[0])):
        temp = ''
        for k in default_lst:
            temp += str(k[j]) + '|'
        print(temp)
    print('----------')
    print("This is just a sampling. Only 5 entries are shown here. ")
    default_out = scrape(url)
    csv_write('sc_content_full.csv', default_out)
else:
    print('Wrong number of input! ')
