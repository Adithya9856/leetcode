class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        left=0
        lenght=0
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right],0)+1
            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            lenght=max(lenght,right-left+1)
        return lenght