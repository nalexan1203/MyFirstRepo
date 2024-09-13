
foods = []
values = []

def order_menu(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        foods.append(key)
        values.append(value)
    return foods,values



total = {}
mass = []
while True:
  
    
    x = input("Enter your choice: ")
    if x == "q":
        break
    y = input("Enter the price: ")
    total= {x:y}
    mass = order_menu(**total)

  
print(total)
print(mass)
print(type(total))
print(type(mass))
