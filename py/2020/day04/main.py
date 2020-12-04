#!/usr/bin/env python
import re


def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            d1 = []
            d = fin.read().splitlines()
            p = Passport()
            for line in d:
                if (line == ''):
                    if (p.is_passport_valid()):
                        p1 = p1 + 1
                    if (p.is_passport_valid_v2()):
                        p2 = p2 + 1
                    p = Passport()
                else:
                    p.read_data(line)
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


class Passport:
    def __init__(self):
        self.byr = False
        self.iyr = False
        self.eyr = False
        self.hgt = False
        self.hcl = False
        self.ecl = False
        self.pid = False
        self.cid = False
        self.v_byr = False
        self.v_iyr = False
        self.v_eyr = False
        self.v_hgt = False
        self.v_hcl = False
        self.v_ecl = False
        self.v_pid = False
        self.v_cid = False

    def is_passport_valid(self):
        return (
            self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid
        )

    def is_passport_valid_v2(self):
        return (
            self.is_passport_valid() and self.v_byr and self.v_iyr and self.v_eyr and self.v_hgt and self.v_hcl and self.v_ecl and self.v_pid
        )

    def read_data(self, data):
        line = data.split(' ')
        for l in line:
            if (l.count('byr:') == 1):
                self.byr = True
                self.v_byr = self.check_byr(l[4:])
            if (l.count('iyr:') == 1):
                self.iyr = True
                self.v_iyr = self.check_iyr(l[4:])
            if (l.count('eyr:') == 1):
                self.eyr = True
                self.v_eyr = self.check_eyr(l[4:])
            if (l.count('hgt:') == 1):
                self.hgt = True
                self.v_hgt = self.check_hgt(l[4:])
            if (l.count('hcl:') == 1):
                self.hcl = True
                self.v_hcl = self.check_hcl(l[4:])
            if (l.count('ecl:') == 1):
                self.ecl = True
                self.v_ecl = self.check_ecl(l[4:])
            if (l.count('pid:') == 1):
                self.pid = True
                self.v_pid = self.check_pid(l[4:])
            if (l.count('cid:') == 1):
                self.cid = True

    def check_byr(self, x):
        y = int(x)
        return True if (y >= 1920 and y <= 2002) else False

    def check_iyr(self, x):
        y = int(x)
        return True if (y >= 2010 and y <= 2020) else False

    def check_eyr(self, x):
        y = int(x)
        return True if (y >= 2020 and y <= 2030) else False

    def check_hgt(self, x):
        l1 = x[-2:]
        if (l1 == 'cm'):
            l2 = int(x.split('cm')[0])
            return True if (l2 >= 150 and l2 <= 193) else False
        elif (l1 == 'in'):
            l2 = int(x.split('in')[0])
            return True if (l2 >= 59 and l2 <= 76) else False
        else:
            return False

    def check_hcl(self, x):
        l1 = len(x)
        l2 = x[0]
        hex_code = re.compile(r'^#[0-9a-f]{6}$')
        return True if (hex_code.fullmatch(x)) else False

    def check_ecl(self, x):
        l = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        return True if (l.count(x) == 1) else False

    def check_pid(self, x):
        num = re.compile(r'^[0-9]{9}$')
        return True if (num.fullmatch(x)) else False


if __name__ == '__main__':
    main()
