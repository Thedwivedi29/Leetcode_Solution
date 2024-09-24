class Solution(object):
    def runningSum(self, nums):
        r=[]
        s=0
        for i in nums:
            s=s+i
            r.append(s)
        return r
