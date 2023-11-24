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

query = {
  'jql': 'attachments is not EMPTY'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
# print(response.json())

total = response.json()['total']

for i in range(50,total,50):


    query = {
    'jql': 'attachments is not EMPTY',
    'startAt': 50,

    }


    response = requests.request(
    "GET",
    url,
    headers=headers,
    params=query,
    auth=auth
    )
    print(response.json(), sort_keys=True, indent=4, separators=(",", ": "))