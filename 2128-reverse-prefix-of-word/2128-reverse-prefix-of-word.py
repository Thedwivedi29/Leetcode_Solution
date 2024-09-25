class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        x=0
        for i in word:
            if ch == i:
                x=word.index(i)
                return word[x::-1]+word[x+1:]
        return word