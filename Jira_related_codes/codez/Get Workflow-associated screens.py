import requests
import json

base_url = ''
username = ''
password = ''

session = requests.Session()
session.headers.update({'X-Atlassian-Token': 'no-check'})
session.auth = (username, password)

response = session.get(f'{base_url}/rest/api/latest/workflow')

workflows= response.json()

# workflow_name = 'Alluvium Lead Tracking Workflow'

workflow_related_screens = []

for wf in workflows:
    workflow_name = wf['name']
    response = session.get(f'{base_url}/rest/workflowDesigner/latest/workflows?name={workflow_name}')
    
    rjson = response.json()

    for transition in rjson['layout']['transitions']:
        if 'screenName' in transition:
            workflow_related_screens.append(transition['screenName'])

# print(workflow_related_screens)
# a = json.dump(workflow_related_screens)
print("entered")
with open("serverWorkflow-screen.json", "w") as f:
   json.dump(workflow_related_screens, f, indent=4)
print("done")    