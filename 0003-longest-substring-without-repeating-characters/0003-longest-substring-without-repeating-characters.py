class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        left=0
        lenght=0
        for right in range(len(s)):
            if s[right] in freq:
                left=max(left,freq[s[right]]+1)
            freq[s[right]]=right
            lenght=max(lenght,right-left+1)
        return lenght