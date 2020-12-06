#!/usr/bin/env python3
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read().splitlines()
            for line in data:
                print(line)
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


if __name__ == '__main__':
    main()
