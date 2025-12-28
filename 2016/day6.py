import loader

def part_1_and_2(start):
    positions = [[] for _ in range(len(start[0]))]
    for item in start:
        for i in range(len(start[0])):
            positions[i].append(item[i])
    result_max = ''
    result_min = ''
    for position in positions:
        result_max += max(set(position), key=position.count)
        result_min += min(set(position), key=position.count)
    return result_max, result_min


start = loader.one_type_of_data('day6.txt', '\n')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1_and_2(start)[0]}.\n'
      f'Answer for part two is: {part_1_and_2(start)[1]}')