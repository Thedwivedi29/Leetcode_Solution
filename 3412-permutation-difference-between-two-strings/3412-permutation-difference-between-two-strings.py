class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans=0
        for i in s:
            ans+=abs(t.index(i)-s.index(i))
        return ans