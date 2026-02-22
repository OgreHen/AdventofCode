import loader

def part_1_and_2(start):
    regs = {}
    for i in start:
        regs[i[0]] = 0
    alltime_max = 0
    for i in start:
        if i[1] == 'inc':
            instruction = f'{i[3]} regs["{i[4]}"] {i[5]} {i[6]}:\n\tregs["{i[0]}"] = regs["{i[0]}"] + {i[2]}'
        elif i[1] == 'dec':
            instruction = f'{i[3]} regs["{i[4]}"] {i[5]} {i[6]}:\n\tregs["{i[0]}"] = regs["{i[0]}"] - {i[2]}'
        exec(instruction)
        if max(regs.values()) > alltime_max:
            alltime_max = max(regs.values())
    return max(regs.values()), alltime_max

input_data = loader.two_type_of_data('day8.txt')
print(input_data)
print(f'The answer for part 1 is: {part_1_and_2(input_data)[0]}')
print(f'The answer for part 2 is: {part_1_and_2(input_data)[1]}')
