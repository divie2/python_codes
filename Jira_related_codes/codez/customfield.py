import requests
import json 

# Replace with your Jira instance URL and project key
jira_url = "https://perm-test.atlassian.net/"
project_key = "TPCC3W"

# Define the API endpoint for retrieving custom fields
api_endpoint = f"{jira_url}/rest/api/2/issue/createmeta"

# Set up your Jira credentials (use API token for security)
auth = ("", "")

# Parameters to specify the project key and expand fields
params = {
    "projectKeys": project_key,
    "expand": "projects.issuetypes.fields",
}

result = {}

try:
    response = requests.get(api_endpoint, params=params, auth=auth)

    if response.status_code == 200:
        data = response.json()
        
        # Extract custom fields from the response
        custom_fields = data['projects'][0]['issuetypes'][0]['fields']
      
        for i in custom_fields.values():
           
           for j in i["schema"]:
               if j == 'custom':
                result.update({project_key : i['schema']})
              
        

        

        
        # Write the JSON result to a file
        with open('custom_fields.json', 'w') as json_file:
            json.dump(result, json_file, indent=4)

        print("JSON result saved to custom_fields.json")
    else:
        print(f"Error: {response.status_code} - {response.text}")

except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")        