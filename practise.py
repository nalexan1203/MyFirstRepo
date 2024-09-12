
 
menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "popcorn" : 6.00,
        "fries" : 2.50,
        "chips" : 1.00
}

test2 = 0
cart = []
total = 0

while True:
    food = input(f"Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    print(food, end=" ")

for value in cart:
    total += menu.get(value)

print( )  
print(f"{total}")


input()