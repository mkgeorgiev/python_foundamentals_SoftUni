import math

string_of_numbers = input().split(", ")


def check_if_number_is_palindrome(a):
    number_is_palindrome = False
    for int_number in a:

        if len(int_number) == 1:
            number_is_palindrome = True
            print(number_is_palindrome)

        elif len(int_number) == 2:
            if int_number[0] == int_number[1]:
                number_is_palindrome = True
                print(number_is_palindrome)

            else:
                number_is_palindrome = False
                print(number_is_palindrome)

        elif not len(str(int_number)) % 2 == 0:
            int_number = list(int_number)
            digit_to_exclude = math.floor(len(int_number) / 2)
            int_number.pop(digit_to_exclude)
            for number_in_list in range(len(int_number) // 2):
                if number_in_list == 0:
                    if int_number[0] == int_number[-1]:
                        number_is_palindrome = True
                    else:
                        number_is_palindrome = False
                elif int_number[number_in_list] == int_number[number_in_list * (-1) - 1]:
                    number_is_palindrome = True
                else:
                    number_is_palindrome = False
            print(number_is_palindrome)
        else:
            for number in range(int(len(int_number)/2 - 1)):
                if number == 0:
                    if int_number[0] == int_number[-1]:
                        number_is_palindrome = True
                    else:
                        number_is_palindrome = False
                elif int_number[number] == int_number[number * (-1)-1]:
                    number_is_palindrome = True
                else:
                    number_is_palindrome = False
            print(number_is_palindrome)


check_if_number_is_palindrome(string_of_numbers)