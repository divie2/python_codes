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
option={}


# Open and read the JSON file
with open('results/customcontexts.json', 'r') as json_file:
    data = json.load(json_file)

for customfield_id, context in data.items():
    # print(customfield_id.keys())
  

    # customfield contextId
    contextId= context
    customfield= customfield_id

    auth = HTTPBasicAuth(username,api_key)

    url = f"{ur}{customfield}/context/{contextId}/option"

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


    for i in options:
        if customfield in option.keys():
            option[customfield]['option(s)'].extend([i])
        else:
            option[customfield] = ({"option(s)" : [i]})

        # print(customfield,i)
with open("results/options2.json", "w") as f:
    json.dump(option, f, indent=4)

print(option)
print("done") 
  