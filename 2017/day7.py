import loader

def part_1(start):
    on_top = []
    for i in start:
        if len(i) > 3:
            for j in range(3, len(i) - 1):
                on_top.append(i[j][:-1])
            on_top.append(i[-1])
    for i in start:
        if i[0] not in on_top:
            return i[0]

def part_2(start):
    towers = {}
    for i in start:
        current = []
        current.append(int(i[1][1:-1]))
        if len(i) > 3:
            for j in range(3, len(i) - 1):
                current.append(i[j][:-1])
            current.append(i[-1])
        towers[i[0]] = current
    def calculate_weight(tower):
        weight = towers[tower][0]
        if len(towers[tower]) > 1:
            for i in towers[tower][1:]:
                weight += calculate_weight(i)
        return weight
    for tower in towers.keys():
        if len(towers[tower]) > 1:
            weights = []
            for i in towers[tower][1:]:
                weights.append(calculate_weight(i))
            if len(set(weights)) != 1:
                for i in range(len(weights)):
                    if weights.count(weights[i]) == 1:
                        wrong_weight = weights[i]
                        wrong_index = i
                    else:
                        correct_weight = weights[i]
                return towers[towers[tower][wrong_index + 1]][0] + correct_weight - wrong_weight
    return None

input_data = loader.two_type_of_data('day7.txt')
# print(input_data)
print(f'The answer for part 1 is: {part_1(input_data)}')
print(f'The answer for part 2 is: {part_2(input_data)}')
