"""
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
提示:

words的长度在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sparse-array-search-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def findString(self, words: List[str], target: str) -> int:
        def search_list(left, right):
            # print('1st', left, right, words[left], words[right])
            if left == right:
                return left if words[left] == target else None
            if left > right:
                return None
            mid = (left + right) // 2
            word = words[mid]
            if word == "":
                return search_list(left, mid - 1) or search_list(mid + 1, right)
            if word == target:
                return mid
            if word < target:
                return search_list(mid + 1, right)
            else:
                return search_list(left, mid - 1)


        res = search_list(0, len(words) - 1)
        return res if res is not None else -1

S = Solution()
words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]
target = "ta"
print(S.findString(words, target))

words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""]
target = "ball"
print(S.findString(words, target))

words = ["DirNnILhARNS hOYIFB", "SM ", "YSPBaovrZBS", "evMMBOf", "mCrS", "oRJfjw gwuo", "xOpSEXvfI"]
target = "mCrS"
print(S.findString(words, target))