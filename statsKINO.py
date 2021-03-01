import json
from urllib.request import urlopen
from datetime import date,timedelta,datetime

def dates_of_month():
    m = datetime.now().month
    y = datetime.now().year
    ndays = (date(y, m+1, 1) - date(y, m, 1)).days
    ndays -= ndays%datetime.now().day
    d1 = date(y, m, 1)
    d2 = date(y, m, ndays)
    delta = d2 - d1

    return [(d1 + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]

def openDataUrl(x):
    data = urlopen(x).read().decode("utf-8")
    return json.loads(data)

date_draws= "https://api.opap.gr/draws/v3.0/1100/draw-date/{date1}/{date1}/draw-id"

dates = dates_of_month()
draws=[]
for i in dates:
    url = date_draws.format(date1=i)
    draws.append(url)

draw_url = "https://api.opap.gr/draws/v3.0/1100/{drawId}"

for i in draws: #for each day
    data = openDataUrl(i)
    if data == []:
        continue
    per_draw=[]
    for d in data: #get draw's url
        per_draw.append(draw_url.format(drawId=d))
    firstDraw = []
    flag = True
    numOccur = [0 for x in range(80)] #occurrences [1-80]
    for x in per_draw: #get winningnumbers of each draw
        data = openDataUrl(x)
        if data == []:
            continue
        drawList = data['winningNumbers']['list']
        if flag is True:
            firstDraw = drawList
            flag = False
        for a in drawList:
            numOccur[a-1]+=1
    print("1st Draw at %s: " %dates.pop(0),firstDraw)
    print("Statistics for these numbers")
    for x in firstDraw: #occurences of numbers from 1st draw
        per = float(numOccur[x-1]/len(per_draw))*100    
        print("%d->%d/%d (%.2f%%)" %(x,numOccur[x-1],len(per_draw),per))
