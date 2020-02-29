import os
import sqlite3
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt

def parse(url):
	try:
		parsed_url_components = url.split('//')
		sublevel_split = parsed_url_components[1].split('/', 1)
		domain = sublevel_split[0].replace("www.", "")
		return domain
	except IndexError:
		print("URL format error!")


data_path = os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
files = os.listdir(data_path)
history_db = os.path.join(data_path, 'history')
c = sqlite3.connect(history_db)
cursor = c.cursor()
select_statement = "SELECT urls.url, urls.title, urls.visit_count, datetime(visits.visit_time/1000000-11644473600,'unixepoch') FROM urls, visits WHERE urls.id = visits.url ORDER BY visits.visit_time;"  # time isn't according to the time zone.
cursor.execute(select_statement)

results = cursor.fetchall()
for search in results:
	print(search)

"""
sites_count = {} #dict makes iterations easier :D

for url, count in cursor:
	url = parse(url)
	if url in sites_count:
		sites_count[url] += 1
	else:
		sites_count[url] = 1
sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))

plt.bar(range(len(sites_count_sorted)), sites_count_sorted.values(), align='edge')
plt.xticks(rotation=45)
plt.xticks(range(len(sites_count_sorted)), sites_count_sorted.keys())
plt.show()


"""
results = cursor.fetchall()
for search in results:
	print(search)




