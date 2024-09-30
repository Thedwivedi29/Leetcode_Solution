class Solution:
    def groupThePeople(self, s: List[int]) -> List[List[int]]:
        r = []
        m = {}

        for i, g in enumerate(s):
            if g not in m:
                m[g]=[]
            m[g].append(i)

            if len(m[g])==g:
                r.append(m[g])
                m[g]=[]
        return r