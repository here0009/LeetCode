"""
We have a sequence of books: the i-th book has thickness books[i][0] and height books[i][1].

We want to place these books in order onto bookcase shelves that have total width shelf_width.

We choose some of the books to place on this shelf (such that the sum of their thickness is <= shelf_width), then build another level of shelf of the bookcase so that the total height of the bookcase has increased by the maximum height of the books we just put down.  We repeat this process until there are no more books to place.

Note again that at each step of the above process, the order of the books we place is the same order as the given sequence of books.  For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, the third book on the second shelf, and the fourth and fifth book on the last shelf.

Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
Output: 6
Explanation:
The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.
 

Constraints:

1 <= books.length <= 1000
1 <= books[i][0] <= shelf_width <= 1000
1 <= books[i][1] <= 1000
"""
"""
1. place the book on another floor
2. try to place  the previous books to the same floor
"""
class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf') for _ in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            max_width = shelf_width
            max_height = 0
            j = i - 1
            print('=============')
            print(i, books[i-1])
            while j >= 0 and max_width - books[j][0] >= 0:
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + max_height)
                print(j)
                print(dp)
                j -= 1
            # print(dp)
        return dp[n]

# https://leetcode.com/problems/filling-bookcase-shelves/discuss/323415/simple-Python-DP-solution
class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1) # dp[i] indicates min height for books 0 to i - 1
        dp[0] = 0 # no book, no height
        # dynamic programming
        for i in range(1, n + 1):
            curr_width, curr_height = shelf_width, 0
            j = i - 1
            #It is actually that in the beginning of iteration j = i - 1, the very last book is put in a separate row; in the other iterations, more previous books are pushed to this row.
            # print(dp)
            while j >= 0 and curr_width - books[j][0] >= 0:
                # put book j into this row & update info
                curr_width -= books[j][0]
                curr_height = max(curr_height, books[j][1])
                dp[i] = min(dp[i], dp[j] + curr_height)
                j -= 1
        # print(dp)
        return dp[n]
# https://leetcode.com/problems/filling-bookcase-shelves/discuss/323291/Python-DP-with-recursion-and-cache
from functools import lru_cache
class Solution:
    def minHeightShelves(self, books, shelf_width: int) -> int:
        @lru_cache(None)
        def dp(index, height, width):
            if width < 0:
                return float('inf')
            if index == length:
                return height
            b_width, b_height = books[index]
            add_to_curr = dp(index+1, max(height, b_height), width - b_width)
            add_to_next = height + dp(index+1, b_height, shelf_width - b_width)
            return min(add_to_next, add_to_curr)

        length = len(books)
        return dp(0, 0, shelf_width)

s = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(s.minHeightShelves(books, shelf_width))