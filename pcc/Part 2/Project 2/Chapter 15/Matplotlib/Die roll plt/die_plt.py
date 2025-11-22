import matplotlib.pyplot as plt

from die import Die

die = Die()

x_values = [x for x in range(1, 7)]
rolls = [die.roll() for x in range(1000)]

y_values = [rolls.count(value) for value in range(1, 7)]


plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.viridis,
 edgecolor='none', s=40)

plt.title("Die Rolls", fontsize=24)
plt.xlabel("Roll", fontsize=14)
plt.ylabel("Occurences", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([1, 6, 0, 1001])

plt.savefig('Desktop/diem.png', bbox_inches='tight')