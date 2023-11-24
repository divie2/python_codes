import requests
import json

# update your jira credentials and path to SSL certs on your machine
username = ""
password = ""
path_to_certs = "/path/to/certs"

# below are examples of JQL queries to get the tickets in a particular project (ABC) with links specfically to confluence, specifically to GEN JIRA, and then those with any remote link (re
confluence_jql = 'project =ABC and (issueFunction in linkedIssueOfRemote("application name", "Barcap confluence"))'
jira_jql = 'project = ABC and (issueFunction in linkedIssueofRemote("application name","GenJIRA"))'
all_remote_jql = 'project = ABC and issueFunction in hasRemoteLinks()'

# form the JSON for getting the tickets with remote link, choosing one of our JQL queries from above
jql_json = {"jql":all_remote_jql, 'startAt':0,"maxResults":1000, "fields" : ["key"] }

# theURLs for searching the source jira instance with our JQL query
Cft_search_URL = 'https://cftjira.barcapint.com/rest/api/2/search'
ficc_search_URL = 'https://ficcjira.barcapint.com/rest/api/2/search'
gen_search_URL = 'https://genjira.barcapint.com/rest/api/2/search'
gtis_search_URL = 'https://gtisjira.barcapint.com/rest/api/2/search'


header = {"content-type" : "application/json"}

# get a list of all tickets from source jirainstance satisfying the  JQL (in this example we use CFT)
jqlresp = requests.post(url = Cft_search_URL,auth = (username, password), data=json.dumps(jql_json), headers=header, verify=path_to_certs)

# loop through each ticket in the source instance satisfying the JQL
for issue in jqlresp.json()['issues']:

    # format the url for the source jira instance to get the original ticket (have included all here for reference but you will only need one), and the URL
    cft_URL = 'https://cftjira.barcapint.com/rest/api/2/issue/{}/remotelink'.format(issue['key'])
    ficc_URL = 'https://ficcjira.barcapint.com/rest/api/2/issue/{}/remotelink'.format(issue['key'])
    gen_URL = 'https://genjira.barcapint.com/rest/api/2/issue/{}/remotelink'.format(issue['key'])
    gtis_URL = 'https://gtisjira.barcapint.com/rest/api/2/issue/{}/remotelink'.format(issue['key'])
    est_URL = 'https://estjira.barcapint.com/rest/api/2/issue/{}/remotelink'.format(issue['key'])

    # get a list of the remote link and its remote relationship and link to screen
    for link in getresp.json():
        # optional - print the issue key and its remote rlationship and link to screen
        if link['application']:
            print(issue['key'],link['relationship',link['object']['url']])
        else:
            print(issue['key'],"links to", link['object']['title'])

        # post the remote link onto the migrated EST ticket
        postresp = requests.post(url=est_URL, auth=(username, password), data = json.dumps(link), headers=header, verify=path_to_certs)


