class Solution:
    def convertDateToBinary(self, date: str) -> str:
        ans=[]
        def DecimalToBinary(num):
            return bin(num).replace("0b", "")
        l=date.split("-")
        for i in l:
            ans.append(DecimalToBinary(int(i)))
        return "-".join(ans)

