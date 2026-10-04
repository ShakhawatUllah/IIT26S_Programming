print("Program starting.")
print("\nOptions:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")

choice = int(input("Your choice: "))

if choice == 1:
    celsius = int(input("Insert the amount of Celsius: "))
    fahrenheit = (float(celsius) * 9/5) + 32
    print(f"{celsius} degrees Celsius is equals to {fahrenheit} degrees Fahrenheit")
elif choice == 2:
    fahrenheit = int(input("Insert the amount of Fahrenheit: "))
    celsius = (float(fahrenheit) - 32) * 5/9
    print(f"{fahrenheit} degrees Fahrenheit is equals to {celsius} degrees Celsius")
elif choice == 0:
    print("Exit")
else:
    print("Unknown option")           
print("\nProgram ending.")