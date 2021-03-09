#!/usr/bin/env python33

def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read()
            flr = 0
            for d in range(0,len(data)):
              if p2 == 0 and flr == -1:
                p2 = d
              if data[d] == '(':
                flr += 1
              elif data[d] == ')':
                flr -= 1
            p1 = flr
    finally:
        fin.close()
        print(f'P1::{p1}')
        print(f'P2::{p2}')
if __name__ == '__main__':
    main()