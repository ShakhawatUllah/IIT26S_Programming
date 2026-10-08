print("Program starting.")
print()
number = int(input("Insert a positive integer: "))
steps = 0
while number != 1:
    print(number, end=" -> ")
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    steps += 1
print("1")
print(f"Sequence had {steps} total steps.")
print("\nProgram ending.")