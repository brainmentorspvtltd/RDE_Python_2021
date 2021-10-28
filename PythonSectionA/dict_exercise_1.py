data = {
    "names" : ["Ram","Shyam","Amit","Mohit","Naman"],
    "marks" : [67,87,76,33,89],
    "branch" : ["IT","CS","CS","EC","EC"]
    }

#print(data["names"][3])
#print(data["marks"][3])

name = input("Enter Student Name : ")
index = data["names"].index(name)
print(data["marks"][index])

for i in range(len(data)):
    if data["names"][i] == name:
        print(data["marks"][i])
        break


