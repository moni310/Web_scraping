import json
with open("task1.json","r") as file1:
    data=json.load(file1)
# print(data)
for i in data:
    # print(i)
    m=i["url"]
    store=m[-10:-1]
    print(store)
    f= open(store+".json","w") 
    s= json.dump(i,f,indent=4)
    # print(f)

        
        

        


 