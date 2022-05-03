import unittest
from cash import Cash

class CashTest(unittest.TestCase):
    def test_change_cash(self):
        cash = Cash(0.41)
        change = cash.calculate_change()
        # When the change is 41 cents, so the minimun numbers coins is 4 (4 dimes coin)
        self.assertEqual(change, 4)
        # When the change is 25 cents, so the minimun numbers coins is One (1 quarter coin)
        cash = Cash(0.25)
        change = cash.calculate_change()
        self.assertEqual(change, 1)
        # When the change is 50 cents, so the minimun numbers coins is Two (2 quarter coin)
        cash = Cash(0.5)
        change = cash.calculate_change()
        self.assertEqual(change, 2)
        # When the change is 900 cents (9 dollars), so the minnumo coins is Thirty Six (36 quarters coins)
        cash = Cash(9)
        change = cash.calculate_change()
        self.assertEqual(change, 36)
        # When the change is 8 cents, so the minnumo coins is eight (8 pennies coins)
        cash = Cash(0.08)
        change = cash.calculate_change()
        self.assertEqual(change, 8)
        

if __name__ == '__main__':
    unittest.main()