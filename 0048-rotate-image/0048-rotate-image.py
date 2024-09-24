class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix)
        for i in range(0,l//2):
            for j in range(i,l-i-1):
                matrix[i][j],matrix[j][l-1-i]=matrix[j][l-1-i],matrix[i][j]
                matrix[i][j],matrix[l-1-i][l-1-j]=matrix[l-1-i][l-1-j],matrix[i][j]
                matrix[i][j],matrix[l-1-j][i]=matrix[l-1-j][i],matrix[i][j]
