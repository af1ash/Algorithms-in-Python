from src.HashMap.SortTableMap import (
    SortedTableMap
)
import sys
import unittest


class TestUnsortedTableMap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        print(sys.path)
        self.m = SortedTableMap()

    def tearDown(self):
        print('test finished')

    def testUnsortedTableMap(self):

        self.assertEqual(len(self.m), 0)
        self.m['K'] = 2
        self.m['B'] = 4
        self.m['U'] = 2
        self.m['V'] = 8
        self.m['K'] = 9
        self.assertEqual(len(self.m), 4)
        self.assertEqual(self.m['B'], 4)
        self.assertRaises(KeyError, self.m.get('A'))
        self.assertEqual(self.m.get('K', 5), 9)
        del self.m['V']


if __name__ == '__main__':
    unittest.main()
