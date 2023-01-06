#!/usr/bin/python3

"""
Unittest for max_integer([])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    '''unittest for max_integer'''
    def test_max_integer(self):
        '''test for correct output'''
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 1, 1]), 1)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([1,2,3,4,-2,3,4,-4,-5]), 4)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer(), None)
