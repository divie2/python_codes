import requests
from requests.auth import HTTPBasicAuth
import json
import hashlib

names = json.load(open("issues_attachs_prod.json", "r"))
# names = json.load(open("test_prod.json"))
at = {}
le = {}
le2 = []

# json.dumps(name)
# print(name[88775]['key'])
# print(len(name))

# {facebook.png: {tickets:[as-23, as-25], "size":456, attachment-ids:[]}}
# no of attachment 88775

def hash_attachment(attachment_url):
    resp = requests.get(attachment_url, auth = (username, api_key), allow_redirects=True)
    return hashlib.md5(resp.content).hexdigest()

for name in names:
    for i in name['attachments']:
        filehash = hash_attachment(i['content'])

        # checking if the file name exists

        # if filehash in at.keys():
        #         at[filehash]['attach_ids'].append(i['id'])
        #         at[filehash]['issue_key'].append(name['key'])
        #         at[filehash]['sizes'].append(i['size'])

        #     #creates the new file 
        # else:
        #     at[filehash] = {'attach_ids' : [i['id']] , 'issue_key' : [i['size']] , 'sizes' :[name['key']] }

        # takes into account issue keys with the same size and groups them

        if filehash in at.keys() and i['size'] in at[filehash]['size_key']:
           at[filehash]['size_key'].extend([i['size'] , name['key']])
        #    if there is a match 
           le[filehash] = {'size':i['size'], 'filename' : i['filename']}

        else:   
            at[filehash] = {'size_key' :[i['size'] , name['key'] , at['filename']]}


ab = json.dumps(at , indent = 4)
lg = json.dumps(le,indent = 4)


# with open("prod(sort by image size).json", "w") as f:
#     f.write(ab)
# with open("prod(duplicates).json", "w") as f:
#     f.write(lg)    

# le
name1 = json.load(open("prod(duplicates).json", "r"))
# at
name2 = json.load(open("prod(sort by image size).json", "r"))

all = []
count = 0
# Merge duplicates to duplicate items
for i in name1.keys():
    count += 1
    print(f"{count} of {len(name1.keys())}")
    for a in name2.items():
        if i in a:
            all.append(a)
    # if count == 10:
    #     break
            # with open("prod(final-duplicates.items).json", "a") as f:
            #     f.write(ann) 

with open("prod(final-duplicates.items).json", "w") as test:
    json.dump(all, test, indent=2)
print("done !!") 

# # a = json.dumps(json.loads(at), sort_keys=True, indent=4, separators=(",", ": "))           
# a = json.dumps(at,indent= 4)
# # print(name[le]['attachments'])
# with open("all_attachments(prod).json", "w") as f:
#     f.write(a)
# print("done !!")






