string_of_numbers = input().split(" ")


def string_of_integers_slicing(list_of_integers, command):
    command = command.split(" ")
    slice_number = int(command[1])

    if 0 > slice_number or slice_number > (len(list_of_integers)):
        print("Invalid index")
    else:
        left_part = list_of_integers[:slice_number+1]
        right_part = list_of_integers[slice_number+1:]
        list_of_integers = right_part + left_part

    return list_of_integers


def turning_list_of_int_to_2_lists_of_odd_and_even_numbers(list_of_integers):
    list_of_even_numbers = []
    list_of_odd_numbers = []

    for number in list_of_integers:
        if int(number) % 2 == 0:
            list_of_even_numbers.append(int(number))
        else:
            list_of_odd_numbers.append(int(number))

    return list_of_even_numbers, list_of_odd_numbers


def max_and_min_odd_and_even_numbers(list_of_integers):
    import sys
    max_even_number = -sys.maxsize
    min_even_number = sys.maxsize
    max_odd_number = -sys.maxsize
    min_odd_number = sys.maxsize
    max_even_number_index = None
    min_even_number_index = None
    max_odd_number_index = None
    min_odd_number_index = None

    for numbers in range(len(list_of_integers)):
        if int(list_of_integers[numbers]) % 2 == 0:
            if max_even_number <= int(list_of_integers[numbers]):
                max_even_number = int(list_of_integers[numbers])
                max_even_number_index = numbers
            if min_even_number >= int(list_of_integers[numbers]):
                min_even_number = int(list_of_integers[numbers])
                min_even_number_index = numbers
        else:
            if max_odd_number < int(list_of_integers[numbers]):
                max_odd_number = int(list_of_integers[numbers])
                max_odd_number_index = numbers

            if min_odd_number > int(list_of_integers[numbers]):
                min_odd_number = int(list_of_integers[numbers])
                min_odd_number_index = numbers

    if max_even_number_index is None:
        max_even_number_index = "No matches"
    if max_odd_number_index is None:
        max_odd_number_index = "No matches"
    if min_odd_number_index is None:
        min_odd_number_index = "No matches"
    if min_even_number_index is None:
        min_even_number_index = "No matches"

    return max_even_number_index, max_odd_number_index, min_odd_number_index, min_even_number_index




command = input()


while not command == "end":


    if "exchange" in command:
        string_of_numbers = string_of_integers_slicing(string_of_numbers, command)

    elif "max" in command:
        max_even_number_index, max_odd_number_index, min_odd_number_index, min_even_number_index = \
            max_and_min_odd_and_even_numbers(string_of_numbers)

        if "even" in command:
            print(max_even_number_index)

        elif "odd" in command:
            print(max_odd_number_index)

    elif "min" in command:
        max_even_number_index, max_odd_number_index, min_odd_number_index, min_even_number_index = \
            max_and_min_odd_and_even_numbers(string_of_numbers)
        if "even" in command:
            print(min_even_number_index)

        elif "odd" in command:
            print(min_odd_number_index)

    elif "first" in command:
        list_of_even_numbers, list_of_odd_numbers = turning_list_of_int_to_2_lists_of_odd_and_even_numbers(
            string_of_numbers)

        command = command.split(" ")
        count_of_numbers_to_shown = int(command[1])
        if count_of_numbers_to_shown > len(string_of_numbers):
            print("Invalid count")
        else:
            if "even" in command:
                print(list_of_even_numbers[:count_of_numbers_to_shown])

            elif "odd" in command:
                print(list_of_odd_numbers[:count_of_numbers_to_shown])
    elif "last" in command:
        list_of_even_numbers, list_of_odd_numbers = turning_list_of_int_to_2_lists_of_odd_and_even_numbers(
            string_of_numbers)
        command = command.split(" ")
        count_of_numbers_to_shown = int(command[1])
        if count_of_numbers_to_shown > len(string_of_numbers):
            print("Invalid count")

        else:
            if "even" in command:
                if count_of_numbers_to_shown > len(list_of_even_numbers):
                    print(list_of_even_numbers)
                else:
                    opposite_order_of_list_of_even_numbers = list_of_even_numbers[-1: count_of_numbers_to_shown*-1 -1:-1]
                    opposite_order_of_list_of_even_numbers.reverse()
                    print(opposite_order_of_list_of_even_numbers)
            elif "odd" in command:
                if count_of_numbers_to_shown > len(list_of_odd_numbers):
                    print(list_of_odd_numbers)
                else:
                    opposite_order_of_list_of_odd_numbers = list_of_odd_numbers[-1: count_of_numbers_to_shown*-1 -1: - 1]
                    opposite_order_of_list_of_odd_numbers.reverse()
                    print(opposite_order_of_list_of_odd_numbers)

    command = input()

string_of_numbers = [int(i) for i in string_of_numbers]
print(string_of_numbers)