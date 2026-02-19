import math

def part_1(start):
    outer_spiral = math.ceil(math.sqrt(start))
    outer_spiral += 1 if outer_spiral % 2 == 0 else 0
    side = 1 #S=1, E=2, N=3, W=4
    while start < outer_spiral ** 2 - side * (outer_spiral - 1): side += 1
    mid_point = int(outer_spiral ** 2 - ((2 * side - 1) * (outer_spiral - 1)) / 2)
    result = abs(mid_point - start) + int((outer_spiral - 1)/ 2)
    return result

def part_2(start):
    shell = 0
    x = 0
    y = 0
    coordinates = {(x, y): 1}
    result = 0
    while result < start:
        # step
        if x == shell and y == -shell:
            shell += 1
            x += 1
        elif x == shell and y < shell:
            y += 1
        elif x > -shell and y == shell:
            x -= 1
        elif x == -shell and y > -shell:
            y -= 1
        elif x < shell and y == -shell:
            x += 1
        # update
        result = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try: result += coordinates[(x + i, y + j)]
                except: pass
        coordinates[(x, y)] = result
    return result

starting_data = 289326
print(f'The answer for part 1 is: {part_1(starting_data)}')
print(f'The answer for part 2 is: {part_2(starting_data)}')
