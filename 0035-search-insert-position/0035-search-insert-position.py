class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        if nums[-1]<target :
            return len(nums)
        else:
            for i in nums:
                if i >target:
                    break
            return nums.index(i)
