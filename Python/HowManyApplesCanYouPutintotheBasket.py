"""
You have some apples, where arr[i] is the weight of the i-th apple.  You also have a basket that can carry up to 5000 units of weight.

Return the maximum number of apples you can put in the basket.

 

Example 1:

Input: arr = [100,200,150,1000]
Output: 4
Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.
Example 2:

Input: arr = [900,950,800,1000,700,800]
Output: 5
Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.
 

Constraints:

1 <= arr.length <= 10^3
1 <= arr[i] <= 10^3
"""
class Solution:
    def maxNumberOfApples(self, arr):
        capacity = 5000
        arr = sorted(arr)
        counts = 0
        weights = 0
        for n in arr:
            weights += n
            if weights > capacity:
                break
            else:
                counts += 1
        return counts

s = Solution()
arr = [100,200,150,1000]
print(s.maxNumberOfApples(arr))

arr = [900,950,800,1000,700,800]
print(s.maxNumberOfApples(arr))