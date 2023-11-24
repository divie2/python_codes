import requests
from requests.auth import HTTPBasicAuth
import json
import csv

# count = []
# # names = json.load(open("test_prod.json"))
# attach = json.load(open("all_attachments(prod).json", "r"))
# # print(attach.values())
# for i in attach.items():
#     if len(i[1]['attach_ids']) > 2  and i[1]['sizes'] :

#         count.append({'attachment' : i[0] , 'count' : int(f"{len(i[1]['attach_ids'])}") , 'size' : i[1]['sizes']})
# # print(count[id])       



# count.sort(key=lambda x:x['count'])



#convert json to csv
attach_csv = json.load(open("all_(prod-count).json", "r"))

# print(attach_csv[0].keys())



with open ("all_(prod-count).csv", "w",encoding="utf-8") as f:
    fieldname = attach_csv[0].keys()
    writer = csv.DictWriter(f,fieldnames= fieldname)
    writer.writeheader()
    for value in attach_csv:
       writer.writerow(value)
print("done !!!")


# a = json.dumps(count,indent= 4)

# with open("all_(prod-count).json", "w") as f:
#     f.write(a)
# print("done !!")
    