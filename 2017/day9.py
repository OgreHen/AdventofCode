def part_1_and_2(start):
    first_string = ''
    counter = 0
    while counter < len(start):
        if start[counter] == '!':
            counter += 2
        else:
            first_string += start[counter]
            counter += 1
    second_string = ''
    counter, removed = 0, 0
    garbage = False
    while counter < len(first_string):
        if garbage:
            if first_string[counter] == '>':
                garbage = False
            else:
                removed += 1
        else:
            if first_string[counter] == '<':
                garbage = True
            else:
                second_string += first_string[counter]
        counter += 1
    score, open, counter = 0, 0, 0
    while counter < len(second_string):
        if second_string[counter] == '{':
            open += 1
        elif second_string[counter] == '}':
            score += open
            open -= 1
        counter += 1
    return score, removed

input_data = open('day9.txt', 'r').read()
# print(input_data)
print(f'The answer for part 1 is: {part_1_and_2(input_data)[0]}')
print(f'The answer for part 2 is: {part_1_and_2(input_data)[1]}')
