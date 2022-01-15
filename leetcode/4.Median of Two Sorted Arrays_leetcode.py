"""
4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sumlist=list()
        sumlist.append(nums1)
        sumlist.append(nums2)
        sumlist=sum(sumlist,[])
        sumlist.sort()
        ## 인덱스가 홀수 
        if len(sumlist)%2!=0:
            result=sumlist[len(sumlist)/2]
        ## 인덱스가 짝수
        else:
            result=float(sumlist[len(sumlist)/2]+sumlist[len(sumlist)/2-1])/2
        return result
    
    #123456