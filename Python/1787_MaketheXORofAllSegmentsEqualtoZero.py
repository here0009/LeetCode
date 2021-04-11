"""
You are given an array nums​​​ and an integer k​​​​​. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

Return the minimum number of elements to change in the array such that the XOR of all segments of size k​​​​​​ is equal to zero.


Example 1:

Input: nums = [1,2,0,3,0], k = 1
Output: 3
Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
Example 2:

Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
Output: 3
Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
Example 3:

Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
Output: 3
Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].
 

Constraints:

1 <= k <= nums.length <= 2000
​​​​​​0 <= nums[i] < 210
"""


from typing import List
from collections import Counter
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        """
        Thoughts: 
        there are len(nums) - k + 1 groups.
        we can convert the list with at most len(nums) - k + 1 modifications, at least 0 modifications
        """
        len_nums = len(nums)
        if k == 1:
            return sum([_n > 0 for _n in nums])
        kmers = Counter()
        for i in range(len_nums - k + 2):
            kmers[tuple(sorted(nums[i: i + k - 1]))] += 1
        print(kmers)
        m_keys = kmers.most_common()[0]
        val = 0
        for _k in m_keys:
            val ^= _k
        for i in range(len_nums - k + 2):
            pass



# 作者：yuan-zhi-b
# 链接：https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero/solution/python3-dong-tai-gui-hua-yi-huo-jie-guo-6kkyf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        freq=defaultdict(Counter)
        for i in range(k):
            for j in range(i,len(nums),k):
                freq[i][nums[j]]+=1
        dp=[[math.inf]*(2**11) for _ in range(len(freq)+1)]
        dp[-1][0]=0
        for i in range(k-1,-1,-1):
            mindp=min(dp[i+1])
            itemCnt=sum(freq[i].values())
            for xor in range(1025):
                res=itemCnt+mindp
                for key,cnt in freq[i].items(): # change all nums in 'i' set to v
                    res=min(res,itemCnt-cnt+dp[i+1][xor^key])
                dp[i][xor]=res
        return dp[0][0]



from typing import List
from collections import Counter
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:        

S = Solution()
nums = [1,2,0,3,0]
k = 1
print(S.minChanges(nums, k))
nums = [3,4,5,2,1,7,3,4,7]
k = 3
print(S.minChanges(nums, k))
nums = [1,2,4,1,2,5,1,2,6]
k = 3
print(S.minChanges(nums, k))
