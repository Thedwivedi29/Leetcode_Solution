class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count_dict = {}
        ans=[]
        for item in nums:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1
        for item in nums:
            if item not in ans or ans.count(item) < 2:
                ans.append(item)
        nums[:] = ans

        return len(nums)