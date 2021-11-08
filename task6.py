import requests
import json
with open ("task5.json","r") as file1:
    data=json.load(file1)
# print(data)
list2=[]
for d in data:
    list2.append(d["langauge"])
    a=list2

i=0
dic={}
while i<len(a):
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
            c+=1
        j+=1
    if str(i) not in a[i]:
        dic[a[i]]=c
    i+=1
print(dic)
with open("task6.json","w") as f:
    json.dump(dic,f,indent=4)

