class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderl=list(order)
        sl=list(s)
        dic={}
        x=[]
        for i in sl:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for i in orderl:
            if i in sl:
                for j in range(0,dic[i]):
                    x.append(i)
                    sl.remove(i)
        x=x+sl
        return "".join(x)

        