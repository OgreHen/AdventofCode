import loader

def part_1(start):
    memory_locations = []
    for i in start:
        memory_locations.append(int(i))
    iterations = []
    while memory_locations not in iterations:
        iterations.append(memory_locations.copy())
        to_reallocate = max(memory_locations)
        current = 0
        while memory_locations[current] != to_reallocate:
            current += 1
        memory_locations[current] = 0
        while to_reallocate > 0:
            current = (current + 1) % len(memory_locations)
            memory_locations[current] += 1
            to_reallocate -= 1
    return len(iterations)

def part_2(start):
    memory_locations = []
    for i in start:
        memory_locations.append(int(i))
    for i in range(2):
        iterations = []
        while memory_locations not in iterations:
            iterations.append(memory_locations.copy())
            to_reallocate = max(memory_locations)
            current = 0
            while memory_locations[current] != to_reallocate:
                current += 1
            memory_locations[current] = 0
            while to_reallocate > 0:
                current = (current + 1) % len(memory_locations)
                memory_locations[current] += 1
                to_reallocate -= 1
    return len(iterations)

input_data = loader.one_type_of_data('day6.txt', '\t')
print(input_data)
print(f'The answer for part 1 is: {part_1(input_data)}')
print(f'The answer for part 2 is: {part_2(input_data)}')
