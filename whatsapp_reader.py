def read(filename):
    data = []

    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue

            try:
                _, msg = line.split(' - ', 2)
                sender, msgTxt = msg.split(': ', 2)
            except:
                lastEntry = data[-1]
                data[-1] = (lastEntry[0] + ' \n ' + line, lastEntry[1])
                continue

            data.append((msgTxt.strip(), sender))

    return data
