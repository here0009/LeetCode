"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
import itertools
def find_all(a_str, pattern):
    start = 0
    pos_list = []
    len_a_str = len(a_str)
    len_pattern = len(pattern)
    pos_tmp = a_str.find(pattern, start)
    while pos_tmp != -1 and start < len_a_str:
        pos_list.append(pos_tmp)
        start = pos_tmp + 1
        pos_tmp = a_str.find(pattern, start)
    return pos_list
    
class Solution_1:
    """
    Thoughts: Time Exceed, try to use update dict method
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_set = set(s)
        t_set = set(t)
        if s_set != t_set:
            return False
        if all(s.count(letter) ==  t.count(letter) for letter in s_set):
            return True
        else:
            return False

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p_set = set(p)
        start = 0
        end = 0
        len_p = len(p)
        while start <= len(s) - len_p  and end < len(s):
            # print(s[start])
            while start <= len(s) - len_p:
                if s[start] not in p_set:
                    start += 1
                else:
                    break
            end = start
            while end < len(s):
                if s[end] in p_set and end-start < len_p:
                    end += 1
                else:
                    break
            if end-start == len_p:
                # print(s[start:end])
                if self.isAnagram(s[start:end], p):
                    res.append(start)
                start += 1
            else:
                start = end + 1
        return res

class Solution:
    def strToDict(self, string):
        s_dict = dict()
        for s in string:
            s_dict[s] = s_dict.get(s, 0) + 1
        return s_dict



    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        len_p = len(p)
        start = 0
        end = start + len_p
        p_dict = self.strToDict(p)
        tmp_dict = self.strToDict(s[start:end])
        if p_dict == tmp_dict:
            res.append(start)
        while end < len(s):
            end += 1
            tmp_dict[s[start]] -= 1
            if tmp_dict[s[start]] == 0:
                tmp_dict.pop(s[start])
            tmp_dict[s[end-1]] = tmp_dict.get(s[end-1], 0) + 1
            # print(p_dict,tmp_dict)
            start += 1
            if tmp_dict == p_dict:
                res.append(start)
        return res





s = Solution()
s_1 = "cbaebabacd"
p_1 = "abc"
# print(find_all("baa", "aa"))
print(s.findAnagrams("baa", "aa"))
print(s.findAnagrams("aaaaaaaaaaaaa", "aaaaaaaaaa"))
c = "cbaebabacd" 
p = "abc"
print(s.findAnagrams(c, p))
c = "abab" 
p = "ab"
print(s.findAnagrams(c, p))
c = "aa"
p = "bb"
print(s.findAnagrams(c, p))