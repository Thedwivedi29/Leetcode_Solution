class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        dic={}
        ans=[]
        temp=list(set(nums))
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in temp:
            if dic[i]==2:
                ans.append(i)
        return ans