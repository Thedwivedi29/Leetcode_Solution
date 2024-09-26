class Solution:

    def minimumAverage(self, nums: List[int]) -> float:
        avg=[]
        while(nums!=[]):
            ma=max(nums)
            nums.remove(ma)
            mi=min(nums)
            nums.remove(mi)
            avg.append((ma+mi)/2)
        return min(avg)