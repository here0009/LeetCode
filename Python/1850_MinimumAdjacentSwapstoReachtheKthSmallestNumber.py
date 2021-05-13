"""
You are given a string num, representing a large integer, and an integer k.

We call some integer wonderful if it is a permutation of the digits in num and is greater in value than num. There can be many wonderful integers. However, we only care about the smallest-valued ones.

For example, when num = "5489355142":
The 1st smallest wonderful integer is "5489355214".
The 2nd smallest wonderful integer is "5489355241".
The 3rd smallest wonderful integer is "5489355412".
The 4th smallest wonderful integer is "5489355421".
Return the minimum number of adjacent digit swaps that needs to be applied to num to reach the kth smallest wonderful integer.

The tests are generated in such a way that kth smallest wonderful integer exists.

 

Example 1:

Input: num = "5489355142", k = 4
Output: 2
Explanation: The 4th smallest wonderful number is "5489355421". To get this number:
- Swap index 7 with index 8: "5489355142" -> "5489355412"
- Swap index 8 with index 9: "5489355412" -> "5489355421"
Example 2:

Input: num = "11112", k = 4
Output: 4
Explanation: The 4th smallest wonderful number is "21111". To get this number:
- Swap index 3 with index 4: "11112" -> "11121"
- Swap index 2 with index 3: "11121" -> "11211"
- Swap index 1 with index 2: "11211" -> "12111"
- Swap index 0 with index 1: "12111" -> "21111"
Example 3:

Input: num = "00123", k = 1
Output: 1
Explanation: The 1st smallest wonderful number is "00132". To get this number:
- Swap index 3 with index 4: "00123" -> "00132"
 

Constraints:

2 <= num.length <= 1000
1 <= k <= 1000
num only consists of digits.
"""


# next permutation:  https://leetcode-cn.com/problems/next-permutation/solution/xia-yi-ge-pai-lie-by-leetcode-solution/
class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        """
        1. find the kth smallest  number (kth permutation of num)
        2. calculate the distance
        """
        def next_perm(nums):
            """
            get the next premutation of nums, modify nums inplace, return None
            """
            if len(nums) < 2:
                return
            i = len(nums) - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            # nums[i] < nums[i + 1]
            # nums[i + 1:] is non-increasing
            if i < 0:
                return
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # nums[j] > nums[i], j is the right most index
            # nums[i] > nums[j + 1], nums[i] < nums[j] < nums[j - 1], so after we swap nums[i] and nums[j], nums[i + 1:] is still decreasing
            nums[i], nums[j] = nums[j], nums[i]
            # because nums[i+1:] is decreasing, we just need to reverse it to get the increasing one
            left, right = i + 1, len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        target = list(num)
        while k > 0:
            next_perm(target)
            k -= 1
        nums = list(num)
        length = len(nums)
        res = 0
        for i in range(length):
            if nums[i] != target[i]:
                for j in range(i + 1, length):
                    if nums[j] == target[i]:
                        break
                for k in range(j, i, -1):
                    res += 1
                    nums[k], nums[k - 1] = nums[k - 1], nums[k]
        return res

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:

        def findnext_nums(nums):
            for i in range(n-1,0,-1):
                if nums[i-1] < nums[i]:   #找到后面数字比前面数字大的情况，不加这行会导致超时，具体情况可以试试
                    for j in range(n-1,i-1,-1):   #从后往前遍历到索引i-1的前面
                        if nums[i-1] < nums[j]:   #从后往前找到数字比nums[i-1]大的数字
                            nums[i-1],nums[j] = nums[j],nums[i-1]    #交换这两个数字
                            nums[i:] = sorted(nums[i:])       #将i-1之后的数子排序，因为这样才是最小妙数
                            return nums

        n = len(num); nums = list(num); num = list(num)
        for _ in range(k):
            nums = findnext_nums(nums)
        
        cnt = 0
        for i in range(n):
            if num[i] != nums[i]:  #如果这两个数组的数字不相等
                for j in range(i+1,n):
                    if num[j] == nums[i]:    #从原数组往后找，找到和现数组相等的数
                        cnt += j-i           #两个索引的差就是交换次数
                        num[i+1:j+1] = num[i:j]    #将原数组两个索引对应的位置前进一格，也就是交换的结果
                                                   #不过原数组的i没有替换，但并不影响后面
                        break
        return cnt

# 作者：luo_luo
# 链接：https://leetcode-cn.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/solution/lin-wei-jiao-huan-de-zui-xiao-ci-shu-pyt-duju/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
S = Solution()
num = "5489355142"
k = 4
print(S.getMinSwaps(num, k))
num = "11112"
k = 4
print(S.getMinSwaps(num, k))
num = "00123"
k = 1
print(S.getMinSwaps(num, k))