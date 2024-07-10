class Solution(object):
    def longestCommonPrefix(self, strs):
        r=""
        ma=len(max(strs))
        k=""
        for y in strs:
            m=len(y)
            if ma>=m:
                ma=m
                k=y
        for x in range(0,len(k)):
            c=0
            for i in strs:
                p=strs[0][x]
                if (p==i[x]):
                    c=c+1
                else:
                    break
            if c==len(strs):
                r=r+p
            elif (len(strs)==1):
                r=strs[0]
            else:
                break
        return r 
