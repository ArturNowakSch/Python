import time

import math_utilties

def main():
    print("Wprowadź działanie w formacie <liczba_1> <działanie> <liczba_2>")
    print("Dostępne działania to: ")
    print("+ = dodawanie")
    print("- = odejmowanie")
    print("* = mnożenie")
    print("/ = dzielenie")
    print("^ = potęgowanie")

    user_input = input("Podaj działanie: ")

    try:
        num_1, operation, num_2 = user_input.split()
        num_1 = float(num_1)
        num_2 = float(num_2)
    except ValueError:
        print("Nieprawidłowy format danych!")
        return

    try:
        match operation:
            case "+":
                result = math_utilties.sum(num_1, num_2)
            case "-":
                result = math_utilties.subtraction(num_1, num_2)
            case "*":
                result = math_utilties.multiplication(num_1, num_2)
            case "/":
                result = math_utilties.division(num_1, num_2)
            case "^":
                result = math_utilties.power(num_1, num_2)
            case _:
                print("Nie ma takiego działania!")
                return
        print()
        print(f"Wynik działania {user_input} to: {result}")
    except math_utilties.MathException as e:
        print(f"Błąd - {e}")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)
        print("-" * 5)
        print()
