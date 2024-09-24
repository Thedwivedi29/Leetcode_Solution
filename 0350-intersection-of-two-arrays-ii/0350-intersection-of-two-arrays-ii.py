class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1)>len(nums2):
            temp=nums2
            ans=[]
            for i in nums1:
                if i in temp:
                    ans.append(i)
                    temp.remove(i)
        else:
            temp=nums1
            ans=[]
            for i in nums2:
                if i in temp:
                    ans.append(i)
                    temp.remove(i)
        return ans