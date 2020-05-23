"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        old_r = len(nums)
        old_c = len(nums[0])
        if old_r * old_c != r * c:
            return nums
        else:
            num_counts = 0
            reshaped_nums = []
            for i in range(old_r):
                for j in range(old_c):
                    num_counts += 1
                    # print(num_counts)
                    # print(num_counts//c)
                    if (num_counts-1) % c == 0:
                        reshaped_nums.append([nums[i][j]])
                    else:
                        reshaped_nums[(num_counts-1)//c].append(nums[i][j])
            return reshaped_nums


s = Solution()
nums = [[1,2],[3,4]]
r = 1
c = 4
print(s.matrixReshape(nums, r, c))
nums = [[1,2],[3,4]]
r = 2
c = 4
print(s.matrixReshape(nums, r, c))


class Solution_1:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        temp = [i for row in nums for i in row]
        return [temp[i:i+c] for i in range(0, len(temp), c)]