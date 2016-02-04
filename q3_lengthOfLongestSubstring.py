# -*- coding: utf-8 -*-
__author__ = 'gaochenchao'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
        """
        # dvdf 3
        if not s:
            return 0
        if len(s) == 1:
            return 1
        start = maxLen = 0
        charUsed = {}
        for i, v in enumerate(s):
            if v in charUsed and charUsed[v] >= start:
                start = charUsed[v] + 1
                charUsed[v] = i
            else:
                charUsed[v] = i
                maxLen = max(maxLen, i - start + 1)
        return maxLen
st = Solution()
print st.lengthOfLongestSubstring("bbbbb")
