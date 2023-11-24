# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://your-domain.atlassian.net/rest/api/3/field/{fieldId}/context/{contextId}/option"

auth = HTTPBasicAuth("email@example.com", "<api_token>")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "options": [
    {
      "disabled": false,
      "id": "10001",
      "value": "Scranton"
    },
    {
      "disabled": true,
      "id": "10002",
      "value": "Manhattan"
    },
    {
      "disabled": false,
      "id": "10003",
      "value": "The Electric City"
    }
  ]
} )

response = requests.request(
   "PUT",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))