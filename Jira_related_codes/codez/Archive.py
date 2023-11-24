# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

name = json.load(open("projectName.json", "r"))

def archive(a):
    url = "/rest/api/3/project/{a}/archive"

    auth = HTTPBasicAuth("", "")

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "POST",
        url,
        headers=headers,
        auth=auth
    )

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

for p_name in name:
    archive(p_name)
