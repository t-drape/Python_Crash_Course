import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = 'Desktop/good_year.csv'
other_file = "Desktop/SF_year.csv"

# Get dates and high temps from file
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			date = datetime.strptime(row[2], "%m/%d/%y")
			high = int(row[6])
			low = int(row[7])
		except ValueError:
			print(date, 'missing data')
		else:
			dates.append(date)
			highs.append(high)
			lows.append(low)

with open(other_file) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	o_dates, o_highs, o_lows = [], [], []
	for row in reader:
		try:
			date = datetime.strptime(row[0], "%m/%d/%y")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(date, 'missing data')
		else:
			o_dates.append(date)
			o_highs.append(high)
			o_lows.append(low)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.plot(o_dates, o_highs, c='green', alpha=0.5)
plt.plot(o_dates, o_lows, c='yellow')
plt.fill_between(o_dates, o_highs, o_lows, facecolor='orange', alpha=0.1)

# Format plot
plt.title("Daily high and low temps - 2021\nSitka, AK (bottom) and Death Valley, CA (top)", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temp (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(0, 150)

plt.show()