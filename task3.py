import json
with open("task1.json","r") as f2:
    data1=json.load(f2)
# print(data1)
def group_by_decade(data1):
    years=[]
    for i in data1:
        if i["year"] not in years:
            years.append(i["year"])
    years.sort()
    my_list=[]
    my_dict={}
    for j in years:
        mod=j%10
        dac=j-mod 
        if dac not in my_list:
            my_list.append(dac)
            my_dict[dac]=[]
    for var in my_dict:
        for var1 in data1:
            new=str(var)
            new2=str(var1["year"])
            if new[-2]==new2[-2]:
                my_dict[var].append(var1)
    with open("task3.json","w") as f3:
        json.dump(my_dict,f3,indent=4)
print(group_by_decade(data1))
