import loader

def splitter(start):
    should = []
    shouldnt = []
    current = ''
    for letter in start:
        if letter == '[':
            if current != '':
                should.append(current)
            current = ''
        else:
            current += letter
        if letter == ']':
            shouldnt.append(current[:-1])
            current = ''
    should.append(current)
    return should, shouldnt

def abba_checker(input):
    for i in range(len(input) - 3):
        if input[i] == input[i + 3] and input [i + 1] == input[i + 2] and input[i] != input[i + 1]:
            return True
    return False

def part_1(start):
    result = 0
    for item in start:
        should, shouldnt = splitter(item)
        should_check = False
        for item in should:
            if abba_checker(item):
                should_check = True
        shouldnt_check = False
        for item in shouldnt:
            if abba_checker(item):
                shouldnt_check = True
        if should_check and not shouldnt_check:
            result += 1
    return result

def aba_checker(input):
    result = []
    for i in range(len(input) - 2):
        if input[i] == input[i + 2] and input[i] != input[i + 1]:
            result.append(input[i:i + 3])
    return result

def part_2(start):
    result = 0
    for item in start:
        outer, inner = splitter(item)
        outer_aba = []
        for part in outer:
            outer_aba += aba_checker(part)
        inner_aba = []
        for part in inner:
            inner_aba += aba_checker(part)
        found = False
        for aba in outer_aba:
            if aba != []:
                if (aba[1] + aba[0] + aba[1]) in inner_aba:
                    found = True
        if found:
            result += 1
    return result

start = loader.one_type_of_data('day7.txt', '\n')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')
