"""
Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.

 

Example 1:

Input: "cdadabcc"
Output: "adbc"
Example 2:

Input: "abcd"
Output: "abcd"
Example 3:

Input: "ecbacba"
Output: "eacb"
Example 4:

Input: "leetcode"
Output: "letcod"
 

Note:

1 <= text.length <= 1000
text consists of lowercase English letters.
"""
import pysnooper
from collections import Counter
class Solution_1:
    """
    wrong solution
    """
    def smallestSubsequence(self, text: str) -> str:
        
        
        len_text = len(text)
        index, pre = 0, text[0]
        trimmed_text = pre #remove continues repetitive letter in text
        while index < len_text:
            if text[index] == pre:
                index += 1
                continue
            pre = text[index]
            trimmed_text += pre
            index += 1
        print("trimmed_text: ",trimmed_text)

        res = ''
        t_counter = Counter(trimmed_text)
        letters = sorted(list(set(trimmed_text)))
        min_index = 0
        print(letters)
        for i in range(1, len(trimmed_text)):
            pre, curr = trimmed_text[i-1], trimmed_text[i]
            if t_counter[pre] > 0:
                if t_counter[pre] == 1 or (t_counter[curr] == 1 and curr>pre) or pre == letters[min_index]:
                    res += pre
                    t_counter[pre] = -1 #do not add to res anymore
                else:
                    t_counter[pre] -= 1
                while min_index < len(letters):
                    if letters[min_index] not in res:
                        break
                    min_index += 1
            print(res, letters[min_index])
        if trimmed_text[-1] not in res:
            res += trimmed_text[-1]
        return res



from collections import Counter
class Solution_2:
    def smallestSubsequence(self, text: str) -> str:
        t_counter = Counter(text)
        pre_set = set()
        res = ''
        for s in text:
            if t_counter[s] == 1:
                if pre_set:
                    sorted_pre_list = sorted(list(pre_set))
                    index = 0
                    while index < len(sorted_pre_list) and sorted_pre_list[index] <= s:
                        res += sorted_pre_list[index]
                        t_counter[sorted_pre_list[index]] = -1
                        index += 1

                    # res += ''.join(sorted_pre_list[:index])
                    pre_set = set(sorted_pre_list[index:])
                res += s
                t_counter[s] = -1
            if t_counter[s] > 1:
                pre_set.add(s)
                t_counter[s] -= 1
        return res


class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last_index = dict()
        for i,s in enumerate(text):
            last_index[s] = i
        # print(last_index)
        res = ''
        left = 0
        while last_index:
            right = min(last_index.values())
            t,i = min((text[i],i) for i in range(left, right+1) if text[i] in last_index)
            res += t
            left = i+1
            last_index.pop(t)
        return res
        # len_t = len(text)-1
        # for i, s in enumerate(text):
        #     if s not in last_index:
        #         continue
        #     index = len_t
        #     for k, v in last_index.items():
        #         if s <= k and v < index:
        #             index = v
        #     if s not in text[i+1:index+1]:
        #         res += s
        #         print(res,i,index)
        #         last_index.pop(s)
        return res


class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last_index = {t:i for i,t in enumerate(text)}
        # print(last_index)
        stack = []
        for i, t in enumerate(text):
            if t in stack:
                continue
            while stack and stack[-1] > t and last_index[stack[-1]] > i:
                stack.pop()
            stack.append(t)
        return ''.join(stack)


s = Solution_3()

text = "cdadabcc"
print(s.smallestSubsequence(text))
text = "abcd"
print(s.smallestSubsequence(text))
text = "ecbacba"
print(s.smallestSubsequence(text))
text = "leetcode"
print(s.smallestSubsequence(text))
text = "e"
print(s.smallestSubsequence(text))
text = "cbaacabcaaccaacababa"
print(s.smallestSubsequence(text))
text = "fbhdbdgadeighfcefdgccchbcigcaebchegeebagbhfcbhfdib"
print(s.smallestSubsequence(text))
# Output:
# "abceghfdi"
# Expected:
# "abcegfhdi"
