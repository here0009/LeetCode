class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter_list = list("abcdefghijklmnopqrstuvwxyz")
        morseCode_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter_morseCode_dict = dict(zip(letter_list, morseCode_list))
        uniqueMorese = set()
        for word in words:
            uniqueMorese.add("".join([letter_morseCode_dict[s] for s in word]))
        return len(uniqueMorese)

s = Solution()
words = ["gin", "zen", "gig", "msg"]
print(s.uniqueMorseRepresentations(words))