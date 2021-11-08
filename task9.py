import json
import time
import random
with open("task1.json","r") as file1:
    data=json.load(file1)
random_sleep=random.randint(1,5)
for i in data:
    if i in data:
        time.sleep(random_sleep)
    m=i["url"]

    store=m[-10:-1]
    f= open(store+".json","w") 
    s= json.dump(i,f,indent=4)





