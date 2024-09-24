class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        s1,s2=[],[]
        for i in range(1,n+1):
            if i%m==0:
                s1.append(i)
            else:
                s2.append(i)
        return sum(s2)-sum(s1)