class Car:

    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def Sales(self):
        

        if self.for_sale == "True":
            price = "is for sale"
        elif self.for_sale == "False":
            price = "is not for sale"
        return price

while True:


    model = input("Enter the model of your car: ")
    year = input("Enter the year: ")
    color = input("Enter the color: ")
    for_sale = input("Is that for sale ('If yes enter:'True', otherwise 'False')")

    break
    

car1 = Car(model, year, color, for_sale)

rma = car1.Sales()
print(f"Your car model is {car1.model}, chronology {car1.year}, color {car1.color} and {rma}")