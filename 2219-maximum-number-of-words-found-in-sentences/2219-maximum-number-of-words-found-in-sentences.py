class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans=[]
        for i in sentences:
            l=i.split(" ")
            ans.append(len(l))
        return max(ans)