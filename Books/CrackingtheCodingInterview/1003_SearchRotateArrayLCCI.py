"""
搜索旋转数组。给定一个排序后的数组，包含n个整数，但这个数组已被旋转过很多次了，次数不详。请编写代码找出数组中的某个元素，假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。

示例1:

 输入: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
 输出: 8（元素5在该数组中的索引）
示例2:

 输入：arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
 输出：-1 （没有找到）
提示:

arr 长度范围在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-rotate-array-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
英文题目更加清晰，one rotate operateiont is put the 1st element to the last of the array
"""

"""
Given a sorted array of n integers that has been rotated an unknown number of times, write code to find an element in the array. You may assume that the array was originally sorted in increasing order. If there are more than one target elements in the array, return the smallest index.

Example1:

 Input: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 5
 Output: 8 (the index of 5 in the array)
Example2:

 Input: arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], target = 11
 Output: -1 (not found)
Note:

1 <= arr.length <= 1000000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-rotate-array-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# 作者：armeria-program
# 链接：https://leetcode-cn.com/problems/search-rotate-array-lcci/solution/er-fen-fa-by-armeria-program/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:                                         # 循环结束条件left==right
            mid = (left + right) >> 1
            if nums[left] < nums[mid]:                              # 如果左值小于中值，说明左边区间升序 
                if nums[left] <= target and target <= nums[mid]:    # 如果目标在左边的升序区间中，右边界移动到mid
                    right = mid
                else:                                               # 否则目标在右半边，左边界移动到mid+1
                    left = mid + 1
            elif nums[left] > nums[mid]:                            # 如果左值大于中值，说明左边不是升序，右半边升序
                if nums[left] <= target or target <= nums[mid]:     # 如果目标在左边，右边界移动到mid
                    right = mid
                else:                                               # 否则目标在右半边的升序区间中，左边界移动到mid+1
                    left = mid + 1
            elif nums[left] == nums[mid]:                           # 如果左值等于中值，可能是已经找到了目标，也可能是遇到了重复值
                if nums[left] != target:                            # 如果左值不等于目标，说明还没找到，需要逐一清理重复值
                    left += 1                                        
                else:                                               # 如果左值等于目标，说明已经找到最左边的目标值
                    right = left                                    # 将右边界移动到left，循环结束
        return left if nums[left] == target else -1                 # 返回left，或者-1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[left] > nums[mid]:
                if nums[left] <= target or target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            elif nums[left] == nums[mid]:
                if nums[left] != target:
                    left += 1
                else:
                    right = left
        return left if nums[left] == target else -1

