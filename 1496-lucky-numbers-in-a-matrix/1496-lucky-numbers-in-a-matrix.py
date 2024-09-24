class Solution(object):
    def luckyNumbers (self, matrix):
        minrow = {min(r) for r in matrix}
        maxcol = {max(c) for c in zip(*matrix)}
        return list(minrow & maxcol)
