class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      ct=0

      for i in nums:
        b=nums.count(i)
        if b==1:
          ct=i
      return ct
          