password_input = input()


def is_password_valid(a):

    digit_count = 0

    is_password_long_enough = False
    does_password_contains_only_letters_and_digits = False
    does_password_contains_at_least_2_digits = False

    if len(password_input) in range(6, 11):
        is_password_long_enough = True

    if password_input.isalnum():
        does_password_contains_only_letters_and_digits = True

    for char in range(len(password_input)):
        if password_input[char].isdigit():
            digit_count += 1
    if digit_count >= 2:
        does_password_contains_at_least_2_digits = True

    if not is_password_long_enough:
        print("Password must be between 6 and 10 characters")

    if not does_password_contains_only_letters_and_digits:
        print("Password must consist only of letters and digits")

    if not does_password_contains_at_least_2_digits:
        print("Password must have at least 2 digits")

    if is_password_long_enough and does_password_contains_only_letters_and_digits and \
            does_password_contains_at_least_2_digits:
        print("Password is valid")


is_password_valid(password_input)
