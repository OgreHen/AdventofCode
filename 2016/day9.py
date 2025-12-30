def part_1(start):
    output = ''
    counter = 0
    while counter < len(start):
        if start[counter] == '(':
            start_position = counter
            end_position = counter + 1
            while start[end_position] != ')':
                end_position += 1
            marker = start[start_position : end_position + 1]
            length = int(marker.split('x')[0][1:])
            repetition = int(marker.split('x')[1][:-1])
            counter = end_position + 1
            for _ in range(repetition):
                output += start[counter : counter + length]
            counter += length
        else:
            output += start[counter]
            counter += 1
    # print(output)
    return len(output)

def part_2(start):
    result = 0
    counter = 0
    while counter < len(start):
        if start[counter] == '(':
            start_position = counter
            end_position = counter + 1
            while start[end_position] != ')':
                end_position += 1
            marker = start[start_position : end_position + 1]
            length = int(marker.split('x')[0][1:])
            repetition = int(marker.split('x')[1][:-1])
            counter = end_position + 1
            if '(' in start[counter : counter + length]:
                result += part_2(start[counter : counter + length]) * repetition
            else:
                result += length * repetition
            counter += length
        else:
            result += 1
            counter += 1
    return result

start = open('day9.txt', 'r').read()
print(f'Starting data: {start}')
print(f'Answer for part one is: {part_1(start)}.')
print(f'Answer for part two is: {part_2(start)}.')
