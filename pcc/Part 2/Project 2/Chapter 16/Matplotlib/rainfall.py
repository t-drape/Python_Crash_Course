import csv

from matplotlib import pyplot as plt
from datetime import datetime

file = "Desktop/MR.csv"

with open(file) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates, rainfall = [], []
	for row in reader:
		date = datetime.strptime(row[0], "%m/%d/%y")
		rain = float(row[1])
		rainfall.append(rain)
		dates.append(date)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, rainfall, c='red')

plt.title("Rainfall in Miami - 2021", fontsize=24)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Precipitation (In.)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(0, 4)

plt.show()

