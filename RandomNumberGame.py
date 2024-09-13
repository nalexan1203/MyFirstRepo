import random 



low = 1
high = 100
guesses = 0

number = random.randint(1,100)

while True:
    guess = int(input(f"Enter a guess value between {low} - {high} :"))
    guesses += 1

    if guess > number:
        print("Your guess is too high")
    elif guess < number:
        print("Your guess is too low")
    else:
        print(f"{guess}: That number is the correct!")
        break

print(f"The number of guesses amounts to {guesses}")
