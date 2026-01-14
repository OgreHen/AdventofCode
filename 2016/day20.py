import loader

def part_1(start):
    start.sort()
    lowest_range = start[0].copy()
    for row in start:
        if row[0] <= lowest_range[1] <= row[1]:
            lowest_range[1] = row[1]
    return lowest_range[1] + 1

def part_2(start):
    start += [[0, 0], [4294967295, 4294967295]]
    start.sort()
    new_ranges = [start[0]]
    result = 0
    for row in start:
        if new_ranges[-1][0] <= row[0] <= new_ranges[-1][1] + 1:
            if new_ranges[-1][1] < row[1]:
                new_ranges[-1][1] = row[1]
        else:
            new_ranges.append(row)
            result += new_ranges[-1][0] - new_ranges[-2][1] - 1
    return result

start = loader.two_type_of_data('day20.txt',  '\n', '-')
for row in range(len(start)):
    for item in range(len(start[row])):
        start[row][item] = int(start[row][item])
print(start)
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')
