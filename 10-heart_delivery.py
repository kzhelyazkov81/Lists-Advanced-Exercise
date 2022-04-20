def representation(last_position, data):
    print(f"Cupid's last position was {last_position}.")
    result = [x for x in data if x == 0]
    if len(result) != len(data):
        diff = abs(len(result) - len(data))
        print(f'Cupid has failed {diff} places.')
    else:
        print('Mission was successful.')


def heart_delivery(data):
    current_index_position = 0
    cupid_last_position = 0

    while True:
        command = input().split(' ')
        if command[0] == 'Love!':
            break
        index = int(command[1])
        index += current_index_position
        if index >= len(data):
            index = 0
        if -1 < index < len(data):
            if data[index] == 0:
                print(f"Place {index} already had Valentine's day.")
            else:
                data[index] -= 2
                if data[index] == 0:
                    print(f"Place {index} has Valentine's day.")
        current_index_position = index
        cupid_last_position = index
    representation(cupid_last_position, data)


nums = list(map(int, input().split('@')))
heart_delivery(nums)
