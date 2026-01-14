import loader

def swap_position(input, position_x, position_y):
    as_list = list(input)
    as_list[position_x], as_list[position_y] = as_list[position_y], as_list[position_x]
    output = ''
    for item in as_list:
        output += item
    return output

def swap_letter(input, letter_x, letter_y):
    first = input.replace(letter_x, '.')
    second = first.replace(letter_y, letter_x)
    output = second.replace('.', letter_y)
    return output

def rotate_steps(input, direction, steps):
    if direction == 'left':
        return input[steps:] + input[:steps]
    if direction == 'right':
        return input[len(input) - steps:] + input[:len(input) - steps]
    else:
        raise ValueError

def rotate_letter(input, letter):
    steps = input.index(letter)
    steps += 1 if steps < 4 else 2
    return rotate_steps(input, 'right', steps)

def rotate_letter_backwards(input, letter):
    steps = input.index(letter)
    steps_to_take = {1: 1, 3: 2, 5: 3, 7: 4, 2: 6, 4: 7, 6: 8, 0: 1}
    return rotate_steps(input, 'left', steps_to_take[steps])

def reverse(input, position_x, position_y):
    result = input[:min(position_x, position_y)]
    result += input[min(position_x, position_y):max(position_x, position_y) + 1][::-1]
    result += input[max(position_x, position_y) + 1:]
    return result

def move_position(input, position_x, position_y):
    outtake = input[position_x]
    first = input[:position_x] + input[position_x + 1:]
    result = first[:position_y] + outtake + first[position_y:]
    return result

def part_1(start, starting_string):
    result = starting_string
    for instruction in start:
        parts = instruction.split(' ')
        if parts[0] == 'swap':
            if parts[1] == 'position':
                result = swap_position(result, int(parts[2]), int(parts[-1]))
            if parts[1] == 'letter':
                result = swap_letter(result, parts[2], parts[-1])
        elif parts[0] == 'rotate':
            if parts[1] == 'based':
                result = rotate_letter(result, parts[-1])
            else:
                result = rotate_steps(result, parts[1], int(parts[2]))
        elif parts[0] == 'reverse':
            result = reverse(result, int(parts[2]), int(parts[-1]))
        else:
            result = move_position(result, int(parts[2]), int(parts[-1]))
    return result

def part_2(start, starting_string):
    result = starting_string
    for instruction in start[::-1]:
        parts = instruction.split(' ')
        if parts[0] == 'swap':
            if parts[1] == 'position': #same
                result = swap_position(result, int(parts[2]), int(parts[-1]))
            if parts[1] == 'letter': #same
                result = swap_letter(result, parts[2], parts[-1])
        elif parts[0] == 'rotate':
            if parts[1] == 'based': #new function with reversing direction and dictionary
                result = rotate_letter_backwards(result, parts[-1])
            else: #switch direction
                direction = 'right' if parts[1] == 'left' else 'left'
                result = rotate_steps(result, direction, int(parts[2]))
        elif parts[0] == 'reverse': #same
            result = reverse(result, int(parts[2]), int(parts[-1]))
        else: #switch direction
            result = move_position(result, int(parts[-1]), int(parts[2]))
    return result

start = loader.one_type_of_data('day21.txt')
print(start)
starting_string = 'abcdefgh'
starting_string_2 = 'fbgdceah'
print(f'Answer for part one is: {part_1(start, starting_string)}.')
print(f'Answer for part two is: {part_2(start, starting_string_2)}.')
