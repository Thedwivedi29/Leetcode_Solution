class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        move=0
        ans=[]
        students.sort()
        for i in range(0,len(seats)):
            move=students[i]-seats[i]
            ans.append(abs(move))
        s=sum(ans)
        return s