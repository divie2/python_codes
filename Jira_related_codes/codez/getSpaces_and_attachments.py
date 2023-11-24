
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

result = []

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
total = json.loads(response.text)


result.append(total)



key_to_check =  "_links"


y = total.get(key_to_check)

print(y)


exit()  

while key_to_check in total:
    url2 = f"https://alluvium-hq.atlassian.net{y['next']}"
    
    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url2,
    headers=headers,
    auth=auth
    )
    total2 = json.loads(response.text)
    result.append(total2)
                
with open("Resul.json" , 'a') as f:
    json.dump(total2, f, indent= 4)
