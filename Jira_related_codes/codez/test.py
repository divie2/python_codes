import requests
from requests.auth import HTTPBasicAuth
import json


url = "/rest/api/3/field"

auth = HTTPBasicAuth("", "")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
result=[]

ten = json.loads(response.text)

for i in ten:
    if i['custom'] == True:
        result.append(i)


with open("results.json", "w") as file:
    json.dump(result,file, indent=4)        



