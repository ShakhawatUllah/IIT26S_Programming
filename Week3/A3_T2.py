print("Program starting.")
print("String comparison")
WordFirst = input("Insert first word: ")
Character = input("Insert a character: ")
if(Character in WordFirst):
    print(f'Word "{WordFirst}" contains character "{Character}"')
else:
    print(f'Word "{WordFirst}" doesn\'t contain character "{Character}"')
WordSecond = input("Insert second word: ")
if WordFirst < WordSecond:
    print(f'(The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically)')
elif WordSecond < WordFirst:
    print(f'(The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically)')
else:
    print(f'(Both words are the same alphabetically: "{WordFirst}"')          

print("Program ending.")