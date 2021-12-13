def sort_names(input_file_path: str, output_file_path: str):
    """
    Function which sorts names from `file_path` and write them to a new file `output_file_path`.
    @param input_file_path: file of unsorted names
    @param output_file_path: file of sorted names
    @return: None
    """
    with open(input_file_path) as in_file:
        if not isinstance(input_file_path, str):
            raise TypeError
        names = []
        for line in in_file:
            if not line.endswith('\n'):
                names.append(line)
            else:
                names.append(line[:-1])
        names.sort()
    with open(output_file_path, 'w') as out_file:
        for name in names:
            out_file.write(name+'\n')
    return None


sort_names('names.txt', 'sorted_names.txt')
