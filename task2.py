import json
with open("task1.json","r") as file1:
    data=json.load(file1)
# print(data)
def group_by_year(data):
    years=[]
    dic={}
    for i in data:
        if i["year"] not in years:
            years.append(i["year"])
    years.sort()
    for j in years:
        list1=[]
        for m in data:
            if j==(m["year"]):
                list1.append(m)
        dic[j]=list1
    with open("tak2.json","w") as f:
        json.dump(dic,f,indent=4)
    return dic
print(group_by_year(data))






