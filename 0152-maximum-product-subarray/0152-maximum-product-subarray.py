class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin,curmax=1,1
        res=max(nums)
        for n in nums:
            if n==0:
                curmin,curmax=1,1
                continue
            temp=n*curmax
            curmax=max(n*curmax,n*curmin,n)
            curmin=min(temp,n*curmin,n)
            res=max(res,curmax)
        return res