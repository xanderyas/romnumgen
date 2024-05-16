def main():
    question()
    roman()


def question():
    print("Welcome to the Roman Number Generator")
    
def roman():
    while True:
        try:
            number = int(input("Type in an integer: "))
            if number < 1:
                print("Integer too small, please try again.")
                continue
            if number >= 4000:
                print("Roman numerials only go up to 3999, please try again.")
                continue
            break
        except ValueError:
            print("Invalid number, please try again.")
            continue
    
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM "]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    print("Roman Numerials: ", end="")
    print(thousands[number // 1000], end="")
    print(hundreds[(number % 1000) // 100], end="")
    print(tens[(number % 100) // 10], end="")
    print(ones[number % 10], end="")


if __name__ == "__main__":
    main()