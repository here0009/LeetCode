"""
Given a list of strings dict where all the strings are of the same length.

Return True if there are 2 strings that only differ by 1 character in the same index, otherwise return False.

Follow up: Could you solve this problem in O(n*m) where n is the length of dict and m is the length of each string.

 

Example 1:

Input: dict = ["abcd","acbd", "aacd"]
Output: true
Explanation: Strings "abcd" and "aacd" differ only by one character in the index 1.
Example 2:

Input: dict = ["ab","cd","yz"]
Output: false
Example 3:

Input: dict = ["abcd","cccc","abyd","abab"]
Output: true
 

Constraints:

Number of characters in dict <= 10^5
dict[i].length == dict[j].length
dict[i] should be unique.
dict[i] contains only lowercase English letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/strings-differ-by-one-character
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import Counter
from collections import defaultdict
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        """
        TLE
        """
        trans_dict = [''.join(string) for string in list(zip(*dict))]
        counts = Counter()
        # print(trans_dict)
        for string in trans_dict:
            index_list = defaultdict(list)
            for i,v in enumerate(string):
                index_list[v].append(i)
            # print(string, index_list)
            for lst in index_list.values():
                if len(lst) > 1:
                    for i in range(len(lst)-1):
                        for j in range(i+1, len(lst)):
                            counts[(lst[i], lst[j])] += 1
        # print(counts)
        if max(list(counts.values()) + [0]) >= len(dict[0])-1:
            return True
        return False


from typing import List
class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        seen = set()
        for string in dict:
            for j in range(len(string)):
                tmp = string[:j] + '?' + string[j+1:]
                if tmp in seen:
                    return True
                seen.add(tmp)
        return False

S = Solution()
dict = ["abcd","acbd", "aacd"]
print(S.differByOne(dict))
dict = ["ab","cd","yz"]
print(S.differByOne(dict))
dict = ["abcd","cccc","abyd","abab"]
print(S.differByOne(dict))