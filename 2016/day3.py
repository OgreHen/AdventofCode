import loader

def part_1(start):
    possible = 0
    for triangles in start:
        a = int(triangles[0:5])
        b = int(triangles[5:10])
        c = int(triangles[10:])
        if a + b > c and a + c > b and b + c > a:
            possible += 1
    return possible

def part_2(start):
    triangles = []
    for row in start:
        a = int(row[0:5])
        b = int(row[5:10])
        c = int(row[10:])
        triangles.append([a, b, c])
    possible = 0
    counter = 0
    while counter < len(triangles):
        for j in range(3):
            a = triangles[counter][j]
            b = triangles[counter + 1][j]
            c = triangles[counter + 2][j]
            if a + b > c and a + c > b and b + c > a:
                possible += 1
        counter += 3
    return possible

start = loader.one_type_of_data('day3.txt')
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')
