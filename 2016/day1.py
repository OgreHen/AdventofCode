import loader

def part_1_and_2(start):
    direction = 0 #directions = North, East, South, West]
    n_s = 0 #nort-south
    e_w = 0 #east-west
    coordinates = [[0, 0]] #visited locations
    location = [] #location of the HQ for the second part
    for step in start:
        if step[0] == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        if direction == 0:
            n_s += int(step[1:])
        elif direction == 1:
            e_w += int(step[1:])
        elif direction == 2:
            n_s -= int(step[1:])
        else:
            e_w -= int(step[1:])
        coordinates.append([e_w, n_s])
    location = [0, 0]
    return abs(n_s) + abs(e_w), abs(location[0]) + abs(location[1])


start = loader.one_line_loader("day1.txt", ', ')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1_and_2(start)[0]}.\n'
      f'Answer for part two is: {part_1_and_2(start)[1]}')

#274+