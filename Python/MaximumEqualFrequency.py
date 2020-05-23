"""
Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.

If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).

 

Example 1:

Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
Example 2:

Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13
Example 3:

Input: nums = [1,1,1,2,2,2]
Output: 5
Example 4:

Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
Output: 8
 

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
from collections import Counter
class Solution_1:
    def maxEqualFreq(self, nums) -> int:
        def check(counter):
            print(counter)
            if len(counter) == 1:
                return True
            val_counter = Counter(counter.values())
            print('val_counter', val_counter)
            if len(val_counter) == 1:
                for key in val_counter.keys():
                    return key == 1
            elif len(val_counter) == 2:
                val_counter_list = sorted(val_counter.keys())
                p,q = val_counter_list
                # p,q = val_counter.keys()
                return (val_counter[q] == 1 and  q-p == 1) or (p == 1 or q == 1)
                # return (val_counter[q] == 1 or val_counter[q] == 1)  or abs(val_counter[q] - val_counter[q]) == 1
            return False

        counter_nums = Counter(nums)
        res = len(nums)
        if check(counter_nums):
            return res
        while res > 2:
            res -= 1
            num = nums[res]
            counter_nums[num] -= 1 #remvoe frome end
            if counter_nums[num] == 0:
                del counter_nums[num]
            print(res)
            if check(counter_nums):
                return res
        return res


from collections import Counter
class Solution:
    def maxEqualFreq(self, nums) -> int:
        def check(counter_vals):
            if len(counter_vals) == 1:
                return index+1 #the removed value was previous value
            elif len(counter_vals) == 2:
                p,q = counter_vals.keys()
                if p < q:
                    p,q = q,p
                vp,vq = counter_vals[p], counter_vals[q]
                if (p-q == 1 and vp == 1) or (q == 1 and vq == 1) : #p-q == 1 and vp == 1, delete one p, others will be equal; q == 1 and vq == 1, delete q, others will be eaqual.
                    return index
            return 0

        counter_nums = Counter(nums)
        counter_vals = Counter(counter_nums.values())
        index = len(nums)
        k = check(counter_vals)
        if k != 0 and k != index + 1:
            # print(k,index)
            return k
        while index > 1:
            index -= 1
            num = nums[index]
            counter_nums[num] -= 1
            if counter_nums[num] == 0:
                del counter_nums[num]
            counter_vals = Counter(counter_nums.values())
            k = check(counter_vals)
            if k != 0:
                return k
        return index+1


s = Solution()
nums = [2,2,1,1,5,3,3,5]
print(s.maxEqualFreq(nums))

nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
print(s.maxEqualFreq(nums))

nums = [1,1,1,2,2,2]
print(s.maxEqualFreq(nums))

nums = [10,2,8,9,3,8,1,5,2,3,7,6]
print(s.maxEqualFreq(nums))

nums = [1,2]
print(s.maxEqualFreq(nums))

nums = [1,2,3,4,5,6,7,8,9]
print(s.maxEqualFreq(nums))

nums = [1,1]
print(s.maxEqualFreq(nums))

nums = [1,1,1,1,1,1]
print(s.maxEqualFreq(nums))

nums = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,65,75,39,10,58,47,97,29,62,77,49,1,18,22,6,73,16,4,11,78,70,81,86,89,45,24,64,56,98,4,72,94,81,90,25,93,83,42,3,28,77,78,100,54,73,86,31,2,48,19,21,90,35,8,48,71,87,23,87,3,44,96,33,51,22,22,36,20,94,86,26,15,17,52,2,21,32,70,42,32,52,74,25,44,89,30,71,96,1,80]
print(s.maxEqualFreq(nums))
# Output:
# 39
# Expected:
# 37

nums = [1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800]
# print(s.maxEqualFreq(nums))