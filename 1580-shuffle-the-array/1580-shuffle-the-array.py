class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        x=nums[0:n]
        y=nums[n:len(nums)]
        for i in range(0,n):
            ans.append(x[i])
            ans.append(y[i])
        return ans
