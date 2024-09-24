class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls=list(s)
        lt=list(t)
        c=0
        x=0
        for i in ls:
            if i in lt[x:]:
                lt=lt[x:]
                x=lt.index(i)
                lt.remove(i)
                c=c+1
                print(i,x)
        if c==len(s):
            return True
        else:
            return False
