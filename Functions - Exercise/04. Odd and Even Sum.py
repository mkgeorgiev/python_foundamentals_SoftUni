a = int(input())


def odd_and_even_sum_of_digits_function(a):
    list_of_digits = []
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    for digit in str(a):
        list_of_digits.append(int(digit))
    for digit_value in range (len(list_of_digits)):
        if list_of_digits[digit_value] % 2 == 0:
            sum_of_even_numbers += list_of_digits[digit_value]
        else:
            sum_of_odd_numbers += list_of_digits[digit_value]

    print(f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}")


odd_and_even_sum_of_digits_function(a)