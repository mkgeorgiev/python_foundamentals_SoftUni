number = int(input())


def is_number_perfect(a):
    sum_of_divisors = 0
    for divisors in range (1, a):
        if a % divisors == 0:
            sum_of_divisors += divisors
    if sum_of_divisors == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


is_number_perfect(number)
