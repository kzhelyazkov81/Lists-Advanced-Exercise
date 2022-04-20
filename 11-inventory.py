def collect(inventory, item):
    if item not in inventory:
        inventory.append(item)
    return inventory


def drop(inventory, item):
    if item in inventory:
        inventory.remove(item)
    return inventory


def combine_items(inventory, item):
    item = item.split(':')
    if item[0] in inventory:
        old_item_index = inventory.index(item[0])
        inventory.insert(old_item_index+1, item[1])
    return inventory


def renew(inventory, item):
    if item in inventory:
        inventory.remove(item)
        inventory.append(item)
    return inventory


collecting_items = input().split(', ')
while True:
    command = input().split(' - ')
    if command[0] == 'Collect':
        collecting_items = collect(collecting_items, command[1])
    elif command[0] == 'Drop':
        collecting_items = drop(collecting_items, command[1])
    elif command[0] == 'Combine Items':
        collecting_items = combine_items(collecting_items, command[1])
    elif command[0] == 'Renew':
        collecting_items = renew(collecting_items, command[1])
    elif command[0] == 'Craft!':
        break

result = ', '.join(collecting_items)
print(result)
