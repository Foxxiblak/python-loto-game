import random

class Player:
    def __init__(self, _name):
        self.name = _name
        self.card = random.sample(range(1, 100), 18)
        self.first_line_pos = self.generate_and_sorted_line()
        self.second_line_pos = self.generate_and_sorted_line()
        self.third_line_pos = self.generate_and_sorted_line()
        self.crossed_out = []

    def generate_and_sorted_line(self):
        return sorted(random.sample(range(0, 9), 6))

    def print_card(self):
        line = 36 - len(self.name) - 2
        isEven = True if line % 2 == 0 else False
        indent = int(line / 2 if isEven else (line - 1) / 2)

        print('-' * indent + f' {self.name} ' + '-' * indent)
        self.print_line(self.first_line_pos, self.card[0:6])
        self.print_line(self.second_line_pos, self.card[6:12])
        self.print_line(self.third_line_pos, self.card[12:])
        print('-' * 36)

    def print_line(self, line, numbs):
        numbs_sort = sorted(numbs)
        string_line = ''
        num_index = 0

        for i in range(0, 9):
            if i in line:
                if (numbs_sort[num_index] in self.crossed_out):
                    string_line += '| - '
                else:
                    string_line += f'|{numbs_sort[num_index]:02d} '
                num_index += 1
            else:
                string_line += '|   '
        print(string_line)

    def check_number(self, num):
        return True if num in self.card else False

    def automatic_move(self, num):
        if num in self.card:
            self.crossed_out.append(num)