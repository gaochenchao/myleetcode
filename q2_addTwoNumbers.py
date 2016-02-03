# -*- coding: utf-8 -*-
import unittest

__author__ = 'gaochenchao'


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# twosum more than 10 next sum will plus 1
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        header = ListNode(0)
        p = header
        highbit = 0
        while l1 or l2 or highbit:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            highbit, twosum = divmod(v1+v2+highbit, 10)
            p.next = ListNode(twosum)
            p = p.next
        return header.next


if __name__ == '__main__':
    l1, l2 = ListNode(0), ListNode(0)
    p1, p2 = l1, l2
    for i in [2, 4, 3]:
        p1.next = ListNode(i)
        p1 = p1.next
    for i in [5, 6, 4]:
        p2.next = ListNode(i)
        p2 = p2.next
    so = Solution()
    header = so.addTwoNumbers(l1.next, l2.next)
    while header:
        print header.val
        header = header.next