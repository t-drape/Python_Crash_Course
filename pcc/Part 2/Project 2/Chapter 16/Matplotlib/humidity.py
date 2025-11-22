import csv

from matplotlib import pyplot as plt
from datetime import datetime

file = "Desktop/DH.csv"

with open(file) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates, max_humidity, min_humidity = [], [], []
	for row in reader:
		date = datetime.strptime(row[0], "%m/%d/%y")
		maxh = int(row[1])
		minh = int(row[3])
		dates.append(date)
		max_humidity.append(maxh)
		min_humidity.append(minh)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, max_humidity, c="green")
plt.plot(dates, min_humidity, c="yellow")
plt.fill_between(dates, max_humidity, min_humidity, facecolor="green",
 alpha=0.5)

plt.title("Humidity in Dallas, TX - 2023", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Humidity (%)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(0, 110)

plt.show()
