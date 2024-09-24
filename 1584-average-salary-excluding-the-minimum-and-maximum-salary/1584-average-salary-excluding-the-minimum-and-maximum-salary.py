class Solution(object):
    def average(self, salary):
        avg=0
        float(avg)
        mi=min(salary)
        ma=max(salary)
        salary.remove(mi)
        salary.remove(ma)
        avg=float(sum(salary))/float(len(salary))
        return avg