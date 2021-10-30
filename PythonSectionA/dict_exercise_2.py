data = [
    {"name":"Ram","branch":"IT","marks":{"math":67,"phy":76}},
    {"name":"Shyam","branch":"CS","marks":{"chem":91,"bio":92}},
    {"name":"Mohan","branch":"IT","marks":{"math":55,"c++":60}},
    {"name":"Aman","branch":"CS","marks":{"java":60,"math":59}},
    {"name":"Kunal","branch":"IT","marks":{"math":37,"phy":84}},
    ]

name = input("Enter Student Name : ")
marks = 0
for i in range(len(data)):
    if data[i]["name"] == name:
        # s1 = data[i]["marks"]["math"]
        # s2 = data[i]["marks"]["phy"]
        # print("Total Marks",s1 + s2)
        # break
        for key in data[i]["marks"]:
            marks += data[i]["marks"][key]

print("Total Marks of {} is {}".format(name, marks))
