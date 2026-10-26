print("Program starting.")
print()
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspection = int(input("Insert inspection point: "))
print()
valid = True
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    valid = False

if inspection < start or inspection > stop:
    print("Inspection value must be within the range of start and stop.")
    valid = False

if valid:
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if i == inspection:
            break
        print(i, end=" " if i < inspection - 1 else "")
    print("\nSecond loop - inspection with continue:")
    first = True   
    for i in range(start, stop):
        if i == inspection:
            continue
        if not first:
            print(" ", end="")
        print(i, end="")
        first = False
        print()
print("\nProgram ending.")