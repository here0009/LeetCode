from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text):
        text_counter = Counter(text)
        balloon = Counter('balloon')
        # for s in balloons.keys():
        #     if s in text_counter:
        #         res.append(text_counter[s]//balloons[s])
        #     else:
        #         res.append(0)
        # return min(res)
        # print(text_counter)
        # print(balloon)
        # print([text_counter[s]//balloon[s] if s in text_counter else 0 for s in balloon])
        return min([text_counter[s]//balloon[s] if s in text_counter else 0 for s in balloon])

s = Solution()
text = "nlaebolko"
print(s.maxNumberOfBalloons(text))
text = "loonbalxballpoon"
print(s.maxNumberOfBalloons(text))
text = "leetcode"
print(s.maxNumberOfBalloons(text))
