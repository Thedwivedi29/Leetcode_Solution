class Solution:
    def defangIPaddr(self, address: str) -> str:
        l=list(address)
        for i in l:
            if i=='.':
                l[l.index(i)]='[.]'
        str="".join(l)
        return str