from programm import main 
import unittest


class TestMain(unittest.TestCase):

    def test_start_game(self):
        main.start_game()