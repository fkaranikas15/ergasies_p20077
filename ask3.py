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

numbers=[]
draw_id=[]
kinobonus=[]
for i in range(k):
    url="https://api.opap.gr/draws/v3.0/1100/draw-date/"+trexon_mhnas[i]+"/draw-id"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    data=json.loads(html,strict=False)
    draw_id.append(data[-1])

for i in range(k):
    url1="https://api.opap.gr/draws/v3.0/1100/"+str(draw_id[i])
    r=urllib.request.urlopen(url1)
    html1=r.read()
    html1=html1.decode()
    data=json.loads(html1,strict=False)
    t=data["winningNumbers"]["list"]
    bonus=data["winningNumbers"]["bonus"]
    t.sort()
    print("h 1h klhrwsh ths",i+1,"h meras tou mhna einai",t)
    print("To kinobonus ths klhrwshs einai to",bonus)
    print(" ")
    numbers=numbers+t
    kinobonus=kinobonus+bonus


def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num


print(" ")
print("O pio suxnos arithmos einai",most_frequent(numbers))

print(" ")
print("O pio suxnos arithmos kinobonus einai",most_frequent(kinobonus))
print(" ")
counts=Counter(numbers)
print(counts)
