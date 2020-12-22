#!/usr/bin/env python3
def main():
    p1 = 0
    p2 = 0
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read().splitlines()
            my_game_console = GameConsole(data)
            p1 = my_game_console.get_accumulator()['accumulator']
            p2 = my_game_console.hit_and_trial_to_fix_game_code()
    finally:
        fin.close()
        print(f'Part 1: {p1}')
        print(f'Part 2: {p2}')


class GameConsole:
    def __init__(self, data):
        self.data = data
        self.accumulator = 0
        self.instruction = set()
        self.terminated = False
        self.is_repeating = False

    def get_accumulator(self, data=[], stop_repeat=True):
        line = 0
        if len(data) == 0:
            data = self.data
        while line <= len(data) - 1 and not self.terminated:
            op, arg = data[line].split(' ')
            if stop_repeat and line in self.instruction:
                break
            else:
                self.instruction.add(line)
            if op == 'acc':
                self.accumulator = self.accumulator + int(arg)
                line += 1
            elif op == 'jmp':
                line += int(arg)
            elif op == 'nop':
                line += 1
            elif op == 'end':
                self.terminated = True
        return {'accumulator': self.accumulator, 'terminated': self.terminated}

    def hit_and_trial_to_fix_game_code(self):
        for i in range(0, len(self.data) - 1):
            self.terminated = False
            self.accumulator = 0
            self.instruction = set()
            line = self.data[i]
            trial_data = self.data[:]
            if 'jmp' in line:
                op, arg = trial_data[i].split(' ')
                op = 'nop'
                trial_data[i] = ' '.join([op, arg])
                if self.get_accumulator(trial_data)['terminated']:
                    break
            elif 'nop' in line:
                op, arg = trial_data[i].split(' ')
                op = 'jmp'
                trial_data[i] = ' '.join([op, arg])
                if self.get_accumulator(trial_data)['terminated']:
                    break

        return self.accumulator


if __name__ == '__main__':
    main()
