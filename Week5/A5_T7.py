DELIMITER = ","


def collectWords():
    Words = ""

    while True:
        Word = input("Insert word(empty stops): ")

        if Word == "":
            break

        if Words == "":
            Words = Word
        else:
            Words += DELIMITER + Word

    return Words


def analyseWords(PWords):
    WordList = PWords.split(DELIMITER)

    AmountWords = len(WordList)
    AmountCharacters = len(PWords.replace(DELIMITER, ""))

    if PWords == "":
        AmountWords = 0
        AverageLength = 0
    else:
        AverageLength = AmountCharacters / AmountWords

    print(f"- {AmountWords} Words")
    print(f"- {AmountCharacters} Characters")
    print("- {:.2f} Average word length".format(AverageLength))


def main():
    print("Program starting.")

    Words = collectWords()
    analyseWords(Words)

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()