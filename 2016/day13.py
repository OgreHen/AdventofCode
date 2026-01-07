def location_calculation(x, y):
    result = x ** 2 + 3 * x + 2 * x * y + y + y ** 2 + input_number
    ones = 0
    for number in bin(result):
        if number == '1':
            ones += 1
    return '.' if ones % 2 == 0 else '#'

def create_maze(width, height):
    maze = []
    for y in range(0, height):
        row = []
        for x in range(0, width):
            row += location_calculation(x, y)
        maze.append(row)
    return maze

def part_1(goal_x, goal_y):
    maze_to_solve = create_maze(50, 50)
    maze_to_solve[1][1] = 0
    counter = 0
    while maze_to_solve[goal_y][goal_x] == '.':
        for y in range(len(maze_to_solve)):
            for x in range(len(maze_to_solve[y])):
                if maze_to_solve[y][x] == counter:
                    to_check = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]
                    for i in to_check:
                        if 0 <= i[0] < len(maze_to_solve) and 0 <= i[1] < len(maze_to_solve[y]):
                            if maze_to_solve[i[0]][i[1]] == '.':
                                maze_to_solve[i[0]][i[1]] = counter + 1
        counter += 1
    return counter

def part_2(goal):
    maze_to_solve = create_maze(50, 50)
    maze_to_solve[1][1] = 0
    counter = 0
    locations = 1
    while counter < goal:
        for y in range(len(maze_to_solve)):
            for x in range(len(maze_to_solve[y])):
                if maze_to_solve[y][x] == counter:
                    to_check = [[y - 1, x], [y + 1, x], [y, x - 1], [y, x + 1]]
                    for i in to_check:
                        if 0 <= i[0] < len(maze_to_solve) and 0 <= i[1] < len(maze_to_solve[y]):
                            if maze_to_solve[i[0]][i[1]] == '.':
                                maze_to_solve[i[0]][i[1]] = counter + 1
                                locations += 1
        counter += 1
    return locations

input_number = 1350
print(f'Answer for part one is: {part_1(31, 39)}.')
print(f'Answer for part two is: {part_2(50)}.')
