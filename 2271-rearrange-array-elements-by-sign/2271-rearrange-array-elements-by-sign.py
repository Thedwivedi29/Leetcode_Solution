class Solution(object):
    def rearrangeArray(self, nums):
        n=[i for i in nums if i<0]
        p=[i for i in nums if i>0]
        r=[]
        pl=len(p)
        nl=len(n)
        for i in range(nl):
            r.append(p[i])
            r.append(n[i])
        return r
        