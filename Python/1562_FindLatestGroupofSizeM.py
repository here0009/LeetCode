"""
Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that initially has all its bits set to zero.

At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.

Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

 

Example 1:

Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.
Example 2:

Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.
Example 3:

Input: arr = [1], m = 1
Output: 1
Example 4:

Input: arr = [2,1], m = 2
Output: 2
 

Constraints:

n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= n
All integers in arr are distinct.
1 <= m <= arr.length
"""



class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        """
        TLE
        """
        target = 2**m - 1
        length = len(arr)
        rev_arr = arr[::-1]
        curr = ['1']*length
        for i,v in enumerate(rev_arr):
            curr_str_list = ''.join(curr).split('0')
            # print(v, curr_str_list)
            max_len = 0
            for j in curr_str_list:
                if len(j) == m:
                    return length - i
                max_len = max(max_len, len(j))
            if max_len < m:
                break
            curr[v-1] = '0'
        return -1

class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        length = len(arr)
        rev_arr = arr[::-1]
        str_set = set()
        str_set.add((1,length+1))
        for i,v in enumerate(rev_arr):
            # print(i,v,str_set)
            if not str_set:
                break
            str_set2 = set()
            for left, right in str_set:
                # print(left, right)
                if right - left < m:
                    continue
                elif right - left == m:
                    return length-i
                else:
                    if v >= left and v < right:
                        str_set2.add((left, v))
                        str_set2.add((v+1, right))
                    else:
                        str_set2.add((left, right))
            str_set = str_set2
        return -1

class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        print(arr)
        if m==len(arr): return m
        
        border=[0]*(len(arr)+2)
        ans=-1
        
        for i in range(len(arr)):
            left=right=arr[i]
            if border[right+1]>0: 
                right=border[right+1]
            if border[left-1]>0: 
                left=border[left-1]
            border[left], border[right] = right, left
            print(left, arr[i], right, border)
            if (right-arr[i]==m) or (arr[i]-left ==m): ans=i
        
        return ans
        
# https://leetcode.com/submissions/detail/385018765/
import bisect
class Solution:
    def findLatestStep(self, arr, k: int) -> int:
        if len(arr) == k:
            return len(arr)
        n = len(arr)
        save = [0, n + 1]
        print(arr, k)
        while arr:
            cur = arr.pop()
            index = bisect.bisect(save, cur)
            left, right = cur - save[index - 1] - 1, save[index] - cur - 1
            print(save, cur, index, left, right)
            if left == k or right == k:
                return len(arr) # the index of the poped item
            if save[index] - save[index - 1] - 1 > k:
                save.insert(index, cur)
        return -1

S = Solution()
arr = [3,5,1,2,4]
m = 1
print(S.findLatestStep(arr, m))
arr = [3,1,5,4,2]
m = 2
print(S.findLatestStep(arr, m))
arr = [1]
m = 1
print(S.findLatestStep(arr, m))
arr = [2,1]
m = 2
print(S.findLatestStep(arr, m))