import loader

def run_assembunny(start, a_start, rounds = 50):
    register = {'a': a_start, 'b': 0, 'c': 0, 'd': 0}
    counter = 0
    output = ''
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
        if task[0] == 'out':
            output += str(register[task[1]])
            if len(output) > 1 and output[-1] == output[-2]:
                return False
            counter += 1
            if len(output) == rounds:
                break
    return output

def part_1(start):
    counter = 1
    while True:
        result = run_assembunny(start, counter)
        if result == '01' * 25 or result == '10' * 25:
            break
        counter += 1
    return counter

start = loader.one_type_of_data('day25.txt')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')

