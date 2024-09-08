

foods = []
prices = []
total = 0

while True:
    
    food = input("Enter your desired food:")
    if food.lower() == "q":
        break
    foods.append(food)
    

    price = float(input(f"Enter the price of {food}:"))
    prices.append(price)

print("Your Cart as follows:")
print()

for c in foods:
    print(c, end=" ")
print()

for price in prices:
    total += price

print(f"Your total Price is {total}")