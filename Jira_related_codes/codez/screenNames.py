import requests
from requests.auth import HTTPBasicAuth
import json

result = []

url = "/rest/api/3/screens"

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

a = response.json()["values"]

for i in a:
  result.append(i["name"])

total = response.json()['total']
maxresult = response.json()['maxResults']
print(f"total = {total}")


for i in range(maxresult, total , maxresult):
  print(f"total2 = {i}")

  # count += 1
  query = {
      
      'startAt': i,

    }

  response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query,
    auth=auth
  )
  b = response.json()["values"]

  for i in b:
    result.append(i["name"])
  # print(f'appending {count}')
#   result.extend(response.json()["name"])
print(f"total = {total}")    
with open("Cloudscreens.json", "w") as f:
   json.dump(result, f, indent=4)
print("done")  