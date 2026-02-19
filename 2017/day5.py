import loader

def part_1(start):
    working = []
    for i in start:
        working.append(int(i))
    current = 0
    steps = 0
    while len(start) - 1 >= current >= 0:
        stepped = current + working[current]
        working[current] += 1
        current = stepped
        steps += 1
    return steps

def part_2(start):
    working = []
    for i in start:
        working.append(int(i))
    current = 0
    steps = 0
    while len(start) - 1 >= current >= 0:
        stepped = current + working[current]
        if working[current] >= 3:
            working[current] -= 1
        else:
            working[current] += 1
        current = stepped
        steps += 1
    return steps

input_data = loader.one_type_of_data('day5.txt')
print(input_data)
print(f'The answer for part 1 is: {part_1(input_data)}')
print(f'The answer for part 2 is: {part_2(input_data)}')
