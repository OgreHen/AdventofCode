def one_type_of_data(filename, split_character = '\n'):
    version = open(filename, 'r').read()
    return version.split(split_character)
