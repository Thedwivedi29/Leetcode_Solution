class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l1=""
        l2=""
        for i in word1:
            l1=l1+i
        for i in word2:
            l2=l2+i
        if len(l1)==len(l2):
            for i in range(len(l1)):
                if l1[i]!=l2[i]:
                    return bool(0)
            return bool(1)
        return bool(0)
