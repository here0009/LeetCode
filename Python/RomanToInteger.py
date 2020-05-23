

class Solution:

    def romanToInt(self, romanNumber):
        """
        :type s: str
        :rtype: int
        """
        # order_string = "IVXLCDM"
        def listToNum(input_list):
            """
            pop out all the elements in the list, convert to a number
            """
            total_num = 0
            while len(input_list) > 0:
                total_num += input_list.pop()
            return total_num

        romanSymbol = ['I','V', 'X', 'L', 'C', 'D', 'M']
        numbers = [1,5,10,50,100,500,1000]
        romanToIntDict = dict(zip(romanSymbol, numbers))
        symbolStack = list()
        result = 0
        for symbol in romanNumber:
            current_num = romanToIntDict[symbol]
            if len(symbolStack) == 0:
                symbolStack.append(current_num)
            else:
                pre_num = symbolStack[-1]
                if current_num == pre_num:
                    symbolStack.append(current_num)
                elif current_num < pre_num:
                    result += listToNum(symbolStack)
                    symbolStack.append(current_num)
                else:
                    tmp_num = listToNum(symbolStack)
                    result -= tmp_num
                    symbolStack.append(current_num)
        result += listToNum(symbolStack)
        return result



        

s = Solution()
roman_strings = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
roman_strings_2 = ["IV", "IX"]
for roman_string in roman_strings:
    print(s.romanToInt(roman_string))