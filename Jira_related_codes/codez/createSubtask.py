# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json


#
# url = input("Enter your url : ")
# email = input("Enter your email address : ")
# token = input("enter your token : ")
# summary = input("Enter your Summary for the week : ")
# print(type(url))
#
def create_issue(a, b, c):
    url = f"https://{a}.atlassian.net/rest/api/3/issue"


    auth = HTTPBasicAuth(f"{b}", f"{c}")


    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({

        "fields": {
            "summary": "Carrying out tests 2",

            "issuetype": {
                "id": "10001"
            },
            "project": {
                "id": "10000"
            }

        }
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    issue_id_task = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    # write into a file
    with open("issue-id.json", "w") as file1:
    # Writing data to a file

        file1.write(issue_id_task)

    return url,b,c


def create_subtask(a, b):
    subtask = 1

    while subtask <= 5:

        url = f'{a[0]}'

        auth = HTTPBasicAuth(f"{a[1]}", f"{a[2]}")

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }


        payload = json.dumps({


            "fields": {
                "summary": "Subtask 1",
                "parent": {
                    "id": f'{b}'
                },

                "issuetype": {
                    "id": '10003'
                },
                "project": {
                    "id": "10000"
                }

            }
        })

        response = requests.request(
            "POST",
            url,
            data=payload,
            headers=headers,
            auth=auth
        )

        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
        subtask += 1

created_issue = create_issue('', '', '')

name = json.load(open("issue-id.json", "r"))

print(name['id'])

create_subtask(created_issue, name['id'])

