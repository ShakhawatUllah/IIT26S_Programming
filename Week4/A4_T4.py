print("Program starting.")
print()
word_count = 0
character_count = 0
word = input("Insert word (empty stops): ")
while word != "":
    word_count += 1
    character_count += len(word)
    word = input("Insert word (empty stops): ")
print("\nYou inserted:")
print(f"- {word_count} words")
print(f"- {character_count} characters")
print("\nProgram ending.")