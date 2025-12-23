import loader
import numpy as np

def part_1(start):
    position_horizontal = 1
    position_vertical = 1
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    code = 0
    for push in start:
        for step in push:
            if step == 'U' and position_vertical != 0:
                position_vertical -= 1
            if step == 'D' and position_vertical != 2:
                position_vertical += 1
            if step == 'L' and position_horizontal != 0:
                position_horizontal -= 1
            if step == 'R' and position_horizontal != 2:
                position_horizontal += 1
        code = code * 10
        code += keypad[position_vertical][position_horizontal]
    return code

def part_2(start):
    current_location = [2, 0]
    keypad = [['X', 'X', '1', 'X', 'X'],
              ['X', '2', '3', '4', 'X'],
              ['5', '6', '7', '8', '9'],
              ['X', 'A', 'B', 'C', 'X'],
              ['X', 'X', 'D', 'X', 'X']]
    code = ''
    for push in start:
        for step in push:
            if step == 'U':
                new_location = [current_location[0] - 1, current_location[1]]
            if step == 'D':
                new_location = [current_location[0] + 1, current_location[1]]
            if step == 'L':
                new_location = [current_location[0], current_location[1] - 1]
            if step == 'R':
                new_location = [current_location[0], current_location[1] + 1]
            if 0 <= new_location[0] <= 4 and 0 <= new_location[1] <= 4:
                if keypad[new_location[0]][new_location[1]] != 'X':
                    current_location = new_location
        code += keypad[current_location[0]][current_location[1]]
    return code

start = loader.one_type_of_data('day2.txt')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')
