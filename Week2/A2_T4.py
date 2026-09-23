print("Program starting.")
print("Estimate how many minutes you spent on programming ...")
print()
A1_T1 = int(input("A1_T1: "))
A1_T2 = int(input("A1_T2: "))
A1_T3 = int(input("A1_T3: "))
A1_T4 = int(input("A1_T4: "))
A1_T5 = int(input("A1_T5: "))
A1_T6 = int(input("A1_T6: "))
A1_T7 = int(input("A1_T7: "))
Total_time = A1_T1 + A1_T2 + A1_T3 + A1_T4 + A1_T5 + A1_T6 + A1_T7
Aeverage_time = Total_time / 7
round_Aeverage_time = round(Aeverage_time)

print()
print(f"In total you spent {Total_time} minutes on programming.")
print(f"Aeverage per task was {round_Aeverage_time: .2f} min and same rounded to the nearest integer {round_Aeverage_time} min.")
print()
print("Program ending.")