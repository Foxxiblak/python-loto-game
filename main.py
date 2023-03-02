import sys
from master import Master
from player import Player

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