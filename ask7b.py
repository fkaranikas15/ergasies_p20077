import urllib.request
import json
import datetime
from collections import Counter


year=2020
month=12
day=1
if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    k=31
elif (month==4 or month==6 or month==9 or month==11):
    k=30
else:
    k=28


trexon_mhnas=[]
for i in range(k):
    d=datetime.date(year,month,day)
    if (day<10):
        trexon_mhnas.append(str(d.year)+"-"+str(d.month)+"-0"+str(d.day)+"/"+str(d.year)+"-"+str(d.month)+"-0"+str(d.day))
    else:
        trexon_mhnas.append(str(d.year)+"-"+str(d.month)+"-"+str(d.day)+"/"+str(d.year)+"-"+str(d.month)+"-"+str(d.day))
    day=day+1

for i in range(k):
    url1="https://api.opap.gr/draws/v3.0/1100/draw-date/"+trexon_mhnas[i]+"/draw-id"
    r=urllib.request.urlopen(url1)
    html1=r.read()
    html1=html1.decode()
    data1=json.loads(html1,strict=False)
    num_day=[]
    for k in range(len(data1)):
        url2="https://api.opap.gr/draws/v3.0/1100/"+str(data1[k])
        r=urllib.request.urlopen(url2)
        html2=r.read()
        html2=html2.decode()
        data2=json.loads(html2,strict=False)
        t=data2["winningNumbers"]["list"]
        num_day=num_day+t


    def most_frequent(List):
        counter = 0
        num = List[0]

        for i in List:
            curr_frequency = List.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                num = i

        return num
    print("O pio suxnos arithmos ths",i+1,"hs meras tou mhna einai",most_frequent(num_day))
    print(" ")
    counts=Counter(num_day)
    print(counts)
