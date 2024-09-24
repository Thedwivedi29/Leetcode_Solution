class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for n in operations:
            if n=="X++" or n=="++X":
                x=x+1
            elif n=="--X"or n=="X--":
                x=x-1
        return x