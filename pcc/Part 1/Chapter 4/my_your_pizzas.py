pizzas = ["Momma's pizza", "Pepperoni pizza with veggies", "BBQ chicken"]

message = "is an amzaing pizza!"

for pizza in pizzas:
    print("\t" + pizza + " " + message)
    
print("\nI love any pizza my mom makes!")

friend_pizzas = pizzas[:]
pizzas.append("Hot Honey")
friend_pizzas.append("Dessert")

print("\nMy favorite pizzas are: \n")
for pizza in pizzas:
    print("\t" + str(pizza))

print("\nMy friend's favorite pizzas are: \n")
for pizza in friend_pizzas:
    print("\t" + str(pizza))