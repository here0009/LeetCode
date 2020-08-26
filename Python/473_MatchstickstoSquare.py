"""
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:
Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:
Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.
Note:
The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15
"""


class Solution:
    def makesquare(self, nums) -> bool:
        """
        check if there are 4 of sum(nums)/4
        """
        def dfs(counts, index, curr):
            if index == length:
                if counts == 4 and curr == 0:
                    self.res = True
                return
            for i in range(index, length):
                visited[i] = True
                tmp = curr + nums[index]
                if tmp == target:
                    dfs(counts+1, index+1, 0)
                elif tmp < target:
                    dfs(counts, index+1, tmp)



        length = len(nums)
        visited = [0]*length
        self.res = False
        target = sum(nums)/4
        if target != int(target):
            return False
        target = int(target)
        dfs(0, 0, 0)


class Solution:
    def makesquare(self, nums) -> bool:
        """
        check if there are 4 of sum(nums)/4
        TLE
        """
        def dfs(index):
            # print(index, sums)
            if self.res:
                return
            if index == length:
                for n in sums:
                    if n != target:
                        break
                else:
                    # print(sums)
                    self.res = True
                return
            # for i in range(index, length):
            for j in range(4):
                tmp, pre = sums[j] + nums[i], sums[j]
                if tmp <= target:
                    sums[j] = tmp
                    dfs(index+1)
                    sums[j] = pre

        if not nums:
            return False
        length = len(nums)
        # visited = [0]*length
        self.res = False
        target = sum(nums)/4
        if target != int(target):
            return False

        target = int(target)
        sums = [0]*4
        dfs(0)
        return self.res



from collections import Counter
class Solution_1:
    def makesquare(self, nums) -> bool:
        def dfs(index, counter):
            # print(index, counter)
            if index == length:
                return len(counter) == 1 and counter[target] == 4
            counter2 = Counter()
            for k, v in counter.items():
                counter2[k] = v
            for k, v in counter.items():
                tmp = nums[index] + k
                if tmp <= target:
                    counter2[tmp] += 1
                    counter2[k] -= 1
                    if counter2[k] == 0:
                        del counter2[k]
                    if dfs(index+1, counter2):
                        return True
                    counter2[tmp] -= 1
                    counter2[k] += 1
            return False

        if not nums:
            return False
        nums.sort(reverse = True)
        length = len(nums)
        # visited = [0]*length
        target = sum(nums)/4
        if target != int(target):
            return False

        target = int(target)
        counter = Counter([0]*4)
        return dfs(0, counter)
         




# https://leetcode.com/problems/matchsticks-to-square/solution/
class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # If there are no matchsticks, then we can't form any square
        if not nums:
            return False

        # Number of matchsticks we have
        L = len(nums)

        # Perimeter of our square (if one can be formed)
        perimeter = sum(nums)

        # Possible side of our square.
        possible_side =  perimeter // 4

        # If the perimeter can be equally split into 4 parts (and hence 4 sides, then we move on).
        if possible_side * 4 != perimeter:
            return False

        # Reverse sort the matchsticks because we want to consider the biggest one first.
        nums.sort(reverse=True)

        # This array represents the 4 sides and their current lengths
        sums = [0 for _ in range(4)]

        # Our recursive dfs function.
        def dfs(index):

            # If we reach the end of matchsticks array, we check if the square was formed or not
            if index == L:
                # If 3 equal sides were formed, 4th will be the same as these three and answer should be True in that case.
                return sums[0] == sums[1] == sums[2] == possible_side

            # The current matchstick can belong to any of the 4 sides (provided their remaining lenghts are >= the size of the current matchstick)
            for i in range(4):
                # If this matchstick can fir in the space left for the current side
                if sums[i] + nums[index] <= possible_side:
                    # Recurse
                    sums[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    # Revert the effects of recursion because we no longer need them for other recursions.
                    sums[i] -= nums[index]
            return False        
        return dfs(0)



def makesquare(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    # If there are no matchsticks, then we can't form any square.
    if not nums:
        return False

    # Number of matchsticks
    L = len(nums)

    # Possible perimeter of our square
    perimeter = sum(nums)

    # Possible side of our square from the given matchsticks
    possible_side =  perimeter // 4

    # If the perimeter isn't equally divisible among 4 sides, return False.
    if possible_side * 4 != perimeter:
        return False

    # Memoization cache for the dynamic programming solution.
    memo = {}

    # mask and the sides_done define the state of our recursion.
    def recurse(mask, sides_done):

        # This will calculate the total sum of matchsticks used till now using the bits of the mask.
        total = 0
        for i in range(L - 1, -1, -1):
            if not (mask & (1 << i)):
                total += nums[L - 1 - i]

        # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
        if total > 0 and total % possible_side == 0:
            sides_done += 1

        # If we were successfully able to form 3 sides, return True
        if sides_done == 3:
            return True

        # If this recursion state has already been calculated, just return the stored value.
        if (mask, sides_done) in memo:
            return memo[(mask, sides_done)]

        # Common variable to store answer from all possible further recursions from this step.
        ans = False

        # rem stores available space in the current side (incomplete).
        c = int(total / possible_side)
        rem = possible_side * (c + 1) - total

        # Iterate over all the matchsticks
        for i in range(L - 1, -1, -1):

            # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
            if nums[L - 1 - i] <= rem and mask&(1 << i):

                # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                if recurse(mask ^ (1 << i), sides_done):
                    ans = True
                    break
        # cache the result for the current recursion state.            
        memo[(mask, sides_done)] = ans
        return ans

    # recurse with the initial mask with all matchsticks available.
    return recurse((1 << L) - 1, 0)


class Solution:
    def makesquare(self, nums) -> bool:
        """
        check if there are 4 of sum(nums)/4
        """
        def dfs(index):
            if index == length:
                for n in sums:
                    if n != target:
                        break
                else:
                    return True
                return False
            # for i in range(index, length):
            for j in range(4):
                if j > 0 and sums[j] == sums[j-1]:
                    continue
                tmp, pre = sums[j] + nums[index], sums[j]
                if tmp <= target:
                    sums[j] = tmp
                    if dfs(index+1):
                        return True
                    sums[j] = pre
            return False

        if not nums:
            return False
        nums.sort(reverse = True)
        length = len(nums)
        # visited = [0]*length
        target = sum(nums)/4
        if target != int(target):
            return False
        target = int(target)
        sums = [0]*4
        return dfs(0)
        
S = Solution()
nums = [1,1,2,2,2]
print(S.makesquare(nums))
nums = [3,3,3,3,4]
print(S.makesquare(nums))
nums = []
print(S.makesquare(nums))
nums = [5,5,5,5,4,4,4,4,3,3,3,3]
print(S.makesquare(nums))
nums = [1569462,2402351,9513693,2220521,7730020,7930469,1040519,5767807,876240,350944,4674663,4809943,8379742,3517287,8034755]
print(S.makesquare(nums))