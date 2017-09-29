import requests

url = ""
r = requests.get(url) 
with open("dongcai_block_data.txt", "wb") as code:
     code.write(r.content)