import requests
response=requests.get("https://covid19.in.th=stat.com/api/open/cases/sum")
data=response.json()

for i,(k,v) in enumerate(data["Province"].item()):
    print("Name = ", k ,"Case = ", v)