from math import log

def part_1(circle_size):
    return 1 + (circle_size - 2 ** int(log(circle_size, 2))) * 2

def part_2(circle_size):
    base = int(log(circle_size - 1, 3))
    result = 1 + circle_size - 1 - 3 ** base
    result += max((circle_size) - 2 * 3 ** base, 0)
    return result

circle_size = 3004953
print(f'Answer for part one is: {part_1(circle_size)}.')
print(f'Answer for part two is: {part_2(circle_size)}.')
