def showOptions():
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None


def askChoice():
    Choice = input("Your choice: ")

    if Choice.isnumeric():
        return int(Choice)
    else:
        return -1


def main():
    print("Program starting.")

    Count = 0

    while True:
        showOptions()
        Choice = askChoice()

        if Choice == 1:
            print(f"Current count - {Count}")

        elif Choice == 2:
            Count += 1

        elif Choice == 3:
            Count = 0

        elif Choice == 0:
            print("Exiting program.")
            break

        else:
            print("Unknown option!")

        print()

    print()
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()