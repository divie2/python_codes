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

custom_field_option_type = []
customfieldkey= []
context_custom = {}
option={}

# url to get customfields
url = f"{ur}"

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

customfield = response.json()

# get custom field keys from response.json()
for i in customfield:

    # select customfields with type option 
    if i['custom'] == True and i['schema']['type'] == "option":

        custom_field_option_type.append(i['key'])
       
# Save customfield keys in customfieldkey.json
with open("results/customfieldkey.json", "w") as f:
   json.dump(custom_field_option_type, f, indent=4)
print("........Custom_fieldkey Secured........") 


# Open and read the custom field key file
with open('results/customfieldkey.json', 'r') as json_file:
    data = json.load(json_file)

# get custom field keys from data
for customkeys in data :

    # url for getting custom field context 
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

    # update context_custom with customfield keys and customfield context ids
    for i in context:
        context_custom.update( {customkeys: i['id'] } )

# save custom field context in a file
with open("results/customcontexts.json", "w") as f:
    json.dump(context_custom, f, indent=4)
print("........Custom_field context Secured........")


# Open and read the custom field context file
with open('results/customcontexts.json', 'r') as json_file:
    data = json.load(json_file)

# Get all customfield keys and customfield context ids from custom field context file
for customfield_id, context in data.items():

    
    contextId= context
    customfield= customfield_id

    auth = HTTPBasicAuth(username,api_key)

    # url to get customfields options 
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

    # save all options from the customfields in the option variable
    for i in options:
        if customfield in option.keys():
            option[customfield]['option(s)'].extend([i])
        else:
            option[customfield] = ({"option(s)" : [i]})

# save the customfields as keys and their options as items
with open("results/options3.json", "w") as f:
    json.dump(option, f, indent=4)
print("........done........file saved") 
