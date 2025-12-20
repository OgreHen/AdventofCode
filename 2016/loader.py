def one_line_loader(filename, split_character = '\n'):
    version = open(filename, 'r').read()
    return version.split(split_character)
