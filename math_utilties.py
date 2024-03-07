class MathException(Exception):
    message = "Błąd matematyczny"

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


def sum(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if (b != 0):
        return a / b
    else:
        raise MathException("Dzielenie przez 0")
