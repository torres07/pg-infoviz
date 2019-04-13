# -*- coding: utf-8 -*-
# @Author: pedrotorres
# @Date:   2019-04-05 13:10:50
# @Last Modified by:   pedrotorres
# @Last Modified time: 2019-04-05 17:33:47

from bs4 import BeautifulSoup
# import urllib2
import csv

url = 'povcal-al-car.html'
html = open(url).read()
soup = BeautifulSoup(html, 'lxml')
table = soup.select_one("div.divCountry")
table_header = soup.select_one("table.oTbl")
table_countries = soup.select_one('div.divCountry')


l_countries = [i.string for i in table_countries.select('div > a')]
qtd_data_p_country = [len(i) for i in table_countries.select('div > table > tbody')]

zipped = zip(l_countries, qtd_data_p_country)

last_column = []
for i, j in zipped:
	for k in range(j):
		last_column.append(i)

headers = [th.contents[0] for th in table_header.select('td > a')][:11]
headers = [headers[0]] + ['DataType'] + headers[1:] + ['Country']

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)

    i = 0
    for row in table.select('tbody tr'):
    	to_wr = []
    	for td in row.find_all('td')[:-1]:
    		to_wr.append(td.text)
    	to_wr.append(last_column[i])
    	i = i + 1
    	# print(to_wr)
    	wr.writerow(to_wr)

    # wr.writerows([[td.text for td in row.find_all('td')[:-1]] for row in table.select('tbody tr')])