import sys

str_numbers = input().split()
numbers_to_remove = int(input())

for str_to_int in range(len(str_numbers)):
    str_numbers[str_to_int] = int(str_numbers[str_to_int])
for every_remove in range(numbers_to_remove):
    str_numbers.remove(min(str_numbers))
for int_to_str in range(len(str_numbers)):
    if int_to_str == len(str_numbers)-1:
        print(str_numbers[int_to_str])
        break
    print(str_numbers[int_to_str], end= ", ")