"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p are present in s. In particular, your input is the string p and you need to output the number of different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.

Example 1:
Input: "a"
Output: 1

Explanation: Only the substring "a" of string "a" is in the string s.
Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.
Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of string "zab" in the string s.
"""
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
        wrong answer for "zaba"
        """
        index, length = 0, len(p)
        res = 0
        substrings = set()
        while index < length:
            next_index = index+1
            while next_index < length and (ord(p[next_index])-ord(p[next_index-1]))%26 == 1:
                next_index += 1
            # print(p[index:next_index])
            if p[index:next_index] not in substrings:
                substrings.add(p[index:next_index])
                res += (next_index-index+1)*(next_index-index)//2
            index = next_index
        return res

# class Solution:
#     def findSubstringInWraproundString(self, p: str) -> int:
#         index, length = 0, len(p)
#         res = 0
#         letter_dict = dict()
#         while j < length:
#             next_index = index+1
#             while next_index < length and (ord(p[next_index])-ord(p[next_index-1]))%26 == 1:
#                 next_index += 1
#             letter_dict[p[index]] = max(next_index-index, letter_dict.get(p[index],0))
#             index = next_index
#         print(letter_dict)
#         return res

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        """
        two pointer and dp
        """
        left, right = 0, 1
        length = len(p)
        letter_dict = dict()
        while right <= length:
            # print(letter_dict)
            while right < length and (ord(p[right])-ord(p[right-1]))%26 == 1:
                right += 1
            while left < right:
                letter_dict[p[left]] = max(right-left, letter_dict.get(p[left],0))
                left += 1
            right += 1
        return sum(letter_dict.values())

            

s = Solution()
p = 'a'
print(s.findSubstringInWraproundString(p))
p = 'cac'
print(s.findSubstringInWraproundString(p))
p = 'zab'
print(s.findSubstringInWraproundString(p))
p = "zaba"
print(s.findSubstringInWraproundString(p))