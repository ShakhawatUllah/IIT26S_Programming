def askDimension(PPrompt: str) -> float:
    Feed = input(f"Insert {PPrompt}: ")
    return float(Feed)


def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Area = PWidth * PHeight
    return Area


def main():
    print("Program starting.")

    Width = askDimension("width")
    Height = askDimension("height")

    Area = calcRectangleArea(Width, Height)

    print("")
    print(f"Area is {Area}²")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()