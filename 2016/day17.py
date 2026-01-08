import hashlib

def step_possibilities(to_hash):
    hashed = str(hashlib.md5(to_hash.encode()).hexdigest())
    result = []
    good_ones = ['b', 'c', 'd', 'e', 'f']
    directions = ['U', 'D', 'L', 'R']
    for i in range(4):
        if hashed[i] in good_ones:
            result.append(directions[i])
    return result

def part_1(starting_string, steps_made):
    possibilities = step_possibilities(starting_string + steps_made)
    if not possibilities:
        return ''
    result = 'a' * 1000
    for possibility in possibilities:
        current = steps_made + possibility
        horizontal_location = current.count('R') - current.count('L')
        vertical_location = current.count('D') - current.count('U')
        if horizontal_location == vertical_location == 3:
            return current
        elif 0 <= horizontal_location <= 3 and 0 <= vertical_location <= 3:
            calculated = part_1(starting_string, current)
            if 0 < len(calculated) < len(result):
                result = calculated
    return result

def part_2(starting_string, steps_made):
    possibilities = step_possibilities(starting_string + steps_made)
    if not possibilities:
        return 0
    result = 0
    for possibility in possibilities:
        current = steps_made + possibility
        horizontal_location = current.count('R') - current.count('L')
        vertical_location = current.count('D') - current.count('U')
        if horizontal_location == vertical_location == 3:
            if len(current) > result:
                result = len(current)
        elif 0 <= horizontal_location <= 3 and 0 <= vertical_location <= 3:
            calculated = part_2(starting_string, current)
            if calculated > result:
                result = calculated
    return result


starting_string = 'vwbaicqe'
print(f'Answer for part one is: {part_1(starting_string, '')}.')
print(f'Answer for part two is: {part_2(starting_string, '')}.')
