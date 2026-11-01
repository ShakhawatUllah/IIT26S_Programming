def main():
    print("Program starting.")

    Word = ""

    while True:
        print("Options:")
        print("1 - Insert word")
        print("2 - Show current word")
        print("3 - Show current word in reverse")
        print("0 - Exit")

        Choice = input("Your choice: ")

        if Choice == "1":
            Word = input("Insert word: ")

        elif Choice == "2":
            print(f'Current word - "{Word}"')

        elif Choice == "3":
            print(f'Word reversed - "{Word[::-1]}"')

        elif Choice == "0":
            print("Exiting program.")
            break

        else:
            print("Unknown option.")

        print()

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()