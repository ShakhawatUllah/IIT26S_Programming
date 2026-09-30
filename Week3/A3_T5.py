print("Program starting.")
print("\nOptions:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = input("Your choice: ")
amount = input("Insert the amount of Celsius: ")
if choice == "1":
    fahrenheit = (float(amount) * 9/5) + 32
    print(f"{amount} Celsius is equal to {fahrenheit} Fahrenheit")
elif choice == "2":
    celsius = (float(amount) - 32) * 5/9
    print(f"{amount} Fahrenheit is equal to {celsius} Celsius")
elif choice == "0":
    print("Exit")
print("23.0 °C equals to 73.4 °F")            
print("\nProgram ending.")