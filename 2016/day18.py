def part_1(starting_row, steps):
    result = 0
    next_row = ''
    for tile in range(len(starting_row)):
        left = starting_row[tile - 1] if tile > 0 else '.'
        right = starting_row[tile + 1] if tile < len(starting_row) - 1 else '.'
        next_row += '^' if left != right else '.'
    result = starting_row.count('.')
    if steps > 0:
        result += part_1(next_row, steps - 1)
    return result

def part_2(starting_row, steps):
    result = starting_row.count('.')
    while steps > 0:
        next_row = ''
        for tile in range(len(starting_row)):
            left = starting_row[tile - 1] if tile > 0 else '.'
            right = starting_row[tile + 1] if tile < len(starting_row) - 1 else '.'
            next_row += '^' if left != right else '.'
        starting_row = next_row
        steps -= 1
        result += starting_row.count('.')
    return result

starting_row = '^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^.......'
steps = 40 - 1
print(f'Answer for part one is: {part_1(starting_row, steps)}.')
steps = 400000 - 1
print(f'Answer for part two is: {part_2(starting_row, steps)}.')
