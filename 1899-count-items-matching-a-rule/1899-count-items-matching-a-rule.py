class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        c=0
        if ruleKey=="type":
            x=0
        elif ruleKey=="color":
            x=1
        elif ruleKey=="name":
            x=2

        for i in items:
            if i[x]==ruleValue:
                c=c+1
        return c