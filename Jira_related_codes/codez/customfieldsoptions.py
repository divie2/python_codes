# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import json
from dotenv import load_dotenv
import os 

# Load environment variables from .env file
load_dotenv(override=True)

# Access environment variables
api_key = os.getenv('Api_key')
username = os.getenv('Username')
ur = os.getenv('Url')

# change reason custom_field id
id="customfield_10007"

# customfield contextId
contextId=10107

auth = HTTPBasicAuth(username,api_key)

url = f"{ur}{id}/context/{contextId}/option"

option = {id :[]}


headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

options = response.json()["values"]
# print(f"{id } :  {options}")


for i in options:
 option[id].append(i)

    # option.append({id[id]:i})
# option = {id :{"id":i["id"],'value':i['value']}}


with open("options.json", "a") as f:
   json.dump(option, f, indent=4)
print("done") 