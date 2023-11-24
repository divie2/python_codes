import requests
from requests.auth import HTTPBasicAuth
import json
from dotenv import load_dotenv
import os 

# Load environment variables from .env file
load_dotenv(override=True)

# Access environment variables
api_key = os.getenv('Api_key')
username = os.getenv('Username')
ur = os.getenv('Url')

url = f"{ur}"

auth = HTTPBasicAuth(username,api_key)

go = []
app={}
customfieldkey= []

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
customfield = response.json()

for i in customfield:
    # print(i['custom'])
    if i['custom'] == True and i['schema']['type'] == "option":
        # print(i)
        go.append(i['key'])

print(go)        

with open("results/customfieldkey.json", "w") as f:
   json.dump(go, f, indent=4)
print("done") 



