"""
A string S represents a list of words.

Each letter in the word has 1 or more options.  If there is one option, the letter is represented as is.  If there is more than one option, then curly braces delimit the options.  For example, "{a,b,c}" represents options ["a", "b", "c"].

For example, "{a,b,c}d{e,f}" represents the list ["ade", "adf", "bde", "bdf", "cde", "cdf"].

Return all words that can be formed in this manner, in lexicographical order.

 

Example 1:

Input: "{a,b}c{d,e}f"
Output: ["acdf","acef","bcdf","bcef"]
Example 2:

Input: "abcd"
Output: ["abcd"]
 

Note:

1 <= S.length <= 50
There are no nested curly brackets.
All characters inside a pair of consecutive opening and ending curly brackets are different.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/brace-expansion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def expand(self, S: str) :
        res = ['']
        stack = []
        flag = False
        tmp = ''
        for letter in S:
            if letter == '{':
                flag = True
                res = [s+tmp for s in res]
                tmp = ''
            elif letter == '}':
                flag = False
                res2 = []
                for t in stack:
                    res2.extend([s+t for s in res])
                stack = []
                res = res2
            elif letter.isalpha():
                if flag:
                    stack.append(letter)
                else:
                    tmp += letter
            # print(letter, stack, res)
        if tmp:
            res = [s+tmp for s in res]
        return sorted(res)


class Solution:
    def expand(self, S: str) :
        def dfs(index, path):
            if index == len_lst:
                self.res.append(path)
                return
            for string in lst[index]:
                dfs(index+1, path+string)

        self.res = []
        index = 0
        length = len(S)
        lst = []
        tmp = ''
        while index < length:
            if S[index] == '{':
                if tmp:
                    lst.append([tmp])
                    tmp = ''
                j = S.find('}', index+1)
                lst.append(S[index+1:j].split(','))
                index = j+1

            else:
                tmp += S[index]
                index += 1
        if tmp:
            lst.append([tmp])
        len_lst = len(lst)
        # print(lst)
        dfs(0, '')
        return sorted(self.res)


# 作者：intoloop
# 链接：https://leetcode-cn.com/problems/brace-expansion/solution/python-by-intoloop-22/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
class Solution:
    def expand(self, S: str) -> List[str]:
        res=['']
        n=len(S)
        i=0
        while i<n:
            cur=[]
            if S[i]=='{':
                j=i
                while S[j]!='}':
                    j+=1
                cur=S[i+1:j].split(',')
                i=j+1
            else:
                j=i
                while j<n and S[j]!='{':
                    j+=1
                cur=[S[i:j]]
                i=j
            res=[i+j for i in res for j in cur]
        return sorted(res)

                




Slt = Solution()
S = "{a,b}c{d,e}f"
print(Slt.expand(S))
S = "abcd"
print(Slt.expand(S))