class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans=[0]*n
        xor=0
        for i in range(0,n):
            ans[i] = start + 2 * i

        for i in ans:
            xor=xor^i
        return xor