import unittest
from yatzy import Yatzy

class TestYatzy(unittest.TestCase):
    def setUp(self):
        self.yatzy = Yatzy()

    def test_roll(self):
        self.yatzy.roll()
        self.assertEqual(len(self.yatzy.dice), 5)
        self.assertTrue(all(1 <= d <= 6 for d in self.yatzy.dice))

    def test_lock_unlock(self):
        self.yatzy.lock_die(0)
        self.assertTrue(self.yatzy.locked[0])
        self.yatzy.unlock_die(0)
        self.assertFalse(self.yatzy.locked[0])

    def test_ones(self):
        self.yatzy.dice = [1, 1, 2, 3, 4]
        self.assertEqual(self.yatzy.ones(), 2)

    def test_twos(self):
        self.yatzy.dice = [2, 2, 1, 3, 4]
        self.assertEqual(self.yatzy.twos(), 4)

    def test_threes(self):
        self.yatzy.dice = [3, 3, 3, 1, 2]
        self.assertEqual(self.yatzy.threes(), 9)

    def test_fours(self):
        self.yatzy.dice = [4, 4, 1, 2, 3]
        self.assertEqual(self.yatzy.fours(), 8)

    def test_fives(self):
        self.yatzy.dice = [5, 5, 5, 1, 2]
        self.assertEqual(self.yatzy.fives(), 15)

    def test_sixes(self):
        self.yatzy.dice = [6, 6, 1, 2, 3]
        self.assertEqual(self.yatzy.sixes(), 12)

    def test_one_pair(self):
        self.yatzy.dice = [3, 3, 4, 4, 1]
        self.assertEqual(self.yatzy.one_pair(), 8)

    def test_two_pairs(self):
        self.yatzy.dice = [3, 3, 4, 4, 1]
        self.assertEqual(self.yatzy.two_pairs(), 14)

    def test_three_alike(self):
        self.yatzy.dice = [3, 3, 3, 4, 1]
        self.assertEqual(self.yatzy.three_alike(), 9)

    def test_four_alike(self):
        self.yatzy.dice = [4, 4, 4, 4, 1]
        self.assertEqual(self.yatzy.four_alike(), 16)

    def test_small(self):
        self.yatzy.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.yatzy.small(), 15)

    def test_large(self):
        self.yatzy.dice = [2, 3, 4, 5, 6]
        self.assertEqual(self.yatzy.large(), 20)

    def test_full_course(self):
        self.yatzy.dice = [2, 2, 3, 3, 3]
        self.assertEqual(self.yatzy.full_course(), 14)

    def test_chance(self):
        self.yatzy.dice = [1, 2, 3, 4, 5]
        self.assertEqual(self.yatzy.chance(), 15)

    def test_yatzy(self):
        self.yatzy.dice = [4, 4, 4, 4, 4]
        self.assertEqual(self.yatzy.yatzy(), 50)

if __name__ == '__main__':
    unittest.main()