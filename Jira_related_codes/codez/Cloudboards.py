# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
app= []
url = "/rest/agile/1.0/board"

auth = HTTPBasicAuth("", "")


headers = {
  "Accept": "application/json",
  
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)
result = response.json()["values"]
print(result)
# exit()
for i in result:
   print(i["name"])
   
   app.append(i["name"])


with open("test.json", "w") as f:
   json.dump(app, f, indent=4)
print("done") 