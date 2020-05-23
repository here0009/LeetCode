class Solution(object):
    """
    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

    Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0
    Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5
    """
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_1 = len(nums1)
        len_2 = len(nums2)
        len_3 = len_1 + len_2
        median_num, odd = divmod(len_3,2) #remainder is 1, len_3 is odd
        # median_num += 1

        print(median_num, odd)
        i = 0
        j = 0
        nums3 = []
        while (i+j < len_3): #i+j is number of nums added to num3
            if i >= len_1:
                nums3.append(nums2[j])
                j+=1
            elif j >= len_2:
                nums3.append(nums1[i])
                i+=1
            elif nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1

        print(nums3)

        if odd:
            median = nums3[median_num]
        else:
            median = (nums3[median_num - 1] + nums3[median_num])/2

        print(median)
        return median
        
s = Solution()
s.findMedianSortedArrays([1,3],[2])
print("****************")
s.findMedianSortedArrays([1,2],[3,4])
s.findMedianSortedArrays([1,3,5,7,9],[2,4,6,8,10])