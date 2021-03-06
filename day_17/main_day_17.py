import fileinput


def solve(p1):
    A = set()
    L = list([l.strip() for l in fileinput.input()])
    for r, l in enumerate(L):
        for c, ch in enumerate(l):
            if ch == '#':
                A.add((r, c, 0, 0))

    for _ in range(6):
        new_A = set()
        CHECK = set()
        for (x, y, z, w) in A:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    for dz in [-1, 0, 1]:
                        for dw in [-1, 0, 1]:
                            if w + dw == 0 or (not p1):
                                CHECK.add((x + dx, y + dy, z + dz, w + dw))

        for (x, y, z, w) in CHECK:
            nbr = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    for dz in [-1, 0, 1]:
                        for dw in [-1, 0, 1]:
                            if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                if (x + dx, y + dy, z + dz, w + dw) in A:
                                    nbr += 1
            if (x, y, z, w) not in A and nbr == 3:
                new_A.add((x, y, z, w))
            if (x, y, z, w) in A and nbr in [2, 3]:
                new_A.add((x, y, z, w))
        A = new_A

    return len(A)


print(solve(True))
print(solve(False))
