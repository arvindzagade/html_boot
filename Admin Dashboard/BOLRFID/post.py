import json
import requests
url='http://localhost:4000/r'
payload=20
payld = json.dumps(payload)
ret = requests.post(url,data = {'Sampledata':payload})
#ret = requests.post(url,data=payld)
#ret = requests.post(url,params=payld)
print(ret.url)
