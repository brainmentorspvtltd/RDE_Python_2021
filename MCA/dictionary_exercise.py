data = {
    "names" : ["John","Shawn","Mac","Nick","Tom"],
    "marks" : [78,99,67,79,91],
    "branch" : ["IT","CS","IT","IT","CS"]
    }

'''
name = input("Enter name of student : ")

for i in range(len(data["names"])):
    if name == data["names"][i]:
        print(data["marks"][i])
'''
totalMarks = 0
count = 0
for i in range(len(data["names"])):
    if "IT" == data["branch"][i]:
        totalMarks += data["marks"][i]
        count += 1

print(totalMarks/count)




