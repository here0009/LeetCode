"""
A string such as "word" contains the following abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

Examples:

"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
 

Constraints:

In the case of multiple answers as shown in the second example below, you may return any one of them.
Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-unique-word-abbreviation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minAbbreviation(self, target: str, dictionary) -> str:
        """
        did not work for the test case:
        target ="apple"
        dictionary = ["applt","hpple"]
        """

        length = len(target)
        d_set = set(d for d in dictionary if len(d) == length)
        if not d_set:
            return str(length)
        if target in d_set:
            return None
        for j in range(1,length+1):  # j is the length of comparision
            for i in range(length-j+1):
                tmp = target[i:i+j]
                if all(word[i:i+j] != tmp for word in d_set):
                    pre = str(i) if i > 0 else ''
                    suff = str(length-(i+j)) if length > i+j else ''
                    return pre + tmp + suff
        return target



class Solution:
    def minAbbreviation(self, target: str, dictionary) -> str:
        def getAbbr(word):
            length = len(word)
            res = []
            if length == 0:
                return [['']]
            if length == 1:
                return [[1], [word]]
            lst1 = getAbbr(word[:length//2])
            lst2 = getAbbr(word[length//2:])
            for r1 in lst1:
                for r2 in lst2:
                    if r1 and r2 and (type(r1[-1]) is int) and (type(r2[0]) is int):
                        res.append(r1[:-1] + [r1[-1]+r2[0]] + r2[1:])
                    else:
                        res.append(r1 + r2)
            return res

        def compare(abbr, word):
            """
            abbr is one of the list representation of the target, e.g. word => ['w',2,'d']
            """
            len_a, len_w = len(abbr), len(word)
            i, j = 0, 0
            # print(i, j, abbr, word)
            while i < len_a and j < len_w:
                if type(abbr[i]) is int:
                    j += abbr[i]
                    i += 1
                else:
                    if abbr[i] != word[j]:
                        return False
                    i += 1
                    j += 1
            return i == len_a and j == len_w

        length = len(target)
        d_set = set(d for d in dictionary if len(d) == length)
        # print('+++++++++++++++++')
        # print(target, dictionary)
        # print(d_set)
        if not d_set:
            return str(length)
        if target in d_set:
            return None

        target_list = sorted(getAbbr(target), key = lambda x:len(x))
        # print(target_list)
        for abbr in target_list:
            if any(compare(abbr, d) for d in d_set):
                continue
            else:
                return ''.join(str(s) for s in abbr)
        return target

S = Solution()
target = "apple"
dictionary = ["blade"]
print(S.minAbbreviation(target, dictionary))
target = "apple"
dictionary = ["plain", "amber", "blade"]
print(S.minAbbreviation(target, dictionary))

target = "apple"
dictionary = ["kkkk"]
print(S.minAbbreviation(target, dictionary))

target ="apple"
dictionary = ["applt","hpple"]
print(S.minAbbreviation(target, dictionary))