class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans=[bool(0)]*len(candies)
        maax=max(candies)
        for j in range(0,len(candies)):
            if candies[j]+extraCandies>=max(candies) :
                ans[j]=bool(candies[j]+extraCandies>=max(candies))
        return ans