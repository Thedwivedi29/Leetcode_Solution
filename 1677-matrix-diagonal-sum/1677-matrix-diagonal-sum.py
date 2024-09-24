class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        temp=[]
        c=int((len(mat)-1)/2)
        for i in range(0,len(mat)):
            temp.append(mat[i][i])
            temp.append(mat[i][(len(mat)-1)-i])
        if len(mat)%2!=0:
            temp.remove(mat[c][c])
        res=list(temp)
        return sum(res)