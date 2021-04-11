"""
在老式手机上，用户通过数字键盘输入，手机将提供与这些数字相匹配的单词列表。每个数字映射到0至4个字母。给定一个数字序列，实现一个算法来返回匹配单词的列表。你会得到一张含有有效单词的列表。映射如下图所示：



示例 1:

输入: num = "8733", words = ["tree", "used"]
输出: ["tree", "used"]
示例 2:

输入: num = "2", words = ["a", "b", "c", "d"]
输出: ["a", "b", "c"]
提示：

num.length <= 1000
words.length <= 500
words[i].length == num.length
num中不会出现 0, 1 这两个数字

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/t9-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



from typing import List
class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:

        word_dict = {'abc':'2', 'def':'3', 'ghi':'4', 'jkl':'5', 'mno':'6', 'pqrs':'7', 'tuv':'8', 'wxyz':'9'}
        letter_dict = dict()
        for key, val in word_dict.items():
            for letter in list(key):
                letter_dict[letter] = val
        # print(letter_dict)
        res = []
        for word in words:
            tmp = ''.join(letter_dict[w] for w in word)
            if tmp == num:
                res.append(word)
        return res



class Solution:
    def getValidT9Words(self, num: str, words: List[str]) -> List[str]:

        word_dict = {'abc':'2', 'def':'3', 'ghi':'4', 'jkl':'5', 'mno':'6', 'pqrs':'7', 'tuv':'8', 'wxyz':'9'}
        letter_dict = dict()
        for key, val in word_dict.items():
            for letter in list(key):
                letter_dict[letter] = val
        length = len(num)
        res = []
        for word in words:
            for idx in range(length):
                if num[idx] != letter_dict[word[idx]]:
                    break
            else:
                res.append(word)
        return res

S = Solution()
num = "8733"
words = ["tree", "used"]
print(S.getValidT9Words(num, words))
num = "2"
words = ["a", "b", "c", "d"]
print(S.getValidT9Words(num, words))
