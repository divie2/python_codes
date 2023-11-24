# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
# Pro_key = {}
Pro_key = []

url = "/rest/api/3/project"

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

ass = json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
print(type(ass))
# write into a file
with open("issue.json", "w") as file1:
#     # Writing data to a file
    file1.write(ass)


name = json.load(open("issue.json", "r"))
print(type(name))
for keys in name:
    Pro_key.append(keys['key'])

    # dump to write into a file and load to read
n = json.dumps(Pro_key)
print(type(n))
with open("projectName.json", "w") as f:
    f.write(n)



# keys2 = json.load(open("projectName.json", "w"))
# print(keys2)

print(Pro_key)

# print(projects)

# def archive(a):
#
#     list_of_pkeys = a
#
#     auth = HTTPBasicAuth("divine@geniesys.co.uk", "VdvCBCePB3KgwVt3hX4h5914")
#
#     headers = {
#         "Accept": "application/json"
#     }
#
#     responses = {}
#
#     for pkey in list_of_pkeys:
#         url = f"https://perm-test.atlassian.net/rest/api/3/project/{pkey}/archive"
#         response = requests.request(
#             "POST",
#             url,
#             headers=headers,
#             auth=auth
#         )
#         responses[pkey] = response.text
#
#     json.dump(responses, open('responses.json', 'w'), indent=2)

# def archive(a):
#     l_of_p = a
#     for i in l_of_p:
#         url = f"https://your-domain.atlassian.net/rest/api/3/project/{i}/archive"
#
#         auth = HTTPBasicAuth("divine@geniesys.co.uk", "VdvCBCePB3KgwVt3hX4h5914")
#
#         headers = {
#           "Accept": "application/json"
#         }
#
#         response = requests.request(
#            "POST",
#            url,
#            headers=headers,
#            auth=auth
#         )
#
#         print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


# archive(projects)