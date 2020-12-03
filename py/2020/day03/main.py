#!/usr/bin/env python
def main():
    p1 = 0
    p2 = 0
    i = 0
    try:
        with open('input.txt', 'r') as fin:
            d = fin.read().splitlines()
            p1 = find_trees(3, 1, d)
            p2 = find_trees(1, 1, d) * find_trees(3, 1, d) * find_trees(5, 1, d) * find_trees(7, 1, d) * find_trees(1, 2, d)
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


def find_trees(right, down, data):
    t = len(data)
    l = len(data[0])
    i = 0
    n = 0
    for j in range(0, t, down):
        line = data[j]
        if (line[i] == '#'):
            n = n + 1
        i = i + right
        if (i > l - 1):
            i = i % l
    return n


if __name__ == '__main__':
    main()
