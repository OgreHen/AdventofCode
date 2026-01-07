import hashlib

def part_1(input_hash):
    counter = 0
    possibilities = []
    results = []
    while len(results) < 64:
        to_hash = input_hash + str(counter)
        to_check = str(hashlib.md5(to_hash.encode()).hexdigest())
        appended = False
        for i in range(len(to_check) - 2):
            if to_check[i] == to_check[i + 1] == to_check[i + 2]:
                if not appended:
                    possibilities.append([counter, to_check[i], False])
                    appended = True
            try:
                if to_check[i] == to_check[i + 1] == to_check[i + 2] == to_check[i + 3] == to_check[i + 4]:
                    for j in range(len(possibilities) - 1):
                        if (counter <= possibilities[j][0] + 1000 and
                                to_check[i] == possibilities[j][1] and
                                possibilities[j][2] == False):
                            possibilities[j][2] = True
                            results.append(possibilities[j])
            except: pass
        counter += 1
    return results[63][0]

def part_2(input_hash):
    counter = 0
    possibilities = []
    results = []
    while len(results) < 64:
        to_hash = input_hash + str(counter)
        hashed = hashlib.md5(to_hash.encode()).hexdigest()
        for i in range(2016):
            hashed = hashlib.md5(hashed.encode()).hexdigest()
        to_check = str(hashed)
        appended = False
        for i in range(len(to_check) - 2):
            if to_check[i] == to_check[i + 1] == to_check[i + 2]:
                if not appended:
                    possibilities.append([counter, to_check[i], False])
                    appended = True
            try:
                if to_check[i] == to_check[i + 1] == to_check[i + 2] == to_check[i + 3] == to_check[i + 4]:
                    for j in range(len(possibilities) - 1):
                        if (counter <= possibilities[j][0] + 1000 and
                                to_check[i] == possibilities[j][1] and
                                possibilities[j][2] == False):
                            possibilities[j][2] = True
                            results.append(possibilities[j])
            except: pass
        counter += 1
    results.sort()
    return results[63][0]

input_hash = 'yjdafjpo'
print(f'Answer for part one is: {part_1(input_hash)}.')
print(f'Answer for part two is: {part_2(input_hash)}.')
