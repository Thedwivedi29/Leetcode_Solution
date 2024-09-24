class Solution(object):
    def countNegatives(self, grid):
        nc=0
        for i in grid:
            count = sum(1 for item in i if item < 0)
            nc=nc+count
        return nc