import requests
import json
from requests.auth import HTTPBasicAuth
import tkinter as tk
import tkinter.scrolledtext as tkscrolled
token = ""
def print(value):
    TKScrollTXT.insert(tk.END, "\n" + str(value))

# Fill in authentication details here
auth = HTTPBasicAuth("", token)

headers = {
   "Accept": "application/json",
   "Content-Type": "application/json"
}

#Function to get next-gen project and its data 
def get_project(url, project_key):
   s_url = f"{url}/rest/api/latest/project/{project_key}"
   s_response = requests.request("GET", s_url, headers=headers, auth=auth, verify=False)
   s_log = json.loads(s_response.text)
   return s_log

#Function to get the notification scheme for the next-gen project
def get_notification_scheme(url, project_key):
   s_url = f"{url}/rest/api/latest/project/{project_key}/notificationscheme"
   s_response = requests.request("GET", s_url, headers=headers, auth=auth , verify=False)
   s_log = json.loads(s_response.text)
   s_nscheme = s_log["id"]
   return s_nscheme

#Function to get permission scheme for next-gen project 
def get_permission_scheme(url, project_key):
   s_url = f"{url}/rest/api/latest/project/{project_key}/permissionscheme"
   s_response = requests.request("GET", s_url, headers=headers, auth=auth , verify=False)
   s_log = json.loads(s_response.text)
  
   s_pscheme = s_log["scope"]["project"]["id"]
   return s_pscheme

#function to get issue security scheme for next-gen project 
def get_issue_security_scheme(url, project_key):
    s_url = f"{url}/rest/api/latest/project/{project_key}/issuesecuritylevelscheme"
    s_response = requests.request("GET", s_url, headers=headers, auth=auth , verify=False)
    s_log = json.loads(s_response.text)
    s_issue_security_scheme = s_log["id"]
    return s_issue_security_scheme

#Function to create classic project with config from next-gen project 
def create_project(url, source_project, source_permission_scheme, source_notification_scheme, source_issue_security_scheme):
    t_url = f"{url}/rest/api/latest/project"

    s_name = f"{new_project_name}"
    s_description = source_project["description"]
    s_lead = source_project["lead"]["accountId"]
    s_key = f"{new_key}"
    s_projectTypeKey = source_project["projectTypeKey"]
    s_assigneeType = source_project["assigneeType"]
    # s_projectCategory = source_project["projectCategory"]["id"]

    payload = {
        "key": s_key,
        "name": s_name,
        "projectTypeKey": s_projectTypeKey,
        "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-simplified-kanban-classic",
        "description": s_description,
        "leadAccountId": s_lead,
        "url": url,
        "assigneeType": s_assigneeType,
        # "avatarId": ,
        # "issueSecurityScheme": source_issue_security_scheme,
        # "permissionScheme": source_permission_scheme,
        # "notificationScheme": source_notification_scheme,
        # "categoryId": s_projectCategory
    }
    # print(payload)
    t_response = requests.request("POST", t_url, json=payload, headers=headers, auth=auth, verify=False)
    
    t_log = json.loads(t_response.text)
    print(t_log)
    print("last")

import json

#Function for 
def migrate():
    global new_key, new_project_name
    json.dump({"test": "should output"}, open("result.json", "w"))
    print("beginning")
    mig = get_entries()
    url = mig["url"]
    project_key = mig["project_key"].upper()
    new_key = mig["new_key"].upper()
    new_project_name = mig["new_project_name"]
    
    project = get_project(url, project_key)
    notification_scheme_id = get_notification_scheme(url, project_key)
    print("test")
    permission_scheme_id = get_permission_scheme(url, project_key)
    issue_security_scheme_id = get_issue_security_scheme(url, project_key)
    json.dump({"project":project, "ntoti":notification_scheme_id, "perm":permission_scheme_id, "issue-sec":issue_security_scheme_id}, open("result.json", "w"), indent=3)
    create_project(url, project, permission_scheme_id, notification_scheme_id, issue_security_scheme_id)


#Function to get enteries from tkinter gui
def get_entries():
    project_key = project_key_ent.get()
    if project_key == '' :
        if 'No project_key Entered' not in TKScrollTXT.get(0.0, "end-1c"): 
            TKScrollTXT.delete(0.0, 2.0)
            TKScrollTXT.insert(1.0, 'No project_key Entered\n')
        return None
    url = url_ent.get()
    if url == '' :
        if 'No url Entered' not in TKScrollTXT.get(0.0, "end-1c"): 
            TKScrollTXT.delete(0.0, 2.0)
            TKScrollTXT.insert(1.0, 'No url Entered\n')
        return None
    new_key = apik_ent.get()
    if new_key == '' :
        if 'No new_key Entered' not in TKScrollTXT.get(0.0, "end-1c"): 
            TKScrollTXT.delete(0.0, 2.0)
            TKScrollTXT.insert(1.0, 'No new_key Entered\n')
        return None
    new_project_name = grp_ent.get()
    if new_project_name == '' :
        if "No new_project_name given" not in TKScrollTXT.get(0.0, "end-1c"): 
            TKScrollTXT.delete(0.0, 2.0)
            TKScrollTXT.insert(1.0, 'No new_project_name given\n')
        return None

    return({"url": url,
            "project_key": project_key,
            "new_key": new_key,
            "new_project_name": new_project_name })


root = tk.Tk()

root.columnconfigure((0,2), weight=1)
root.columnconfigure((1,3), weight=3)

root.rowconfigure(list(range(5)), weight=1)
    
url_frm = tk.Frame(root, width=10)
url_frm.grid(row=0, column=0, columnspan=1, ipadx=10, sticky='news')

url_lbl = tk.Label(master=url_frm, text="Url", font="-weight bold")
url_lbl.pack(fill=tk.BOTH, side=tk.LEFT, ipadx=5)

url_ent = tk.Entry(root, width=20)
url_ent.grid(row=0, column=1, columnspan=1,
    padx=5, pady=5, ipady=4, ipadx=4, sticky='news')

apik_lbl = tk.Label(master=root, text="Classic Key", width=20, font="-weight bold")
apik_lbl.grid(row=0, column=2, sticky='news')

apik_ent = tk.Entry(root)
apik_ent.grid(row=0, column=3, columnspan=2,
    padx=5, pady=5, ipady=4, sticky='news')

project_key_frm = tk.Frame(root, width=7)
project_key_frm.grid(row=1, column=0, columnspan=1, ipadx=10, sticky='news')

project_key_lbl = tk.Label(master=project_key_frm, text="Next Gen Key", font="-weight bold")
project_key_lbl.pack(fill=tk.BOTH, side=tk.LEFT, ipadx=5)

project_key_ent = tk.Entry(root, width=20)
project_key_ent.grid(row=1, column=1, columnspan=1,
    padx=5, pady=5, ipady=4, ipadx=4, sticky='news')

grp_lbl = tk.Label(root, text="Classic Project Name", width=15, font="-weight bold")
grp_lbl.grid(row=1, column=2)

grp_ent = tk.Entry(root)
grp_ent.grid(row=1, column=3, columnspan=2, padx=5, pady=5, sticky='news')

grp_btn = tk.Button(root, text="Migrate", command=(lambda: migrate()))
grp_btn.grid(row=3, column=10, padx=8)

'''grp_btn = tk.Button(root, text="Add Users to Group", command=(lambda: csv_user()))
grp_btn.grid(row=1, column=6)

save_btn1 = tk.Button(root, text="Save response as JSON", command=(lambda : file_save("json")))
save_btn1.grid(row=2, column=6, padx=4, sticky='s')

save_btn2 = tk.Button(root, text="Save response as CSV", command=(lambda : file_save("csv")))
save_btn2.grid(row=3, column=6, pady=4, sticky='n')'''

# JSON Output Display
area = tk.Frame(root, relief=tk.RAISED)
area.grid(row=2, column=0, columnspan=6, rowspan=15,
    padx=5, pady=5, ipady=5)

TKScrollTXT = tkscrolled.ScrolledText(area, wrap='word', height=20, width=75)
# TKScrollTXT.insert(1.0, textss)
TKScrollTXT.pack(fill='both')

def main():
    root.title("Next Gen to Classic") 
    root.geometry("650x420")
    root.mainloop()

if __name__ == '__main__':
    main()
