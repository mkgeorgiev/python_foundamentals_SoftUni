n = int(input())
list_positive_numbers = []
list_negative_numbers = []
count_of_positive_numbers = 0
sum_negative_numbers = 0

for number in range(n):
    new_number = int(input())
    if new_number >= 0:
        list_positive_numbers.append(new_number)
        count_of_positive_numbers += 1
    else:
        list_negative_numbers.append(new_number)
        sum_negative_numbers += new_number

print(list_positive_numbers)
print(list_negative_numbers)
print(f"Count of positives: {count_of_positive_numbers}. Sum of negatives: {sum_negative_numbers}")

