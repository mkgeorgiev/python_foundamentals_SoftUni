def calculations(operator, num_1, num_2):
    if operator == "multiply":
        result = num_1 * num_2
        return result
    elif operator == "divide":
        result = num_1 / num_2
        return result
    elif operator == "add":
        result = num_1 + num_2
        return result
    elif operator == "subtract":
        result = num_1 - num_2
        return result

operation = input()
first_number = int(input())
second_number = int(input())

print(int(calculations(operation, first_number, second_number)))