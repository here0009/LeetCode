"""
Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

 

Example 1:

Input: S = "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: S = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: S = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: S = "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
 

Constraints:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-repeating-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        length = len(S) + 1
        res = 0
        dp = [[0]*length for _ in range(length)]
        for i in range(1, length):
            for j in range(1, length):
                if i != j:
                    flag = int(S[i-1] == S[j-1])
                    dp[i][j] += dp[i-1][j-1]*flag + flag
                    res = max(res, dp[i][j])
        # for row in dp:
        #     print(row)
        return res

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/longest-repeating-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def search(self, L: int, a: int, modulus: int, n: int, nums) -> str:
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # compute the hash of string S[:L]
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus
              
        # already seen hashes of strings of length L
        seen = {h} 
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus) 
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1
        
    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**24
        
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L - 1
               
        return left - 1


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/longest-repeating-substring/solution/zui-chang-zhong-fu-zi-chuan-by-leetcode-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def search(self, L: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            if tmp in seen:
                return start
            seen.add(tmp)
        return -1

    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, n, S) != -1:
                left = L + 1
            else:
                right = L - 1
        return left - 1


class Solution:
    def longestRepeatingSubstring(self, S: str) -> str:
        def check(n):
            visited = set()
            for i in range(length-n+1):
                tmp = S[i:i+n]
                if tmp in visited:
                    return True
                visited.add(tmp)
            return False

        length = len(S)
        left, right = 1, length
        while left < right:
            mid = (left + right)//2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left-1


class Solution:
    def longestRepeatingSubstring(self, S: str) -> str:
        def check(n):
            visited = set()
            for i in range(length-n+1):
                tmp = hash(S[i:i+n])
                if tmp in visited:
                    return True
                visited.add(tmp)
            return False

        length = len(S)
        left, right = 1, length
        while left < right:
            mid = (left + right)//2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left-1


class Solution:
    def longestRepeatingSubstring(self, S: str) -> str:
        def search(n):
            h = 0
            for i in range(mid):
                h = (h * a + nums[i]) % M
            seen = {h}
            aL = pow(a, mid, M)
            for start in range(1, length-n+1):
                h = (h * a - nums[start-1] * aL + nums[start+n-1]) % M
                if h in seen:
                    return True
                seen.add(h)
            return False

        length = len(S)
        nums = [ord(S[i]) - ord('a') for i in range(length)]
        a = 26
        M = 10**9 +7
        left, right = 1, length
        while left < right:
            mid = left + (right - left) // 2
            if search(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1

Slt = Solution()
S = "abcd"
print(Slt.longestRepeatingSubstring(S))
S = "abbaba"
print(Slt.longestRepeatingSubstring(S))
S = "aabcaabdaab"
print(Slt.longestRepeatingSubstring(S))
S = "aaaaa"
print(Slt.longestRepeatingSubstring(S))