with open('learning_python.txt') as f_obj:
	lines = f_obj.readlines()

for line in lines:
	line = line.replace("Python", "C")
	print(line.strip())