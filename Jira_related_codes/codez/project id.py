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

name = json.loads(response.text)
# print(name[0]['id'])

for i in name:
    print({i['id'] : i['name']})
# for i in name:
#     a.append(name)
#     print(a)

# # This code sample uses the 'requests' library:
# # http://docs.python-requests.org
# import requests
# from requests.auth import HTTPBasicAuth
# import json

# url = "https://your-domain.atlassian.net/rest/api/3/project"

# auth = HTTPBasicAuth("email@example.com", "<api_token>")

# headers = {
#   "Accept": "application/json"
# }

# response = requests.request(
#    "GET",
#    url,
#    headers=headers,
#    auth=auth
# )

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))