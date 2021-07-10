character_1 = input()
character_2 = input()

def character_to_asci_number(a):
    number_1_in_asci_table = ord(a)
    return number_1_in_asci_table


first_number = character_to_asci_number(character_1)
second_number = character_to_asci_number(character_2)

for numbers in range(first_number+1, second_number):
    if numbers < second_number-1:
        print(chr(numbers), end =" ")
    else:
        print(chr(numbers))
