fire_cells = input().split("#")
water_available = int(input())
effort = 0
total_fire = 0
fire_types = [["High", 81, 125], ["Medium", 51, 80], ["Low", 1, 50]]
is_fire_valid = False
print("Cells:")

for cell_index in range(len(fire_cells)):
    fire_attributes = fire_cells[cell_index].split(" = ")
    fire_power = int(fire_attributes[1])
    for fire_type in fire_types:
        if fire_attributes[0] == fire_type[0]:
            if fire_power in range(fire_type[1], fire_type[2]+1):
                is_fire_valid = True
            else:
                is_fire_valid = False
    if is_fire_valid:
        if water_available >= fire_power:
            water_available -= fire_power
            effort += 0.25 * fire_power
            total_fire += fire_power

            print(f" - {fire_power}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")



