num_of_wagons = int(input())
train = num_of_wagons * [0]
command = input()
while command != "End":
    command = command.split()
    if command[0] == "add":
        train[-1] += int(command[1])
    elif command[0] == "insert":
        train[int(command[1])] += int(command[2])
    elif command[0] == "leave":
        train[int(command[1])] -= int(command[2])
    command = input()
print(train)
