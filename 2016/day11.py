import loader

def data_converter(start):
    result = []
    for floor in start:
        info = floor.split(' ')
        current_floor = []
        for i in range(len(info)):
            if info[i] == 'floor':
                current_floor.append(info[i - 1] + ' ' + info[i])
            if (info[i].replace(',', '').replace('.', '') == 'generator' or
                info[i].replace(',', '').replace('.', '') == 'microchip'):
                current_floor.append(info[i - 1] + ' ' + info[i].replace(',', '').replace('.', ''))
        result.append(current_floor)
    return result

start = loader.one_type_of_data('day11.txt')
print(f'Starting data: {start}')
data = data_converter(start)
print('Starting data cleared:')
for i in data:
    print(i)
# print(f'Answer for part one is: {part_1(start)}.')
# print(f'Answer for part two is: {part_2(start)}.')
