def electron_ditribution(number):
    filled_shells = []
    shell_number = 1
    while True:
        element = 2*(shell_number**2)
        if element < number:
            number -= element
            filled_shells.append(element)
            shell_number += 1
        else:
            filled_shells.append(number)
            break
    print(filled_shells)


number_of_electrones = int(input())
electron_ditribution(number_of_electrones)

