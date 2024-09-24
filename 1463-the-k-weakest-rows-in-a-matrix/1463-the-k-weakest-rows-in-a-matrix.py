class Solution(object):
    def kWeakestRows(self, mat, k):
        x=[]
        r=[]
        for i in mat:
            occurrence = {item: i.count(item) for item in i}
            x.append(occurrence.get(1))
        for i in range(0,k):
            mi=min(x)
            r.append(x.index(mi))
            x[x.index(mi)]=max(x)+1
        return r

