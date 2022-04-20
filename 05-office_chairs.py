def office_management(number_of_rooms):
    left_chairs = 0
    condition = True
    for room_number in range(1, number_of_rooms+1):
        data = input().split(' ')
        difference = len(data[0]) - int(data[1])
        if difference >= 0:
            left_chairs += difference
        else:
            print(f'{abs(difference)} more chairs needed in room {room_number}')
            condition = False
    if condition:
        print(f'Game On, {left_chairs} free chairs left')


info = int(input())
office_management(info)
