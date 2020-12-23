#!/usr/bin/env python
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read().splitlines()
            data = [int(x) for x in data]
            data.sort()
            p1 = find_jolt_difference(data)

    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


def find_jolt_difference(bag=[]):
    diff1 = 0
    diff3 = 1
    previous_adapter = 0
    for i in range(len(bag)):
        adapter = bag[i]
        if adapter - previous_adapter == 1:
            diff1 += 1
        elif adapter - previous_adapter == 3:
            diff3 += 1
        previous_adapter = adapter
    return diff1 * diff3


if __name__ == '__main__':
    main()
