animals = ["Tibetan Mastiff", "Chow Chow", "Dachshund", "Doberman Pinscher", "Chinese Shar-Pei"]

message = " is an amazing and beautiful pet" 

for animal in animals:
	print("A " + animal + message)

print("\nAll of these dogs are amazing pets, especially for my future dog!")

print("\nThe first three items in the list are: " + str(animals[:3]))

print("Three items frtom the middle of the list are: " + str(animals[1:4]))

print("The last three items in the list are: " + str(animals[-3:]))