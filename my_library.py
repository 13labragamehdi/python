#fonction moyenne 

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