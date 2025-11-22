chow = {"type": "medium dog", "owner": "TJ"}
pom = {"type": "small dog", "owner": "Glo"}
c_lab = {"type": "large_dog", "owner": "Dad"}
dox = {"type": "small dog", "owner": "Lia"}

dogs = [chow, pom, c_lab, dox]

for dog in dogs:
	for key, value in dog.items():
		print(key + ":" + " " + value + "\n")