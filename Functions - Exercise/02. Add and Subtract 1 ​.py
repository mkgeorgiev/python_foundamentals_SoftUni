

def sum_numbers(a, b):
    result_add = a + b
    return result_add


def subtract(result_of_sum, c):
    result_subtract = result_of_sum - c
    return result_subtract


def add_and_subtract(a,b,c):
    sum_1 = sum_numbers(a, b)
    final_result = subtract(sum_1, c)
    return final_result


a = int(input())
b = int(input())
c = int(input())




print(add_and_subtract(a, b, c))