my_foods = ["pizza", "Falafel", "Carrot cake"]

friend_foods = my_foods[:]

print("\nMy favorite fioods are: ")
for item in my_foods: 
    print("\n\t" + str(item))

print("\nMy friends favorite foods are: ")
for item in friend_foods:
    print("\n\t" + str(item))