data = [
    {"name":"Ram","branch":"IT","marks":{"math":67,"phy":76}},
    {"name":"Shyam","branch":"CS","marks":{"math":91,"phy":92}},
    {"name":"Mohan","branch":"IT","marks":{"math":55,"phy":60}},
    {"name":"Aman","branch":"CS","marks":{"math":60,"phy":59}},
    {"name":"Kunal","branch":"IT","marks":{"math":37,"phy":84}},
    ]

name = input("Enter Student Name : ")
total = 0
for i in range(len(data)):
    if data[i]["name"] == name:
        # total = sum(data[i]["marks"].values())
        # total = data[i]["marks"]["math"] + data[i]["marks"]["phy"]
        # print(total)
        for key in data[i]["marks"]:
            total += data[i]["marks"][key]

print(total)


