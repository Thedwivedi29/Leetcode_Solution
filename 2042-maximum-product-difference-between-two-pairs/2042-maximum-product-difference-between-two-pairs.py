class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        pair1,pair2=[],[]
        pair2[:]=nums[0:2]
        pair1[:]=nums[len(nums)-2:]
        i=0
        return (pair1[i]*pair1[i+1])-(pair2[i]*pair2[i+1])