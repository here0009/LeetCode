"""
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
"""


from typing import List
from bisect import bisect_right
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        # print(ages)
        res = 0
        for age in ages:
            min_age = 0.5*age + 7
            max_age = age
            if age < 100:
                max_age = min(100, max_age)
            i = bisect_right(ages, min_age)
            j = bisect_right(ages, max_age)
            # print(age, i, j, min_age, max_age)
            if i < j:
                res += j-i-(min_age < age <= max_age)
        return res

S = Solution()
ages = [16,16]
print(S.numFriendRequests(ages))
ages = [16,17,18]
print(S.numFriendRequests(ages))
ages = [20,30,100,110,120]
print(S.numFriendRequests(ages))
ages = [101,98,80,20,1,97,3,77,114,109]
print(S.numFriendRequests(ages))
# Output
# 20
# Expected
# 21