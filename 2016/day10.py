import loader

def part_1(start):
    bots = {} # {'bot' + number: [first number, second number]}
    give = {}
    for instruction in start:
        if 'value' in instruction:
            aim_bot = 'bot' + instruction.split(' ')[-1]
            value = instruction.split(' ')[1]
            # exists = False
            if aim_bot in bots.keys():
                bots[aim_bot] = [bots[aim_bot][0], int(value)]
            else:
                bots[aim_bot] = [int(value)]
        else:
            giving_bot = 'bot' + instruction.split(' ')[1]
            low_receiver = instruction.split(' ')[5] + instruction.split(' ')[6]
            high_receiver = instruction.split(' ')[-2] + instruction.split(' ')[-1]
            give[giving_bot] = [low_receiver, high_receiver]
    def give_numbers(bot):
        low_receiver = give[bot][0]
        high_receiver = give[bot][1]
        if low_receiver in bots.keys():
            old_value = bots[low_receiver][0]
            bots[low_receiver] = [old_value, min(bots[bot])]
        else:
            bots[low_receiver] = [min(bots[bot])]
        if high_receiver in bots.keys():
            old_value = bots[high_receiver][0]
            bots[high_receiver] = [old_value, max(bots[bot])]
        else:
            bots[high_receiver] = [max(bots[bot])]
        del bots[bot]
    while True:
        for i in bots.keys():
            if len(bots[i]) == 2:
                if 17 in bots[i] and 61 in bots[i]:
                    print(i, bots[i])
                    return i
                give_numbers(i)
                break

def part_2(start):
    bots = {} # {'bot' + number: [first number, second number]}
    give = {}
    for instruction in start:
        if 'value' in instruction:
            aim_bot = 'bot' + instruction.split(' ')[-1]
            value = instruction.split(' ')[1]
            # exists = False
            if aim_bot in bots.keys():
                bots[aim_bot] = [bots[aim_bot][0], int(value)]
            else:
                bots[aim_bot] = [int(value)]
        else:
            giving_bot = 'bot' + instruction.split(' ')[1]
            low_receiver = instruction.split(' ')[5] + instruction.split(' ')[6]
            high_receiver = instruction.split(' ')[-2] + instruction.split(' ')[-1]
            give[giving_bot] = [low_receiver, high_receiver]
    def give_numbers(bot):
        low_receiver = give[bot][0]
        high_receiver = give[bot][1]
        if low_receiver in bots.keys():
            old_value = bots[low_receiver][0]
            bots[low_receiver] = [old_value, min(bots[bot])]
        else:
            bots[low_receiver] = [min(bots[bot])]
        if high_receiver in bots.keys():
            old_value = bots[high_receiver][0]
            bots[high_receiver] = [old_value, max(bots[bot])]
        else:
            bots[high_receiver] = [max(bots[bot])]
        del bots[bot]
    while True:
        if 'output0' in bots.keys() and 'output1' in bots.keys() and 'output2' in bots.keys():
            return sum(bots['output0']) * sum(bots['output1']) * sum(bots['output2'])
        for i in bots.keys():
            if len(bots[i]) == 2:
                give_numbers(i)
                break

start = loader.one_type_of_data('day10.txt')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')
