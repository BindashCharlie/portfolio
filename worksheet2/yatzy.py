import random

class Yatzy:
    def __init__(self):
        self.dice = [0] * 5
        self.locked = [False] * 5
        self.roll()  # Roll all dice upon instantiation

    def roll(self):
        for i in range(5):
            if not self.locked[i]:
                self.dice[i] = random.randint(1, 6)
        return self.dice

    def lock_die(self, index):
        if 0 <= index < 5:
            self.locked[index] = True

    def unlock_die(self, index):
        if 0 <= index < 5:
            self.locked[index] = False

    def ones(self):
        return sum(d for d in self.dice if d == 1)

    def twos(self):
        return sum(d for d in self.dice if d == 2)

    def threes(self):
        return sum(d for d in self.dice if d == 3)

    def fours(self):
        return sum(d for d in self.dice if d == 4)

    def fives(self):
        return sum(d for d in self.dice if d == 5)

    def sixes(self):
        return sum(d for d in self.dice if d == 6)

    def one_pair(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):
            if counts[i] >= 2:
                return i * 2
        return 0

    def two_pairs(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        pairs = [i for i in range(6, 0, -1) if counts[i] >= 2]
        if len(pairs) >= 2:
            return pairs[0] * 2 + pairs[1] * 2 # Correct calculation
        return 0

    def three_alike(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):
            if counts[i] >= 3:
                return i * 3
        return 0

    def four_alike(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        for i in range(6, 0, -1):
            if counts[i] >= 4:
                return i * 4
        return 0

    def small(self):
        if sorted(self.dice) == [1, 2, 3, 4, 5]:
            return 15
        return 0

    def large(self):
        if sorted(self.dice) == [2, 3, 4, 5, 6]:
            return 20
        return 0

    def full_course(self):
        counts = [0] * 7
        for d in self.dice:
            counts[d] += 1
        if 2 in counts and 3 in counts:
            return sum(i * counts[i] for i in range(1, 7))
        return 0

    def chance(self):
        return sum(self.dice)

    def yatzy(self):
        if len(set(self.dice)) == 1:
            return 50
        return 0