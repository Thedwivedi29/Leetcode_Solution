class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec=list(nums)
        inc=list(nums)
        incr=0
        decr=0
        inc.sort()
        dec.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i]==inc[i]:
                incr=incr+1
            if nums[i]==dec[i]:
                decr=decr+1
        if incr==len(nums) or decr==len(nums):
            return True
        else:
            return False