"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""
class Solution:
    def canJump(self, nums) -> bool:
        def dfs(index):
            # print(index)
            if index == target or index+nums[index] >= target:
                self.res = True
                return
            for i in range(1,nums[index]+1):
                tmp = index + i
                if not self.res and tmp < length:
                    if not visited[tmp]:
                        visited[tmp] = 1
                        dfs(tmp)
                else:
                    break

        length = len(nums)   
        target = length-1
        visited = [0]*length
        self.res = False
        visited[0] = 1
        dfs(0)
        return self.res

class Solution:
    def canJump(self, nums) -> bool:
        """
        Greedy, mark the range that can be reached with left and right, then start from [left, right], update the range that can be reached in the next jump [right, nxt_right]
        """
        left, right = 0, 0
        while right < len(nums)-1:
            nxt_right = max([i+nums[i] for i in range(left, right+1)])
            if right == nxt_right:
                break
            left, right = right, nxt_right #left can not be right+1, because left may equals to right and nums[left] == 0, so you can not jump anymore


        return right >= len(nums)-1
            

S = Solution()
nums = [2,3,1,1,4]
print(S.canJump(nums))
nums = [3,2,1,0,4]
print(S.canJump(nums))
nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
print(S.canJump(nums))

nums = [3,0,8,2,0,0,1]
print(S.canJump(nums))