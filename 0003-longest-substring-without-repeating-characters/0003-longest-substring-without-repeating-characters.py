class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        freq = {}
        max_length = 0
        start = 0

        for i, char in enumerate(s):
            if char in freq:
                start = max(start, freq[char] + 1)

            freq[char] = i
            max_length = max(max_length, i - start + 1)

        return max_length