class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderl=list(order)
        sl=list(s)
        dic={}
        temp=""
        x=[]
        for i in sl:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for i in orderl:
            if i in sl:
                temp=i*dic[i]
                x+=list(temp)
        for i in x:
            if i in sl:
                print(i)
                sl.remove(i)

        x=x+sl
        return "".join(x)

        