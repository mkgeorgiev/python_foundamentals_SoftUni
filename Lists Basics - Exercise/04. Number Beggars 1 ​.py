string_of_numbers = input().split(", ")
beggars = int(input())
beggar_profit = 0
list_of_profits = []

for beggar in range(0, beggars):
    for numbers in range(beggar, len(string_of_numbers), beggars):
        beggar_profit += int(string_of_numbers[numbers])
    list_of_profits.append(beggar_profit)
    beggar_profit = 0
print(list_of_profits)




