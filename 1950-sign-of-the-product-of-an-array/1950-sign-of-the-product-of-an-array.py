class Solution(object):
    def arraySign(self, nums):
        p=1
        for i in nums:
            p=p*i
        return (p>0)-(p<0)