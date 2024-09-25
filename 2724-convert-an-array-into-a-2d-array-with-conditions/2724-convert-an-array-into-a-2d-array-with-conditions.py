class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        while(len(nums)!=0):
            ans.append(list(set(nums)))
            for i in list(set(nums)):
                nums.remove(i)
        return ans