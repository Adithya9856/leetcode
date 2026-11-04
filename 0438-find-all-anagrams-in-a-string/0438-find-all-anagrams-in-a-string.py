class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s)<len(p):
            return []
        result=[]
        p_map=[0]*26
        window=[0]*26
        for ch in p:
            p_map[ord(ch)-ord("a")]+=1
        for ch in s[:len(p)]:
            window[ord(ch)-ord("a")]+=1
        if p_map==window:
            result.append(0)
        left=0
        for right in range(len(p),len(s)):
            window[ord(s[right])-ord("a")]+=1
            window[ord(s[left])-ord("a")]-=1
            left+=1
            if window==p_map:
                result.append(left)
        return result
