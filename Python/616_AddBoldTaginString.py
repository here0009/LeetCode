"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
 

Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
 

Constraints:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
Note: This question is the same as 758: https://leetcode.com/problems/bold-words-in-string/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-bold-tag-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addBoldTag(self, string: str, words) -> str:
        def findall(string, word):
            res = []
            index = string.find(word)
            len_w = len(word)
            while index < len(string) and index != -1:
                res.append((index, index+len_w))
                index = string.find(word, index+1) # the word may overlap with itself, so index+1, not index + len_w
            return res

        index_list = []
        for word in words:
            index_list.extend(findall(string, word))
        if not index_list:
            return string
        # print(index_list)
        index_list.sort()

        merged_list = []
        pre, latter = index_list[0]
        for i,j in index_list[1:]:
            if i <= latter:
                latter = max(latter, j)
            else:
                merged_list.append((pre, latter))
                pre, latter = i, j
        merged_list.append((pre, latter))

        # print(merged_list)
        res = ''
        index = 0
        for p, q in merged_list:
            res += string[index:p]
            res += '<b>{}</b>'.format(string[p:q])
            index = q
        res += string[index:]
        return res

S = Solution()
string = "aaabbcckaaabc"
words = ["aaa","aab","bc"]
print(S.addBoldTag(string, words))
string ="aaabbcc"
words = []
print(S.addBoldTag(string, words))

"qrzjsorbkmyzzzvoqxefvxkcwtpkhzbakuufbpgdkykmojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmweyyzzmgcoiupjnidphvzlnxtcogufozlenjfvokztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm"
["qr","zj","so","rb","km","yz","zz","vo","qx","ef","vx","kc","wt","pk"]

# Output
"<b>qrzjsorbkmyzz</b>z<b>voqxefvxkcwtpk</b>hzbakuufbpgdky<b>km</b>ojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmwey<b>yzz</b>mgcoiupjnidphvzlnxtcogufozlenjf<b>vo</b>kztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm"

# Expected
"<b>qrzjsorbkmyzzzvoqxefvxkcwtpk</b>hzbakuufbpgdky<b>km</b>ojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmwey<b>yzz</b>mgcoiupjnidphvzlnxtcogufozlenjf<b>vo</b>kztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm"