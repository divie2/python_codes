# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import os

# Access environment variables
api_key = os.getenv('API_KEY')
username = os.getenv('username')
url = os.getenv('url')

# Use the environment variables in your script


url = f"https://{url}.atlassian.net/rest/api/3/project/DIV/role/10002"

auth = HTTPBasicAuth(username, api_key)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))