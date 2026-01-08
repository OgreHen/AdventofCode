import loader

def part_1(discs):
    counter = 0
    falling = False
    while not falling:
        falling = True
        for disc in discs:
            if (counter + disc[0] + disc[2]) % disc[1] != 0:
                falling = False
        counter += 1
    return counter - 1

def part_2(discs):
    discs.append([7, 11, 0])
    counter = 0
    falling = False
    while not falling:
        falling = True
        for disc in discs:
            if (counter + disc[0] + disc[2]) % disc[1] != 0:
                falling = False
        counter += 1
    return counter - 1

start = loader.one_type_of_data('day15.txt')
starting_positions = []
for i in start:
    row = i.split(' ')
    starting_positions.append([int(row[1][1:]), int(row[3]), int(row[-1][:-1])])
print(f'Starting data: {starting_positions}')
print(f'Answer for part one is: {part_1(starting_positions)}.')
print(f'Answer for part two is: {part_2(starting_positions)}.')
