class Solution(object):
    def twoSum(self, nums, target):
        l=[]
        p=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                x=nums[i]+nums[j]
                if x==target:
                    p=1
                    break
            if p==1:
                break
        l.append(i)
        l.append(j)
        return l
