class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[0]*len(nums)
        rightsum=[0]*len(nums)
        ans=[]
        sum=0
        for i in range(0,len(nums)):
            leftsum[i]=sum
            sum=sum+nums[i]
        # print(leftsum)
        sum=0
        for i in range(len(nums)-1,-1,-1):
            rightsum[i]=sum
            sum=sum+nums[i]
        for i in range(0,len(nums)):
            ans.append(abs(leftsum[i]-rightsum[i]))
        return ans