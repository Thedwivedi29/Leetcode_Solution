class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res=nums1+nums2
        res.sort()
        l=len(res)
        mid=l//2
        if l%2==1:
            return float(res[mid])
        else:
            return(float(res[mid-1])+float(res[mid]))/2