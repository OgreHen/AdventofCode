import loader

def convert_data(start):
    result = []
    for row in range(2, len(start)):
        while '  ' in start[row]:
            start[row] = start[row].replace('  ', ' ')
        parts = start[row].split(' ')
        coordinates = parts[0].split('-')
        x = int(coordinates[1][1:])
        y = int(coordinates[2][1:])
        size = int(parts[1][:-1])
        used = int(parts[2][:-1])
        avail = int(parts[3][:-1])
        used_percent = int(parts[4][:-1])
        result.append([(x, y), size, used, avail, used_percent])
    return result

def part_1(start):
    result = 0
    for i in start:
        if i[2] != 0:
            for j in start:
                if i[0] == j[0]:
                    continue
                if i[2] <= j[3]:
                    result += 1
    return result

def easier_grid(start):
    '''
    Used for visualization only, part_2 solution was worked out based on it.
    '''
    max_x = 0
    max_y = 0
    for location in start:
        if location[0][0] > max_x:
            max_x = location[0][0]
        if location[0][1] > max_y:
            max_y = location[0][1]
    print(max_x, max_y)
    map = [['.' for x in range(max_y + 1)] for y in range(max_x + 1)]
    for location in start:
        if location[1] > 500:
            map[location[0][0]][location[0][1]] = -1
            print(location)
        elif location[2] == 0:
            map[location[0][0]][location[0][1]] = 0
            print(location)
        else:
            map[location[0][0]][location[0][1]] = 1
    map[max_x][0] = 2
    for i in map:
        print(i)

def part_2(start):
    '''
    Find the maximum of x => 29
    Find the location with the movable (empty) storage => (11, 22)
    Find the location with min x having a giant => 21

    Move above the rows with giants => movable_x - giant_x + 1 => (7, 22)
    Move to the left wall => movable_y => (7, 0)
    Move above the 2 => max_x - giant_x => (28, 0)
    Snake up to row 1 => 5 * (max_x - 1) => (0, 0)
        (1 snake move takes 5 steps: down, right, up, up, left)
    Move once more to the final desination => 1 => (1, 0)
    '''
    max_x = 0
    giant_x = 100
    for location in start:
        if location[1] > 500:
            if giant_x > location[0][0]:
                giant_x = location[0][0]
        if location[2] == 0:
            movable_x = location[0][0]
            movable_y = location[0][1]
        if location[0][0] > max_x:
            max_x = location[0][0]
    result = movable_x - giant_x + 1
    result += movable_y
    result += max_x - giant_x
    result += 5 * (max_x - 1)
    result += 1
    return result

start = loader.one_type_of_data('day22.txt')
print(start)
converted_start = convert_data(start)
print(f'Answer for part one is: {part_1(converted_start)}.')
print(f'Answer for part two is: {part_2(converted_start)}.')

# easier_grid(converted_start)

