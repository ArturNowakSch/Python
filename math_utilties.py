import  math
class MathException(Exception):
    message = "Błąd matematyczny"

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


def sum(a: float, b: float) -> float:
    return a + b


def subtraction(a:float, b:float) -> float:
    return a - b


def multiplication(a:float, b:float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if (b != 0):
        return a / b
    else:
        raise MathException("Dzielenie przez 0")


def power(a, b):
    y = 1
    for x in range(b):
        y = y * a
    return y

