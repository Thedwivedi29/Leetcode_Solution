class Solution:
    def validStrings(self, n: int) -> List[str]:
        def convert(n,z):
            s=bin(n)
            s=s[2:]
            if len(s)<z:
                return "0"+s
            else:
                return s

        def check(x):
            c=0
            for i in range(0,len(x)-1):
                if x[i:i+2]!="00":
                    c=c+1
            if c==n-1:
                return x

        ans=[]
        start=int(pow(2,n-2))
        end=int(pow(2,n))
        for i in range(start,end):
            temp=convert(i,n)
            if check(temp):
                ans.append(temp)
        return ans

