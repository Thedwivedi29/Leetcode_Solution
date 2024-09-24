class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s=sum(nums)
        a=set(nums)
        l=list(a)
        x=sum(l)
        return(x*2-s)