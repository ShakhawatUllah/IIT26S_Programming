print("Program starting.")
print()
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print()
print("Starting while-loop")
i = start
while i <= stop:
    if i == stop:
        print(i)
    else:
        print(i, end=" ")
    i += 1      
print("\nProgram ending.")