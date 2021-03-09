#!/usr/bin/env python3
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read().splitlines()
            for line in data:
                x, z = line.split(': ')
                y, c = x.split(' ')
                a, b = y.split('-')
                if (checkPwdCount(int(a), int(b), c, z)):
                    p1 = p1 + 1
                if (checkPwdLocation(int(a), int(b), c, z)):
                    p2 = p2 + 1
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


def checkPwdCount(min, max, ch, pwd):
    x = pwd.count(ch)
    if (x == -1):
        return False
    elif (x >= min and x <= max):
        return True
    else:
        return False


def checkPwdLocation(a, b, ch, pwd):
    x = pwd.count(ch)
    y = pwd[a - 1]
    z = pwd[b - 1]
    if (x == -1):
        return False
    elif ((y == ch or z == ch) and y != z):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
