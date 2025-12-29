import loader

def part_1_and_2(start):
    screen = [['.' for _ in range(50)] for _ in range(6)]
    def rect(width, height):
        for y in range(height):
            for x in range(width):
                screen[y][x] = '#'
    def rotate_row(row, by):
        for _ in range(by):
            fallout = screen[row][-1]
            for i in range(len(screen[row]) - 1, 0, -1):
                screen[row][i] = screen[row][i - 1]
            screen[row][0] = fallout
    def rotate_column(column, by):
        for _ in range(by):
            fallout = screen[-1][column]
            for i in range(len(screen) - 1, 0, -1):
                screen[i][column] = screen[i - 1][column]
            screen[0][column] = fallout
    for line in start:
        if 'rect' in line:
            width = int(line.split(' ')[1].split('x')[0])
            height = int(line.split(' ')[1].split('x')[1])
            rect(width, height)
        elif 'row' in line:
            row = int(line.split(' ')[2].split('=')[1])
            by = int(line.split(' ')[-1])
            rotate_row(row, by)
        elif 'column' in line:
            column = int(line.split(' ')[2].split('=')[1])
            by = int(line.split(' ')[-1])
            rotate_column(column, by)
    result = 0
    for row in screen:
        result += row.count('#')
        readable = ''
        for char in row:
            readable += char
        print(readable)
    return result

start = loader.one_type_of_data('day8.txt', '\n')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1_and_2(start)}.')
print(f'Answer for part two is: AFBUPZBJPS, seen above.')
