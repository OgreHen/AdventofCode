def calculate_checksum(number):
    while len(number) % 2 == 0:
        result = ''
        for i in range(int(len(number) / 2)):
            if number[i * 2] == number[i * 2 + 1]:
                result += '1'
            else:
                result += '0'
        number = result
    return number

def part_1_and_2(start, required_length):
    while len(start) < required_length:
        a = start
        b = ''
        for i in a[::-1]:
            if i == '1':
                b += '0'
            else:
                b += '1'
        start = a + '0' + b
    result = calculate_checksum(start[:required_length])
    return result

start = '00111101111101000'
required_length = 272
print(f'Answer for part one is: {part_1_and_2(start, required_length)}.')
required_length = 35651584
print(f'Answer for part two is: {part_1_and_2(start, required_length)}.')
