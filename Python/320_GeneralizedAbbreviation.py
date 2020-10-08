"""
Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generalized-abbreviation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def generateAbbreviations(self, word: str):
        """
        wrong answer, did not get abbr such as 1o1d, 1or1
        """
        res = [word]
        length = len(word)
        for j in range(1,length+1):  # j is the length of replaced substring of word
            for i in range(length-j+1):
                res.append(word[:i] + str(j) + word[i+j:])
        return res

class Solution:
    def generateAbbreviations(self, word: str):
        """
        divide and conquer, use list of strs and ints to represent string, and merge lists, if two ints are ajacent, merge the ints
        e.g. [w, 1] + [1, d] => [w, 2, d]
        将输入string分解然后合并， 合并时将相邻的整数相加。
        例如word分解为wo和rd，
        wo : [w1, 1o, 2, wo]
        rd : [r1, 1d, 2, rd]
        合并后即为答案
        """
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

        return [''.join([str(s) for s in lst]) for lst in getAbbr(word)]


# 作者：loick
# 链接：https://leetcode-cn.com/problems/generalized-abbreviation/solution/jian-dan-hui-su-mei-you-wei-yun-suan-by-loick/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def generateAbbreviations(self, word: str):
        def backtrace(curr, i):
            if i == length:
                res.append(curr)
                return
            backtrace(curr + word[i], i+1)  # no replacement
            if not (curr and curr[-1].isdigit()):  # the last letter of curr is not digit, so we can replace the string of word[i:j]
                for j in range(i+1, length+1):
                    backtrace(curr + str(j-i), j)

        length = len(word)
        res = []
        backtrace('', 0)
        return res

class Solution:
    def generateAbbreviations(self, word: str):
        """
        get the binary number < 2**len(word), for input 'word',  they are 0000 ~ 1111,
        if we got 0 do not replace letter, if we got 1 replace it with letter
        """
        length = len(word)
        up = 1 << length
        res = []
        for num in range(up):
            tmp_str = ''
            counts = 0
            tmp_num = num
            for i in range(length-1, -1, -1):
                if tmp_num & 1:
                    counts += 1
                else:
                    tmp_str += str(counts)[::-1] if counts > 0 else ''
                    tmp_str += word[i]
                    counts = 0
                tmp_num = tmp_num >> 1
            tmp_str += str(counts)[::-1] if counts > 0 else ''
            res.append(tmp_str[::-1])
        return res

class Solution:
    def generateAbbreviations(self, word: str):
        """
        get the binary number < 2**len(word), for input 'word',  they are 0000 ~ 1111,
        if we got 0 do not replace letter, if we got 1 replace it with letter
        in this solution word is matching with reverse(bin(num)) which will get the same result as the previous one
        """
        length = len(word)
        up = 1 << length
        res = []
        for num in range(up):
            tmp_str = ''
            counts = 0
            tmp_num = num
            for i in range(length):
                if tmp_num & 1:
                    counts += 1
                else:
                    tmp_str += str(counts) if counts > 0 else ''
                    tmp_str += word[i]
                    counts = 0
                tmp_num = tmp_num >> 1
            tmp_str += str(counts) if counts > 0 else ''
            res.append(tmp_str)
        return res



S = Solution()
word = 'word'
print(S.generateAbbreviations(word))
word = ''
print(S.generateAbbreviations(word))
word = "dictionary"
print(S.generateAbbreviations(word))
