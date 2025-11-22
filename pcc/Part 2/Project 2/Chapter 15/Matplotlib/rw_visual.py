import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	# Make a random walk and plot the points
	rw = RandomWalk(5000000)
	rw.fill_walk()
	plt.figure(dpi=100, figsize=(15, 8))
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=40)

	ax = plt.gca()

	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)


	plt.show()
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break