import loader

def part_1(start):
    result = 0
    for line in start:
        if len(line) == len(set(line)):
            result += 1
    return result

def part_2(start):
    result = 0
    for line in range(len(start)):
        good = True
        for word in range(len(start[line]) - 1):
            for second_word in range(word + 1, len(start[line])):
                if set(start[line][word]) == set(start[line][second_word]):
                    good = False
                    break
        if good: result += 1
    return result

input_data = loader.two_type_of_data('day4.txt')
# print(input_data)
print(f'The answer for part 1 is: {part_1(input_data)}')
print(f'The answer for part 2 is: {part_2(input_data)}')
