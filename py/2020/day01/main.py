#!/usr/bin/env python

def main():
    p = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read()
            d = [int(i) for i in data.split()]
            for j in d:
                for k in d:
                    if(j + k == 2020):
                         p = j * k
                         break
                    for l in d:
                        if(i + j + k == 2020):
                            p2 = i * j * k
                            break
    finally:
        fin.close()
        print(f'Product of the 2 number is {p}')
        print(f'Product of the 3 number is {p2}')
if __name__ == '__main__':
    main()