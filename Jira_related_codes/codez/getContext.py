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
j = {}

# Open and read the JSON file
with open('results/customfieldkey.json', 'r') as json_file:
    data = json.load(json_file)

for customkeys in data :

    url = f'{ur}{customkeys}/context'
    auth = HTTPBasicAuth(username,api_key)
  

    headers = {
    "Accept": "application/json"
    }

    response = requests.request(
    "GET",
    url,
    headers=headers,
    auth=auth
    )
    context = response.json()['values']

    for i in context:
        j.update( {customkeys: i['id'] } )
        # print(i['id'])

   

with open("results/customcontexts.json", "w") as f:
    json.dump(j, f, indent=4)


  




