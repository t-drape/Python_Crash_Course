import pygal

from die import Die

# Create a D6.
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results to a list.

results = [(die_1.roll() + die_2.roll()) for roll_num in range(50000000)]

# Analyze the results
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = pygal.Bar()

hist.title = "Results of rolling two D8 50,000,000 times."
hist.x_labels = [x for x in range(2, 13)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D8 + D8", frequencies)
hist.render_to_file('Desktop/two_8.svg')