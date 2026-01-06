import loader

def part_1_and_2(start, c_start = 0):
    register = {'a': 0, 'b': 0, 'c': c_start, 'd': 0}
    counter = 0
    while counter < len(start):
        task = start[counter].split(' ')
        if task[0] == 'cpy':
            try:
                register[task[2]] = register[task[1]]
            except:
                register[task[2]] = int(task[1])
            counter += 1
        if task[0] == 'inc':
            register[task[1]] += 1
            counter += 1
        if task[0] == 'dec':
            register[task[1]] -= 1
            counter += 1
        if task[0] == 'jnz':
            try:
                if register[task[1]] == 0:
                    counter += 1
                else:
                    counter += int(task[2])
            except:
                if task[1] == '0':
                    counter += 1
                else:
                    counter += int(task[2])
    return register['a']

start = loader.one_type_of_data('day12.txt')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1_and_2(start)}.')
print(f'Answer for part two is: {part_1_and_2(start, 1)}.')
