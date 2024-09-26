class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        alice=0
        bob=0
        while(len(nums)!=0):
            alice=min(nums)
            nums.remove(alice)
            bob=min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(alice)
        return arr