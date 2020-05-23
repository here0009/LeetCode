class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output_list = []
        for i in range(1, n+1):
            if i%15 == 0 :
                letter = "FizzBuzz"
            elif i%3 == 0:
                letter = "Fizz"
            elif i%5 == 0:
                letter = "Buzz"
            else:
                letter = str(i)
            output_list.append(letter)
        return output_list

s = Solution()
print(s.fizzBuzz(30))
