"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]
"""
class Solution_1:
    def largestDivisibleSubset(self, nums):
        # len_n = len(nums)
        # matrix = [[0]*len_n for _ in range(len_n)]
        # for i in range(len_n-1):
        #     for j in range(i+1, len_n):
        #         if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
        #             matrix[i][j] = 1
        #             matrix[j][i] = 1
        """
        TLE
        """
        res_list = [[]]
        for n in nums:
            tmp = []
            for l in res_list:
                if len(l) == 0 or all(n%m == 0 or m%n == 0 for m in l):
                    tmp.append(l+[n])
            res_list.extend(tmp)
        # print(res_list)
        return sorted(res_list, key = lambda x:len(x))[-1]

class Solution:
    def largestDivisibleSubset(self, nums):
        # len_n = len(nums)
        # matrix = [[0]*len_n for _ in range(len_n)]
        # for i in range(len_n-1):
        #     for j in range(i+1, len_n):
        #         if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
        #             matrix[i][j] = 1
        #             matrix[j][i] = 1
        res_list = [[]]
        max_len = 0
        len_n = len(nums)
        rest_num = len_n
        for n in nums:
            # n = nums[i]
            tmp = []
            for i in range(len(res_list)):
                l = res_list[i]
                if len(l) + rest_num <= max_len:
                    # res_list.pop(i)
                    continue
                if len(l) == 0:
                    tmp.append([n])
                else:
                    for m in l:
                        if n%m != 0 and m%n != 0:
                            break
                    else:
                        tmp.append(l+[n])
                        max_len = max(max_len, len(l)+1)
            res_list.extend(tmp)
            rest_num -= 1

        # print(res_list)
        return sorted(res_list, key = lambda x:len(x))[-1]

class Solution:
    def largestDivisibleSubset(self, nums):
        res_set = set(())
        max_len = 0
        len_n = len(nums)
        rest_num = len_n
        for n in nums:
            # n = nums[i]
            tmp = set()
            res_set.add({n})
            for l in res_set:
                print('l',l,len(l))
                if len(l) + rest_num <= max_len:
                    res_set.pop(l)
                    continue
                else:
                    for m in l:
                        if n%m != 0 and m%n != 0:
                            break
                    else:
                        tmp.add(l.add(n))
                        max_len = max(max_len, len(l)+1)
            print(tmp)
            res_set |= tmp
            # print(res_set)
            rest_num -= 1

        print(res_set)
        # return sorted(res_list, key = lambda x:len(x))[-1]

class Solution:
    def largestDivisibleSubset(self, nums):
        """
        TLE
        """
        nums = sorted(nums)
        res_list = [[]]
        len_n = len(nums)
        rest_num = len_n
        max_len = 0
        for n in nums:
            tmp = []
            pop_index = []
            for i in range(len(res_list)):
                l = res_list[i]
                if len(l) + rest_num <= max_len:
                    pop_index.append(i)
                    continue
                if len(l) == 0 or n % l[-1] == 0:
                    tmp.append(l+[n])
                    max_len = max(max_len, len(l)+1)
            for i in sorted(pop_index, reverse = True):
                res_list.pop(i)
            res_list.extend(tmp)
            rest_num -= 1
        # print(res_list)
        return sorted(res_list, key = lambda x:len(x))[-1]

class Solution:
    def largestDivisibleSubset(self, nums):
        #dp[i] stores the largest res ends with i
        #divisibility is transductive, in anscending list [i,j,k], if j%i == 0 and k%j == 0, then k%i == 0
        dp = {-1:set()}
        nums = sorted(nums)
        for n in nums:
            dp[n] = max([dp[s] for s in dp if n % s == 0], key = len) | {n}
        # print(dp)
        return  list(max(dp.values(), key = len))

class Solution:
    def largestDivisibleSubset(self, nums):
        dp = [[]]
        nums = sorted(nums)
        for n in nums:
            dp.append([n] + max((s for s in dp if  len(s) == 0 or n%s[0] == 0) ,key = len))
        return max(dp, key = len)


s = Solution()
nums = [1,2,3]
print(s.largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(s.largestDivisibleSubset(nums))