# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = ""

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

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
value = response.json()["values"]

result = []

for values in value:
  result.append(values)

total = response.json()['total']
maxresult = response.json()['maxResults']


for i in range(maxresult, total , maxresult):

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
with open("values.json", "w") as f:
   json.dump(result, f, indent=4)
print("done")  