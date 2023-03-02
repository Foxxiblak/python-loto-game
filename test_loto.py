import unittest
import random
from main import ask
from master import Master
from player import Player
from unittest.mock import patch


class LotoMasterCase(unittest.TestCase):
    def setUp(self):
        self.master = Master()
    def test_init(self):
        self.assertEqual(self.master.used, [])
        self.assertEqual(len(self.master.bag), 100)

    def test_make_choice(self):
        self.assertLess(self.master.make_choice(), 100)
        self.assertGreater(self.master.make_choice(), -1)


class LotoPlayerCase(unittest.TestCase):
    def setUp(self):
        self.player = Player('Fox')

    def test_init(self):
        self.assertEqual(self.player.name, 'Fox')
        self.assertEqual(len(self.player.card), 18)
        for item in self.player.card:
            self.assertIn(item, [i for i in range(0, 100)])
        self.assertEquals(len(self.player.first_line_pos), len(self.player.second_line_pos), len(self.player.third_line_pos))
        self.assertEqual(self.player.crossed_out, [])

    def test_generate_and_sorted_line(self):
        res = self.player.generate_and_sorted_line()
        self.assertEqual(len(res), 6)
        for item in res:
            self.assertLess(item, 9)
            self.assertGreater(item, -1)

    def test_check_number(self):
        self.assertTrue(self.player.check_number(random.choice(self.player.card)))

    def test_automatic_move(self):
        num = random.choice(self.player.card)
        self.player.automatic_move(num)
        self.assertEqual(self.player.crossed_out, [num])


class DefaultTest(unittest.TestCase):
    @patch('builtins.input', return_value='y')
    def test_ask_true(self, input_mock):
        res = ask()
        input_mock.assert_called_with('Зачеркнуть цифру? (y/n) ')
        self.assertEqual(input_mock.return_value, 'y')
        self.assertTrue(res)

    @patch('builtins.input', return_value='n')
    def test_ask_false(self, input_mock):
        res = ask()
        input_mock.assert_called_with('Зачеркнуть цифру? (y/n) ')
        self.assertEqual(input_mock.return_value, 'n')
        self.assertFalse(res)


