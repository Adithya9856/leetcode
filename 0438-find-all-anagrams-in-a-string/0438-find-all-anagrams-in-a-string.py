class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s)<len(p):
            return []
        result=[]
        p_map={}
        window={}
        for ch in p:
            p_map[ch]=p_map.get(ch,0)+1
        for ch in s[:len(p)]:
            window[ch]=window.get(ch,0)+1
        if p_map==window:
            result.append(0)
        left=0
        for right in range(len(p),len(s)):
            window[s[right]]=window.get(s[right],0)+1
            window[s[left]]-=1
            if window[s[left]]==0:
                del window[s[left]]
            left+=1
            if window==p_map:
                result.append(left)
        return result
