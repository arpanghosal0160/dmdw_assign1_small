# tests/test_fp_growth.py
import unittest
from src.fp_growth import FPGrowth, FPTreeNode

class TestFPGrowth(unittest.TestCase):

    def setUp(self):
        self.min_support = 2
        self.fp_growth = FPGrowth(self.min_support)

    def test_build_fp_tree(self):
        transactions = [
            ['A', 'B', 'D'],
            ['B', 'C', 'E'],
            ['A', 'B', 'C', 'E'],
            ['B', 'E']
        ]
        tree, header_table = self.fp_growth.build_fp_tree(transactions)

        # Assert the tree structure and header table content
        self.assertIsNotNone(tree)
        self.assertIsNotNone(header_table)
        self.assertIn('B', header_table)

    def test_mine_patterns(self):
        transactions = [
            ['A', 'B', 'D'],
            ['B', 'C', 'E'],
            ['A', 'B', 'C', 'E'],
            ['B', 'E']
        ]
        tree, _ = self.fp_growth.build_fp_tree(transactions)
        patterns = self.fp_growth.mine_patterns(tree)

        # Assert the mined patterns
        self.assertIsNotNone(patterns)
        self.assertGreaterEqual(len(patterns), 1)

if __name__ == '__main__':
    unittest.main()
