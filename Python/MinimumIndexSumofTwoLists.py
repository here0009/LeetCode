"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        cmn_rst = set(list1) & set(list2)
        dic1 = {k:i for i,k in enumerate(list1) if k in cmn_rst}
        dic2 = {k:i for i,k in enumerate(list2) if k in cmn_rst}
        min_cmn_index = len(list1) + len(list2)
        res = []
        for rst in cmn_rst:
            tmp_index = dic1[rst] + dic2[rst]
            if tmp_index < min_cmn_index:
                res = [rst]
                min_cmn_index = tmp_index
            elif tmp_index == min_cmn_index:
                res.append(rst)
        return res

s = Solution()
list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(s.findRestaurant(list1, list2))

list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
list2 = ["KFC", "Shogun", "Burger King"]
print(s.findRestaurant(list1, list2))

list1 = ["vacag","KFC"]
list2 = ["fvo","xrljq","jrl","KFC"]
print(s.findRestaurant(list1, list2))