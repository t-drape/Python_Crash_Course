future_car = "lamborghini"
print("Will my future car be a supercar from Lamborghini? I predict True")
print(future_car == "lamborghini")
print("Or maybe a Toyota? I think not!")
print(future_car == "Toyota")
country = "Italy"
print("Will my car be from Italy? I think so!")
print(country == "Italy")

model = "supercar"
print("Maybe a truck? No!!!!")
print(model == "Truck")
print("What about a supercar?")
print(model == "supercar")

fuel = "gas"
print("Will it be electric? Not fully!")
print(fuel == "gas")

cost = "expensive"
print("Will it be cheap? I don't think so!")
print(cost=="cheap")
print("Will it be super-expensive? Not that either!")
print(cost=="super-expensive")
print("Maybe just expensive? I'll hedge that bet!")
print(cost=="expensive")

efficiency = "NO"
print("Will it be pracitcal? No way Jose")
print(efficiency=="yes")


alt_car = "Ferrari"
speed_1 = "fast"
speed_2 = "fast"
print("Are horses or bull faster? Or equal? I think equal!")
print(speed_1 == speed_2)
print("All are cars from Italy the same? NO!")
print(future_car == alt_car)

print("Is Ferrari the same as ferrari? In my databse at least!")
print(alt_car.lower() == "ferrari")
print("What if we change ferrari to Ferrari? I think not!")
print(alt_car.lower() == "Ferrari")

age = 15
print(age < 21)
print(age < 1)
print(age > 1)
print(age > 20)
print(age == 10)
print(age==15)
print(age >= 11)
print(age <= 18)
print(age >=18)
print(age <=11)
print(age > 1 and age < 18)
print(age > 1 and age > 18)
print(age > 1 or age > 18)

cars = ["Ferrari", "Nissan", "Mazda", "Lamborghini"]
print("Bugatti" in cars)
print("Ferrari" in cars)
print("Bugatti" not in cars)
print("Ferrari" not in cars)