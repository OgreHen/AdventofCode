import hashlib

def part_1(start):
    runner = -1
    result = ''
    while len(result) != 8:
        runner += 1
        current = hashlib.md5((start + str(runner)).encode()).hexdigest()
        if current[:5] == '00000':
            result += current[5]
    return result

def part_2(start):
    runner = -1
    result = ['_']  * 8
    while '_' in result:
        runner += 1
        current = hashlib.md5((start + str(runner)).encode()).hexdigest()
        if current[:5] == '00000':
            if current[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
                if result[int(current[5])] == '_':
                    result[int(current[5])] = current[6]
    string = ''
    for item in result:
        string += str(item)
    return string

start = 'uqwqemis'
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')
