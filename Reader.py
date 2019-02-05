

'''

TODO
    - Make this into a class
    - develop a standard for the file (either plaintext or binary data file)
    - determine what the columns will be for the data (id, x, y, z, type, ...)


'''

def read_points(path):
    points = []

    with open(path) as f:
        for line in f.readlines():
            print(line)
            raw_nums = line.split()
            point = [float(x) for x in raw_nums]
            points += [point]

    return points

def write_points(path, step):
    with open(path, 'w+') as f:
        for x in [-2*step, -step, 0, step, 2*step]:
            for y in [-2*step, -step, 0, step, 2*step]:
                for z in [-2*step, -step, 0, step, 2*step]:
                    f.write(str(x) + " " + str(y) + " " + str(z) + "\n")
