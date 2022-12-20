from collections.abc import Callable
import random

def addition(a: float, b: float) -> float:
    """Cette fonction permet d'additionner deux nombres

    a float le premier nombre à additionner
    b float le deuxieme nombre à additionner
    return float le résultat de l'addition
    """
    result = a + b

    return result

result = addition(123,42)
print(result)

my_number1 = 123
my_number2 = 42
result = addition(my_number1,my_number2)
print(result)

def calculer(calcul1: Callable, calcul2: Callable, a:float, b:float, c:float) -> float:
    result = calcul1(a, b)
    result = calcul2(result, c)

    return result

result = calculer(addition, addition, 123, 42, 3.14)
print(result)




def my_average(numbers: list) -> float:
    result = 0

    my_sum = 0
    count = 0

    for number in numbers:
        if type(number) is int or type(number) is float:
            my_sum += number
            count += 1

    result = my_sum / count

    return result   

my_list = [42, True, "abc", 123]
result = my_average(my_list)
print(result)

