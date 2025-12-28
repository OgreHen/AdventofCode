import loader

def data_splitter(start):
    result = []
    for data in start:
        result.append([data[:-11], int(data[-10:-7]), data[-6:-1]])
    return result


def part_1(start):
    items = data_splitter(start)
    result = 0
    for item in items:
        letters = set(item[0])
        occurence = []
        for letter in letters:
            if letter != "-":
                occurence.append((-item[0].count(letter), letter))
        occurence.sort()
        good = True
        for check in range(5):
            if item[2][check] != occurence[check][1]:
                good = False
        if good:
            result += item[1]
    return result

def part_2(start):
    items = data_splitter(start)
    for item in items:
        text = ''
        for letter in item[0]:
            if letter == "-":
                text += "-"
            else:
                text += chr((ord(letter) - 97 + item[1]) % 26 + 97)
        if 'northpole' in text:
            return(item[1])

start = loader.one_type_of_data('day4.txt')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')