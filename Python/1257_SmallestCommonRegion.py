"""
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region X contains another region Y then X is bigger than Y. Also by definition a region X contains itself.

Given two regions region1, region2, find out the smallest region that contains both of them.

If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is no r2 such that r2 includes r3.

It's guaranteed the smallest region exists.

 

Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"
 

Constraints:

2 <= regions.length <= 10^4
region1 != region2
All strings consist of English letters and spaces with at most 20 letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-common-region
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findSmallestRegion(self, regions, region1: str, region2: str) -> str:
        def dfs(node, res):
            res.append(node)
            if node in root:
                dfs(root[node], res)

        root = dict()
        for lst in regions:
            p = lst[0]
            for q in lst[1:]:
                root[q] = p
        lst1 = []
        lst2 = []
        dfs(region1, lst1)
        dfs(region2, lst2)
        # print(lst1, lst2)
        lst2 = set(lst2)
        for place in lst1:
            if place in lst2:
                return place
        return None

S = Solution()
regions = [["Earth","North America","South America"],["North America","United States","Canada"],["United States","New York","Boston"],["Canada","Ontario","Quebec"],["South America","Brazil"]]
region1 = "Quebec"
region2 = "New York"
print(S.findSmallestRegion(regions, region1, region2))
