# This code sample uses the 'requests' library:
# http://docs.python-requests.org

import requests
from requests.auth import HTTPBasicAuth
import json

url = "/rest/api/3/project/search?expand=insight"

auth = HTTPBasicAuth("", "")


headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)


result = []
count = 5
projects_with_dates = response.json()['values']


while count > 0: 
    print(count)
 

    for projects in projects_with_dates:
        
        if projects['insight'].get('lastIssueUpdateTime',"").startswith(f'2023-0{count}'):
            
                result.append({"names":projects['name'], 'keys': projects['key'], 'issuesCount':projects['insight'].get("totalIssueCount", ""),'lastIssueUpdateTime':projects['insight'].get('lastIssueUpdateTime',""), 'style': projects['style']})
            # result.append(projects)

    total = response.json()['total']
    maxresult = response.json()['maxResults']


    for i in range(maxresult, total , maxresult):

        query = {
        
        'startAt': i,

        }

        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query,
            auth=auth
        )   
        projects_list = response.json()["values"]

        for i in projects_list:
        
            if i['insight'].get('lastIssueUpdateTime',"").startswith(f'2023-0{count}'):
                result.append({"names":i['name'], 'keys': i['key'], 'issuesCount':i['insight'].get("totalIssueCount", ""),'lastIssueUpdateTime':i['insight'].get('lastIssueUpdateTime',""), 'style': i['style']})
                    # result.appei
    count -= 1


with open('6_months_ago_last_updated.json', 'w' ) as file:
    json.dump(result , file, indent= 4)
print('done')    