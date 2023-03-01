import random
import sys

class Master:
    def __init__(self):
        self.bag = [i for i in range(0, 100)]
        self.used = []

    def make_choice(self):
        num = random.choice(self.bag)
        self.used.append(num)
        self.bag.remove(num)
        return num

    def print_choice(self, num):
        print("*" * 12)
        print("*" + " " * 10 + "*")
        print("*" + " " * 4 + f'{num:02d}' + " " * 4 + "*")
        print("*" + " " * 10 + "*")
        print("*" * 12)

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

def ask():
    answer = input('Зачеркнуть цифру? (y/n) ').lower()
    return True if answer == 'y' else False

if __name__ == '__main__':
    name = input("Введите ваше имя: ")
    player_1 = Player(name)
    player_1.print_card()
    player_2 = Player('Computer')
    player_2.print_card()

    go_game = True
    while go_game:
        master = Master()
        bag_choice = master.make_choice()
        master.print_choice(bag_choice)

        user_answer = ask()
        res = player_1.check_number(bag_choice)

        if (user_answer and res == False) or (not user_answer and res == True):
            print('GAME OVER')
            sys.exit(0)
        else:
            player_1.automatic_move(bag_choice)
            player_2.automatic_move(bag_choice)
            player_1.print_card()
            player_2.print_card()

        if len(player_2.card) == len(player_2.crossed_out):
            print('Win Player 2!')
        elif len(player_1.card) == len(player_1.crossed_out):
            print('Win Player 1!')