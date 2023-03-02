import random

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
