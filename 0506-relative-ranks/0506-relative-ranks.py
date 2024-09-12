class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rscore=sorted(score,reverse=True)
        ans=[]
        d={}
        for i in range(0,len(rscore)):
            if i==0:
                d[rscore[i]]="Gold Medal"
            elif i==1:
                d[rscore[i]]="Silver Medal"
            elif i==2:
                d[rscore[i]]="Bronze Medal"
            else:
                d[rscore[i]]=str(i+1)

        for i in range(len(score)):
            ans.append(d[score[i]])
        return ans
