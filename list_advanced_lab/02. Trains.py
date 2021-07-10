train = [0 * number_of_wagons for number_of_wagons in range(int(input()))]
command = input().split()
while not "End" in command:
    if "add" == command[0]:
        train[-1] += int(command[1])
    elif "insert" == command[0]:
        train[int(command[1])] += int(command[2])
    elif "leave" == command[0]:
        train[int(command[1])] -= int(command[2])
    command = input().split()

print(train)