import matplotlib.pyplot as plt
from random_walk import RandomWalk
from datetime import datetime


import csv
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    next_line = next(reader)

    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            date_xx = datetime.strptime(row[0],'%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])

        except ValueError:
            print (date_xx)
        else:
            highs.append(high)
            dates.append(date_xx)
            lows.append(int(row[3]))


fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.5)
plt.title('Daily high and low temperatures-2014',fontsize =24)
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
fig.autofmt_xdate()

plt.show()