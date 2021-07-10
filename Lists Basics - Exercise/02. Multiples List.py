factor = int(input())
count = int(input())
multiples = 0
list_of_multiples = []

for number in range(1,count+1):
    multiples = number * factor
    list_of_multiples.append(multiples)

print(list_of_multiples)