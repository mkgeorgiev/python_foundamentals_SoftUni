str_list_of_gifts = input().split()
command = input()

while not command == "No Money":
    if "OutOfStock" in command:
        new_item = command[11:]
        if new_item in str_list_of_gifts:
            count_of_new_item_in_list_of_gifts = str_list_of_gifts.count(new_item)
            for times_in_list in range(count_of_new_item_in_list_of_gifts):
                index_of_new_item = str_list_of_gifts.index(new_item)
                str_list_of_gifts.remove(new_item)
                str_list_of_gifts.insert(index_of_new_item, "None")

    elif "Required" in command:
        command = command.split()
        new_item = command[1]
        value = int(command[2])
        # if command[-2] == "-":
        #     new_item = command[9:-3]
        #     value = int(command[-2:])
        #
        # else:
        #     new_item = command[9:-2]
        #     value = int(command[-1])
        #     length_of_gift_list = len(str_list_of_gifts)
        if 0 <= value <= len(str_list_of_gifts)-1:
            str_list_of_gifts[value] = new_item
    elif "JustInCase" in command:
        new_item = command[11:]
        str_list_of_gifts.pop(-1)
        str_list_of_gifts.append(new_item)

    command = input()

if "None" in str_list_of_gifts:
    count_of_none = str_list_of_gifts.count("None")
    for none_times_in_list in range(count_of_none):
        str_list_of_gifts.remove("None")

for item in range(len(str_list_of_gifts)):
    print(str_list_of_gifts[item], end=" ")
