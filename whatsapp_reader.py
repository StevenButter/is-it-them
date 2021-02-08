def read(filename):
    data = []

    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[1:]:
            msg = line[20:].split(':', 2)
            data.append((msg[1].strip(), msg[0]))

    return data
