print("Program starting.")
print()
word = input("Insert a closed compoundword: ")

length = len(word)
first_character = (word[0])
reverse_word = word[::-1]

print(f"The word you inserted is '" + word + "' and in reverse it is '" + reverse_word + "'.")
print(f"The inserted word length is {length}")
print(f"Last character is '{word[-1]}'")
print()
print("Take substring from the inserted word by inserting...")
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
size = int(input("3) Step size: "))
print()

substring = word[start:end:size]
print(f"The word '{word}' sliced to the defined substring is '{substring}'.")
print("Program ending.")