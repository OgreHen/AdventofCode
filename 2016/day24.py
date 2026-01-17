import loader
from itertools import combinations, permutations

def create_maze(maze, a, b):
    maze_to_solve = []
    for i in maze:
        row = []
        for j in i:
            if j in ['.', '#']:
                row.append(j)
            elif j == a:
                row.append(0)
            elif j == b:
                row.append('X')
            else:
                row.append('.')
        maze_to_solve.append(row)
    return maze_to_solve

def solve_route(received_maze):
    counter = 0
    while True:
        for row in range(len(received_maze)):
            for column in range(len(received_maze[row])):
                if received_maze[row][column] == counter:
                    possible_steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for i in possible_steps:
                        if received_maze[row + i[0]][column + i[1]] == 'X':
                            return counter + 1
                        if received_maze[row + i[0]][column + i[1]] == '.':
                            received_maze[row + i[0]][column + i[1]] = counter + 1
        counter += 1

def get_numbers(maze):
    nums = []
    for row in maze:
        for column in row:
            if column not in ['.', '#']:
                nums.append(column)
    nums.sort()
    return nums

def part_1(start):
    nums = get_numbers(start)
    num_combinations = list(combinations(nums, 2))
    num_combination_values = {}
    for i in num_combinations:
        num_combination_values[i] = solve_route(create_maze(start, *i))
    nums.remove('0')
    complete_nums = list(permutations(nums))
    result = 0
    for i in range(len(complete_nums)):
        current_result = 0
        current_list = list(complete_nums[i])
        current_list.append('0')
        for j in range(len(current_list) - 1):
            current_result += num_combination_values[(min(current_list[j], current_list[j + 1]), max(current_list[j], current_list[j + 1]))]
        if current_result < result or result == 0:
            result = current_result
    return result

def part_2(start):
    nums = get_numbers(start)
    num_combinations = list(combinations(nums, 2))
    num_combination_values = {}
    for i in num_combinations:
        num_combination_values[i] = solve_route(create_maze(start, *i))
    nums.remove('0')
    complete_nums = list(permutations(nums))
    result = 0
    for i in range(len(complete_nums)):
        current_result = 0
        current_list = list(complete_nums[i])
        current_list.append('0')
        current_list.insert(0, '0')
        for j in range(len(current_list) - 1):
            current_result += num_combination_values[(min(current_list[j], current_list[j + 1]), max(current_list[j], current_list[j + 1]))]
        if current_result < result or result == 0:
            result = current_result
    return result

start = loader.one_type_of_data('day24.txt')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')
