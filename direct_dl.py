import requests
import urllib as ur
import csv

url = "https://advisorsmith.com/wp-content/uploads/2021/02/advisorsmith_cost_of_living_index.csv"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

req = requests.get(url, headers=headers)

decoded = req.content.decode('utf-8')

cr = csv.reader(decoded.splitlines(), delimiter=',')
my_list = list(cr)

with open('cost_of_living.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    # writer.writerow(['NAME', 'POP', 'state', 'place'])
    for k in my_list:
        writer.writerow(k)