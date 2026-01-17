import loader

def part_1_and_2(start, a_start):
    register = {'a': a_start, 'b': 0, 'c': 0, 'd': 0}
    counter = 0
    while counter < len(start):
        if start[counter][0] == 'cpy':
            if start[counter][1] in register:
                register[start[counter][2]] = register[start[counter][1]]
            else:
                register[start[counter][2]] = int(start[counter][1])
            counter += 1
        elif start[counter][0] == 'inc':
            register[start[counter][1]] += 1
            counter += 1
        elif start[counter][0] == 'dec':
            register[start[counter][1]] -= 1
            counter += 1
        elif start[counter][0] == 'jnz':
            if start[counter][1] in register:
                part_x = register[start[counter][1]]
            else:
                part_x = int(start[counter][1])
            if part_x == 0:
                counter += 1
            else:
                if start[counter][2] in register:
                    counter += register[start[counter][2]]
                else:
                    counter += int(start[counter][2])
        elif start[counter][0] == 'tgl':
            toggle = {'inc': 'dec', 'dec': 'inc', 'tgl': 'inc', 'jnz': 'cpy', 'cpy': 'jnz'}
            if start[counter][1] in register:
                to_change = counter + register[start[counter][1]]
            else:
                to_change = counter + int(start[counter][1])
            if 0 <= to_change < len(start):
                start[to_change][0] = toggle[start[to_change][0]]
            counter += 1
        print(counter, register)
    return register['a']

start = loader.two_type_of_data('day23.txt')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1_and_2(start, 7)}.')
start = loader.two_type_of_data('day23.txt')
print(f'Answer for part two is: {part_1_and_2(start, 12)}.')


# This code is horribly slow for the second part (ran overnight), should use multiplication for loops.

# Answer for part two is: 479009184.
