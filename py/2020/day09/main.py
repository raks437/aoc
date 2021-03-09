#!/usr/bin/env python3
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read().splitlines()
            data = [int(x) for x in data]
            p1 = find_xmas_vulnerable_num(data)
            p2 = find_xmas_vulnerability(data, 400480901)

    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


def find_xmas_vulnerable_num(data, preamble_len=25):
    start_index = 0
    end_index = preamble_len
    num_index = preamble_len
    num = 0
    found_vulnerability = False
    while num_index <= len(data) - 1 and not found_vulnerability:
        preamble = data[start_index:end_index]
        num = data[num_index]
        if check_vulnerability(preamble, num):
            return num
        start_index += 1
        end_index += 1
        num_index += 1

    return num


def check_vulnerability(preamble, num):
    is_vulnerable = True
    preamble_len = len(preamble)

    for i in range(preamble_len):
        for j in range(preamble_len):
            if i != j:
                a = preamble[i]
                b = preamble[j]
                if a + b == num:
                    is_vulnerable = False
                    return is_vulnerable
                else:
                    continue
            else:
                continue
    return is_vulnerable


def find_xmas_vulnerability(data=[], num=0):
    limit = data.index(num)
    for i in range(limit - 1):
        for j in range(limit):
            contiguous_nums = data[i:j]
            if num == sum(contiguous_nums):
                return min(contiguous_nums) + max(contiguous_nums)
    return -1


if __name__ == '__main__':
    main()
