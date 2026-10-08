print("Check multiplicative persistence.")

number = int(input("Insert an integer: "))

steps = 0

while number >= 10:
    digits = [int(digit) for digit in str(number)]

    result = 1

    for digit in digits:
        result *= digit

    print(" * ".join(str(digit) for digit in digits), "=", result)

    number = result
    steps += 1

print("No more steps.")
print()
print(f"This program took {steps} step(s)")
print()
print("Program ending.")