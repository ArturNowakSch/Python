def main():
    print("Wprowadź działanie w formacie <liczba_1> <działanie> <liczba_2>")
    print("Dostępne działania to: ")
    print("+ = dodawanie")
    print("- = odejmowanie")
    print("* = mnożenie")
    print("/ = dzielenie")

    user_input = input("Podaj działanie: ")

    try:
        num_1, operation, num_2 = user_input.split()
        num_1 = float(num_1)
        num_2 = float(num_2)
    except ValueError:
        print("Nieprawidłowy format danych!")
        return

    match operation:
        case "+":
            print("Dodawanie")
        case "-":
            print("Odejmowanie")
        case "*":
            print("Mnożenie")
        case "/":
            print("Dzielenie")


if __name__ == "__main__":
    while True:
        main()
        print("-" * 5)
        print()
