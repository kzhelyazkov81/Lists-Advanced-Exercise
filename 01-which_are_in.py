first_list = input().split(', ')
second_list = input()

new_list = [el for el in first_list if el in second_list]

print(new_list)