class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        l=len(nums)
        sum=0
        for i in range(0,l):
            b=bin(i).replace("0b", "")
            if b.count("1")==k:
                sum+=nums[i]
        return sum