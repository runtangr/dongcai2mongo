import requests
import datetime

now_date = datetime.datetime.now()
now_date_str = now_date.strftime("%Y-%m-%d")
url = "http://10.9.4.29:8058/{0}.txt".format(now_date_str)
r = requests.get(url) 
with open("dongcai_block_data.txt", "wb") as code:
     code.write(r.content)