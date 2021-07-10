numbers_in_string = input().split()
second_list_of_numbers =[]
for index in range(len(numbers_in_string)):
    index_number = int(numbers_in_string[index])
    index_number *= -1
    second_list_of_numbers.append(index_number)

print(second_list_of_numbers)