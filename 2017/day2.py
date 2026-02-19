import pandas as pd

def part_1(start):
    result = sum(start.max(axis=1)) - sum(start.min(axis=1))
    return result

def part_2(start):
    result = 0
    np_array = start.to_numpy()
    result = 0
    for row in np_array:
        for col_num in range(len(row)):
            for col_num2 in range(len(row)):
                if col_num != col_num2 and row[col_num] % row[col_num2] == 0:
                    result += int(row[col_num] / row[col_num2])
    return result


input_data = pd.read_csv('day2.csv', delimiter = '\t', header = None)
# print(input_data)
print(f'The answer for part 1 is: {part_1(input_data)}')
print(f'The answer for part 2 is: {part_2(input_data)}')