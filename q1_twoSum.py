# -*- coding: utf-8 -*-
import unittest

__author__ = 'gaochenchao'


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = {}
        for i, v in enumerate(nums):
            if target - v in pairs:
                return pairs[target - v] + 1, i + 1
            pairs[v] = i
        return -1, -1


class SolutionTest(unittest.TestCase):

    def testsum(self):
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), (2, 3))


if __name__ == '__main__':
    unittest.main()
