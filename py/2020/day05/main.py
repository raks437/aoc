#!/usr/bin/env python
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            d = fin.read().splitlines()
            for line in d:
                print(line)
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
