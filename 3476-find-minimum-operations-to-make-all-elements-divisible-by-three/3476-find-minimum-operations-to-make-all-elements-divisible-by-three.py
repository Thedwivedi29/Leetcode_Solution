class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for n in nums:
            if (n-1)%3==0 or (n+1)%3==0:
                c=c+1

        return c

