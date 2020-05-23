"""
Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.
 

Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
Example 3:

Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3
Example 4:

Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0
 

Constraints:

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.
"""
from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        TLE
        """
        unique_letters = set()
        res = 0
        counts = dict()
        total_len = len(s)
        for length in range(minSize, maxSize+1):
            tmp = s[:length]

            unique_letters = Counter(tmp)
            # print(tmp)
            # print(unique_letters)
            if len(unique_letters) <= maxLetters:
                counts[tmp] = counts.get(tmp,0)+1
                res = max(res, counts[tmp])
            for index in range(1,total_len-length+1):
                # print('tmp',s[index:index+length])
                unique_letters[s[index-1]] -= 1
                if unique_letters[s[index-1]] == 0:
                    del unique_letters[s[index-1]]
                unique_letters[s[index+length-1]] += 1
                
                if len(unique_letters) <= maxLetters:
                    tmp = s[index:index+length]
                    counts[tmp] = counts.get(tmp,0)+1
                    res = max(res, counts[tmp])
                    # print(tmp)
                    # print(unique_letters)
        # print(counts)
        return res

from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        """
        Thoughts: if a string of maxsSize can satisfy the requirements, there is also a string of minSize can satisfy the requirements. so only find the string of minSize will be enough.
        """
        unique_letters = set()
        res = 0
        counts = dict()
        total_len = len(s)
        tmp = s[:minSize]
        unique_letters = Counter(tmp)
        # print(tmp)
        # print(unique_letters)
        if len(unique_letters) <= maxLetters:
            counts[tmp] = counts.get(tmp,0)+1
            res = max(res, counts[tmp])
        for index in range(1,total_len-minSize+1):
            # print('tmp',s[index:index+minSize])
            unique_letters[s[index-1]] -= 1
            if unique_letters[s[index-1]] == 0:
                del unique_letters[s[index-1]]
            unique_letters[s[index+minSize-1]] += 1
            
            if len(unique_letters) <= maxLetters:
                tmp = s[index:index+minSize]
                counts[tmp] = counts.get(tmp,0)+1
                res = max(res, counts[tmp])
                # print(tmp)
                # print(unique_letters)
    # print(counts)
        return res

from collections import Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        length = len(s)
        counts = Counter()
        for i in range(length-minSize+1):
            tmp = s[i:i+minSize]
            if len(set(tmp)) <= maxLetters:
                counts[tmp] += 1
        if len(counts) == 0:
            return 0
        return max(counts.values())

S = Solution()
s = "aababcaab"
maxLetters = 2
minSize = 3
maxSize = 4
print(S.maxFreq(s,maxLetters,minSize,maxSize))

s = "aaaa"
maxLetters = 1
minSize = 3
maxSize = 3
print(S.maxFreq(s,maxLetters,minSize,maxSize))

s = "aabcabcab"
maxLetters = 2
minSize = 2
maxSize = 3
print(S.maxFreq(s,maxLetters,minSize,maxSize))

s = "abcde"
maxLetters = 2
minSize = 3
maxSize = 3
print(S.maxFreq(s,maxLetters,minSize,maxSize))

