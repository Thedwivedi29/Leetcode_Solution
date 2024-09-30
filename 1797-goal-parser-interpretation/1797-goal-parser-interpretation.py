class Solution:
    def interpret(self, s: str) -> str:
        result=[]
        i=0
        while i < len(s):
            if s[i] == "G":
                result.append("G")
                i += 1
            elif s[i:i+2] == "()":
                result.append("o")
                i += 2
            elif s[i:i+4] == "(al)":
                result.append("al")
                i += 4
        return "".join(result)