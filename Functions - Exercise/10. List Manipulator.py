string_of_numbers = input().split(" ")


def commands_for_string_of_numbers(list_of_integers, command):
    if "exchange" in command:
        slice_number = int(command[-1])
        left_part = list_of_integers[:slice_number+1]
        right_part = list_of_integers[slice_number+1:]
        list_of_integers = right_part + left_part

        return list_of_integers

    if "max" in command:
        if "even" in command:
            for number in list_of_integers:
                if number % 2 == 0:
                    list_of_even_numbers =[]
                    list_of_even_numbers.append(number)
        elif "odd" in command:

command = input()

while not command == "end":
    commands_for_string_of_numbers(string_of_numbers, command)
    command = input()