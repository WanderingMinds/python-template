# -*- coding: utf-8 -*-
""" Example unittests.

Background Material:

    * [Python Unittest logs](https://docs.python.org/3/library/unittest.html)

"""

import unittest

def myadd(x):
    return x + 1

class TestBasics(unittest.TestCase):
    def test_myadd(self):
        self.assertEqual(myadd(3), 4)

if __name__ == '__main__':
    unittest.main()