import json
unique = []
difference= []
file_path = "Server_boards.json"
app = []
# Using 'with open' to read a file
with open(file_path, "r") as file1:
    data = json.load(file1)
    # print(data)

    for i in data:
        #  print(len(i["name"]))
         app.append(i["NAME"])
        # print(i["NAME"])
          

# with open("serverWorkflow-screen.json", "r") as file2:
#     data1 = json.load(file2)
#     for j in data1:
#         app.append(j)  

with open("new_server_board.json", "w") as h:
            json.dump(app, h, indent=2)
  


# Differences in cloud and server

with open("test.json", "r") as file1:
  cloud_screens_schemes = json.load(file1)
#   print(len(cloud_screens))

with open("new_server_board.json", "r") as file2:
    server_screens_schemes = json.load(file2)

# Calculate the differences using set operations
differences = set(server_screens_schemes) - set(cloud_screens_schemes)

print(len(differences))
print(len(set(cloud_screens_schemes)))
print(len(set(server_screens_schemes)))

print((set(cloud_screens_schemes) - set(server_screens_schemes)))
print(len(set(cloud_screens_schemes).intersection(set(server_screens_schemes))))

for line in differences:
    difference.append(line.strip())
    # print(line)

with open("Difference_in_boards.json", "w") as f:
    json.dump(difference, f, indent=4)
print("done")


# file_path = "Cloudscreens.json"

# # Read the contents of the file
# with open(file_path, "r") as file:
#     data = json.load(file)

# for i in data:
#     if "(migrated)" not in i:
#         unique.append(i)
# with open("Unique_cloud.json", "w") as f:
#             json.dump(unique, f, indent=4)
# print("done")


