def assert_arg_count(argc, args):
    assert len(args) == argc, ("args needs to be exactly %d was %d" % (argc, len(args)))

def update(updated, matrix, args):
    assert_arg_count(4, args)
    x = args[0]-1; y = args[1]-1; z = args[2]-1
    w = args[3]
    matrix[x][y][z] = w
    updated.add((x, y, z))

def query(updated, matrix, args):
    assert_arg_count(6, args)

    def find_in_bounds(updated, args):
        (x1, y1, z1, x2, y2, z2) = args

        coords = []
        for (x, y, z) in updated:
            if x >= (x1-1) and x < x2 and y >= (y1-1) and y < y2 and z >= (z1-1) and z < z2:
                coords.append((x, y, z))
        return coords

    coords = find_in_bounds(updated, args)

    sum = 0
    for (x, y, z) in coords:
        sum += matrix[x][y][z]

    print (sum)

def exec_command(line, updated, matrix):
    def to_int(args):
        return [int(x) for x in args]

    args = to_int(line.split(' ')[1:])
    if line.startswith('UPDATE'):
        update(updated, matrix, args)
    elif line.startswith('QUERY'):
        query(updated, matrix, args)
    else:
        assert (false)

def create_matrix(n):
    return [[[0 for k in range(n)] for j in range(n)] for i in range(n)]

def main():
    test_cases = int(input())

    for case in range(0, test_cases):
        line = input()
        n = int(line.split(' ')[0])
        m = int(line.split(' ')[1])

        updated = set()
        matrix = create_matrix(n)
        for k in range(m):
            exec_command(input(), updated, matrix)

main()