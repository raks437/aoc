#!/usr/bin/env python33
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            d = fin.read().splitlines()
            passes = []
            for line in d:
                seat_id = get_seat_id(line)
                passes.append(seat_id)
                p1 = seat_id if seat_id > p1 else p1
            for p in passes:
                if passes.count(p) == 1 and passes.count((p - 2)) == 1 and passes.count((p - 1)) == 0:
                    p2 = (p - 1)
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


def get_seat_id(boarding_id):
    row = get_row(boarding_id[0:7])
    seat = get_seat(boarding_id[7:])
    return row * 8 + seat


def get_row(rows):
    h = 128
    row = 1
    for i in range(0, 7):
        h = int(h / 2)
        if rows[i] == 'B':
            row = row + h
    return row - 1


def get_seat(seats):
    seat = 1
    l = 8
    for i in range(0, 3):
        l = int(l / 2)
        if seats[i] == 'R':
            seat = seat + l
    return seat - 1


if __name__ == '__main__':
    main()
