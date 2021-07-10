# number_1 = int(input())
# number_2 = int(input())
#
#
# def factorial_of_number(a):
#     factorial_multiplied = 1
#     for factorial in range(1, a+1):
#         factorial_multiplied *= factorial
#     return factorial_multiplied
#
#
# def number_divisor(a, b):
#     result = a / b
#     print(f"{result:.2f}")
#
#
# factorial_1 = factorial_of_number(number_1)
# factorial_2 = factorial_of_number(number_2)
# number_divisor(factorial_1, factorial_2)



string_of_numbers = input().split(" ")

slice_number = int(input())
left_part = string_of_numbers[:slice_number+1]
right_part = string_of_numbers[slice_number+1:]
list_of_integers = right_part + left_part

print(list_of_integers)