class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target=[]*len(nums)
        for i in range(0,len(nums)):
            target.insert(index[i],nums[i])
        return target