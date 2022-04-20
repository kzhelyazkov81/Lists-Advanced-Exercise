def shoot(index, power):
    if -1 < index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add(index, value):
    if -1 < index < len(targets):
        targets.insert(index, value)
    else:
        print('Invalid placement!')
    return targets


def strike(index, radius):
    start_target = index - radius
    end_target = index + radius
    if -1 < start_target < len(targets) and end_target < len(targets):
        for i in range(end_target, start_target - 1, -1):
            targets.pop(i)
    else:
        print('Strike missed!')
    return targets


targets = list(map(int, input().split(' ')))

while True:
    command = input().split(' ')
    if command[0] == 'End':
        break
    if command[0] == 'Shoot':
        targets = shoot(int(command[1]), int(command[2]))
    elif command[0] == 'Add':
        targets = add(int(command[1]), int(command[2]))
    elif command[0] == 'Strike':
        targets = strike(int(command[1]), int(command[2]))

targets = list(map(str, targets))
print('|'.join(targets))
