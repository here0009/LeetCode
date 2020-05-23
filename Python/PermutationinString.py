"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.
Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
from collections import Counter
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        len_s1 = len(s1)
        lens_s2 = len(s2)
        if len_s1 > lens_s2:
            return False
        start = 0
        end = len_s1
        s1_counter = Counter(s1)
        # print(s1_counter)
        s2_counter =  Counter(s2[start:end])
        if s1_counter == s2_counter:
                return True
        while end < lens_s2:
            # print(s2_counter)
            s2_counter[s2[start]] -= 1
            if s2_counter[s2[start]] == 0:
                s2_counter.pop(s2[start])
            s2_counter[s2[end]] += 1
            start += 1
            end += 1
            if s1_counter == s2_counter:
                return True
        return False

s = Solution()
s1 = "ab" 
s2 = "eidbaooo"
print(s.checkInclusion(s1, s2))
s1= "ab" 
s2 = "eidboaoo"
print(s.checkInclusion(s1, s2))
