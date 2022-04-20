def decipher(sequence):
    result = []
    for word in sequence:
        first_letter = list(filter(lambda x: x if 47 < ord(x) < 58 else '', word))
        word = list(filter(lambda x: x if ord(x) < 48 or ord(x) > 57 else '', word))
        first_letter = chr(int(''.join(first_letter)))
        word[0], word[-1] = word[-1], word[0]
        word.insert(0, first_letter)
        result.append(''.join(word))
    print(' '.join(result))


message = input().split(' ')
decipher(message)
