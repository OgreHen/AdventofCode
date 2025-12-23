def one_type_of_data(filename, split_character = '\n'):
    version = open(filename, 'r').read()
    return version.split(split_character)

def two_type_of_data(filename, split_character1 = '\n', splitter_character2 = ' '):
    version = open(filename, 'r').read()
    first = version.split(split_character1)
    second = []
    for item in first:
        second.append(item.split(splitter_character2))
    return second