class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans=[]
        diff=[]
        for i in range(0,len(points)):
            ans.append(points[i][0])
        ans.sort()
        for i in range(0,len(ans)-1):
            diff.append(abs(ans[i]-ans[i+1]))
        return max(diff)
