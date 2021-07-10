str_list_events = input().split("|")
coins = 100
current_energy = 100
energy_needed_to_complete_order = 30
max_energy = 100
if_all_events_are_complete = True

for every_event in range(len(str_list_events)):
    str_list_every_event = str_list_events[every_event]
    command_and_value = str_list_every_event.split("-")
    if command_and_value[0] == "rest":
        if current_energy + int(command_and_value[1]) <= max_energy:
            current_energy += int(command_and_value[1])
            print(f"You gained {command_and_value[1]} energy.")
            print(f"Current energy: {current_energy}.")
        else:
            print(f"You gained {max_energy - current_energy} energy.")
            current_energy = max_energy
            print(f"Current energy: {current_energy}.")
    elif command_and_value[0] == "order":
        if current_energy >= energy_needed_to_complete_order:
            current_energy -= energy_needed_to_complete_order
            coins += int(command_and_value[1])
            print(f"You earned {command_and_value[1]} coins.")
        else:
            if current_energy + 50 <= max_energy:
                current_energy += 50
            else:
                current_energy = max_energy
            print(f"You had to rest!")
            if_all_events_are_complete = False

    else:
        if coins - int(command_and_value[1]) > 0:
            coins -= int(command_and_value[1])
            print(f"You bought {command_and_value[0]}.")
        else:
            print(f"Closed! Cannot afford {command_and_value[0]}.")
            if_all_events_are_complete = False
            break
if if_all_events_are_complete:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")
