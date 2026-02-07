import loader

def data_converter(start):
    result = []
    for floor in start:
        info = floor.split(' ')
        current_floor = []
        for i in range(len(info)):
            if info[i] == 'floor':
                current_floor.append(info[i - 1] + ' ' + info[i])
            if (info[i].replace(',', '').replace('.', '') == 'generator' or
                info[i].replace(',', '').replace('.', '') == 'microchip'):
                current_floor.append(info[i - 1] + ' ' + info[i].replace(',', '').replace('.', ''))
        result.append(current_floor)
    return result

#ChatGPT solution
from collections import deque
from itertools import combinations

FLOORS = (1, 2, 3, 4)

def is_floor_safe(pairs, floor):
    gens = {i for i, (g, c) in enumerate(pairs) if g == floor}
    if not gens:
        return True
    for i, (g, c) in enumerate(pairs):
        if c == floor and g != floor:
            return False
    return True


def is_state_safe(pairs):
    for f in FLOORS:
        if not is_floor_safe(pairs, f):
            return False
    return True


def canonicalize(elevator, pairs):
    # Sort pairs to remove element identity
    return (elevator, tuple(sorted(pairs)))


def items_on_floor(pairs, floor):
    items = []
    for i, (g, c) in enumerate(pairs):
        if g == floor:
            items.append(("G", i))
        if c == floor:
            items.append(("C", i))
    return items


def move_items(pairs, items, new_floor):
    pairs = list(pairs)
    for kind, idx in items:
        g, c = pairs[idx]
        if kind == "G":
            pairs[idx] = (new_floor, c)
        else:
            pairs[idx] = (g, new_floor)
    return tuple(pairs)


def something_below(pairs, floor):
    for g, c in pairs:
        if g < floor or c < floor:
            return True
    return False


def bfs(initial_pairs):
    start = canonicalize(1, initial_pairs)
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (elevator, pairs), steps = queue.popleft()

        # Goal check
        if all(g == 4 and c == 4 for g, c in pairs):
            return steps

        items = items_on_floor(pairs, elevator)

        # Try combinations of 1 or 2 items
        for count in (2, 1):  # prefer 2 up
            for combo in combinations(items, count):
                for direction in (+1, -1):
                    new_floor = elevator + direction
                    if new_floor not in FLOORS:
                        continue

                    # Heuristic: don't go down if nothing below
                    if direction == -1 and not something_below(pairs, elevator):
                        continue

                    new_pairs = move_items(pairs, combo, new_floor)

                    if not is_state_safe(new_pairs):
                        continue

                    new_state = canonicalize(new_floor, new_pairs)
                    if new_state in visited:
                        continue

                    visited.add(new_state)
                    queue.append((new_state, steps + 1))



# Format: (generator_floor, chip_floor)
initial_pairs = (
    (1, 1),  # Thulium
    (1, 2),  # Plutonium
    (1, 2),  # Storntium
    (3, 3),  # Promethum
    (3, 3)   # Ruthenium
)
steps = bfs(initial_pairs)
print("Minimum steps for part 1:", steps)

# Format: (generator_floor, chip_floor)
initial_pairs = (
    (1, 1),  # Thulium
    (1, 2),  # Plutonium
    (1, 2),  # Storntium
    (3, 3),  # Promethum
    (3, 3),  # Ruthenium
    (1, 1),  # Elerium
    (1, 1)   # Dilithium
)
steps = bfs(initial_pairs)
print("Minimum steps for part 2:", steps)





# start = loader.one_type_of_data('day11.txt')
# print(f'Starting data: {start}')
# data = data_converter(start)
# print('Starting data cleared:')
# for i in data:
#     print(i)
# print(f'Answer for part one is: {part_1(start)}.')
# print(f'Answer for part two is: {part_2(start)}.')
