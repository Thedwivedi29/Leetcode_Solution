class Solution:
    
    def isStrictlyPalindromic(self, n: int) -> bool:
        def convert(n,x):
            y=n
            s=""
            temp=""
            while(y!=0):
                r=y%x
                y=y//x
                temp=str(r)
                s=temp+s
            return s
        n=9
        for x in range(2,n-1):
            s=convert(n,x)
            if (s!=s[::-1]):
                return False