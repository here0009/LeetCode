"""
You are given two strings word1 and word2.

A string x is called valid if x can be rearranged to have word2 as a 
prefix
.

Return the total number of valid 
substrings
 of word1.

 

Example 1:

Input: word1 = "bcca", word2 = "abc"

Output: 1

Explanation:

The only valid substring is "bcca" which can be rearranged to "abcc" having "abc" as a prefix.

Example 2:

Input: word1 = "abcabc", word2 = "abc"

Output: 10

Explanation:

All the substrings except substrings of size 1 and size 2 are valid.

Example 3:

Input: word1 = "abcabc", word2 = "aaabc"

Output: 0

 

Constraints:

1 <= word1.length <= 105
1 <= word2.length <= 104
word1 and word2 consist only of lowercase English letters.
"""

from collections import Counter


class Solution:
    
    def validSubstringCount(self, word1: str, word2: str) -> int:
        
        def check_counter(count_x:Counter, count_ref:Counter) -> bool:
            """
            check if count_ref >= count_x for all element in count_ref
            """
            for k, v in count_ref.items():
                if count_x[k] < v:
                    return False
            return True
        
        len_1, len_2 = len(word1), len(word2)
        res = 0
        if len_1 < len_2:
            return res
        count_2 = Counter(word2)
        left, right = 0, 0
        count_tmp = Counter()
        while left < len_1:
            while right < len_1 and not check_counter(count_tmp, count_2):
                count_tmp[word1[right]] += 1
                right += 1
            if check_counter(count_tmp, count_2):
                res += len_1 - right + 1           
            count_tmp[word1[left]] -= 1
            left += 1
        return res
            
        

s = Solution()
word1 = 'abcabc'
word2 = 'abc'
print(s.validSubstringCount(word1, word2))
word1 = "bcca"
word2 = "abc"
print(s.validSubstringCount(word1, word2))
word1 = "abcabc"
word2 = "aaabc"
print(s.validSubstringCount(word1, word2))