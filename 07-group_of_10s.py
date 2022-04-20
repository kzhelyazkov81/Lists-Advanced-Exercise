numbers = list(map(int, input().split(', ')))
boundary = 0
while len(numbers) > 0:
    boundary += 10
    group = list(filter(lambda x: x <= boundary, numbers))
    numbers = list(filter(lambda x: x > boundary, numbers))
    print(f"Group of {boundary}'s: {group}")
