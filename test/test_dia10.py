import dia10.dia10 as dia10

import unittest

class Test_dia10(unittest.TestCase):
    def test_dia10_1(self):
        self.assertEqual(dia10.dia10_1("./dia10/test.txt"), 13140)

if __name__ == '__main__':
    unittest.main()
