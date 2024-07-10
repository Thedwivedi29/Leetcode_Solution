class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff=[]
        s=0
        for i in range(len(prices)-1):
            diff.append(prices[i+1]-prices[i])
        for i in diff:
            if i>0:
                s=s+i
        return s