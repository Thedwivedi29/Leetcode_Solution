class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        se,sd=0,0
        temp=0
        for i in nums:
            se=se+i
            while i>0:
                temp=i%10
                sd=sd+temp
                i=i//10
        return abs(se-sd)