name = input("Give us an appropriate username:")

if len(name) >= 12:
    print("Give a valid number of characters!")
elif not name.find(" ") == -1:
    print("No name spaces!")
elif not name.isalpha() == 1:
    print("Only Strings!")
else:
    print(f'Welcome {name}')