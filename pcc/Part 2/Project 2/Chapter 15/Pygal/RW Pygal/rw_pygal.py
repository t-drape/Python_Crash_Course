import pygal

from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()

max_result = 1000

results = [rw.x_values[i] for i in range(max_result)]
frequency = [results.count(value) for value in range(-4, 5)]

new_frequency = [(i, j) for i, j in zip(rw.x_values, rw.y_values)]
chart = pygal.XY(stroke=False)
chart.title = "Random Walk using Pygal"

chart.add("Random Walk", new_frequency)





chart.render_to_file("Desktop/rw_pygal.svg")