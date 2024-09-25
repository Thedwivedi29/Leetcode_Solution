class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        while(len(nums)!=0):
            s=set(nums)
            l=list(s)
            ans.append(l)
            for i in l:
                nums.remove(i)
        return ans