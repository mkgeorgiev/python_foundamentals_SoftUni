n = int(input())
list_positive_numbers = []
list_negative_numbers = []
list_even_numbers = []
list_odd_numbers = []

for numbers in range(n):
    new_number = int(input())
    if new_number >= 0:
        list_positive_numbers.append(new_number)
    else:
        list_negative_numbers.append(new_number)
    if new_number % 2 == 0 or new_number ==0:
        list_even_numbers.append(new_number)
    else:
        list_odd_numbers.append(new_number)

command = input()
if command == "even":
    print(list_even_numbers)
elif command == "odd":
    print(list_odd_numbers)
elif command == "positive":
    print(list_positive_numbers)
elif command == "negative":
    print(list_negative_numbers)
