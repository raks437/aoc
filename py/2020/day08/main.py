#!/usr/bin/env python3
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read().splitlines()
            my_game_console = GameConsole(data)
            my_game_console.parse()
            p1 = my_game_console.get_accumulator()
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


class GameConsole:
    def __init__(self, data):
        self.data = data
        self.accumulator = 0
        self.instruction = set()
        self.line = 0
        self.terminated = False

    def parse(self, reset=False):
        self.line = 0 if reset else self.line
        while self.line not in self.instruction or self.terminated:
            self.instruction.add(self.line)
            op, arg = self.data[self.line].split(' ')
            if op == 'acc':
                self.accumulator = self.accumulator + int(arg)
                self.line = self.line + 1
            elif op == 'jmp':
                self.line = self.line + int(arg)
            elif op == 'nop':
                self.line = self.line + 1
            self.parse()

    def get_accumulator(self):
        return self.accumulator


if __name__ == '__main__':
    main()
