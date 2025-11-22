with open('learning_python.txt') as f_obj:
	content = f_obj.read()
	print(content + "\n")


with open('learning_python.txt') as f_obj:
	for line in f_obj:
		print(line.rstrip())

print()

with open('learning_python.txt') as f_obj:
	lines = f_obj.readlines()

for line in lines:
	print(line.strip())