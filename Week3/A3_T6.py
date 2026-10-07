print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")
print("\nOptions: ")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
choice = input("Your choice: ")
if choice == "1":
    print("\nLength options: ")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Length_choice = input("Your choice: ")
    if Length_choice == "1":
        meters = float(input("Insert meters: "))
        kilometers = meters / 1000
        print(f"{meters} meters is {kilometers} kilometers")
    elif Length_choice == "2":
        kilometers = float(input("Insert kilometers: "))
        meters = kilometers * 1000
        print(f"{kilometers} kilometers is {meters} meters")
    elif Length_choice == "0":
        print("Exiting...")
if choice == "2":
    print("\nWeight options: ")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Weight_choice = input("Your choice: ")
    if Weight_choice == "1":
        grams = input("Insert grams: ")
        pounds = float(grams) / 453.592
        print(f"{grams} g is {pounds} lb")
    elif Weight_choice == "2":
        pounds = input("Insert pounds: ")
        grams = float(pounds) * 453.592
        print(f"{pounds} lb is {grams} g")
    elif Weight_choice == "0":
        print("Exiting...")
if choice == "0":
    print("Exiting...")
print("\nProgram ending.")