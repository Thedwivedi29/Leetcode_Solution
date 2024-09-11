class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count=0
        startbin=bin(start).replace("0b","")
        goalbin=bin(goal).replace("0b","")
        startbin=list(startbin)
        goalbin=list(goalbin)
        if len(startbin)>len(goalbin):
            x=len(startbin)-len(goalbin)
            for i in range(0,x):
                goalbin.insert(0,"0")
        elif len(startbin)<len(goalbin):
            x=len(goalbin)-len(startbin)
            for i in range(0,x):
                startbin.insert(0,"0")
        # print(startbin,goalbin)
        for i in range(0,len(startbin)):
            if startbin[i]==goalbin[i]:  
                continue
            elif startbin[i]!=goalbin[i]:
                # print(startbin[i],".............",goalbin[i])
                goalbin[i]=startbin[i]
                # print(startbin[i],".............",goalbin[i])
                count+=1

        return count