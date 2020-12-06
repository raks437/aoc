#!/usr/bin/env python3
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read().splitlines()
            cf = CustomsForms()
            for line in data:
                if line == '':
                    p1 = p1 + cf.get_count()
                    p2 = p2 + cf.get_count_v2()
                    cf = CustomsForms()
                else:
                    cf.read(line)
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


class CustomsForms:
    def __init__(self):
        self.all_entry = []

    def read(self, form_data):
        self.all_entry.append(form_data)

    def get_count(self):
        x = ''
        x = x.join(self.all_entry)
        uniques = list(set(list(x)))
        return len(uniques)

    def get_count_v2(self):
        l = self.all_entry
        sets = [set(x) for x in l]
        n = sets[0].intersection(*sets[1:])
        return len(n)


if __name__ == '__main__':
    main()
