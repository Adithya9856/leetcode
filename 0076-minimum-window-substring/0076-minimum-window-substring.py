class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map={}
        for ch in t:
            t_map[ch]=t_map.get(ch,0)+1
        left=0
        s_map={}
        min_len=float("inf")
        count=len(t)
        ans=""
        for right in range(len(s)):
            s_map[s[right]]=s_map.get(s[right],0)+1
            
            if s[right] in t_map and s_map[s[right]]<=t_map[s[right]]:
                count-=1
            while count==0:
                if right-left+1<min_len:
                    min_len=right-left+1
                    ans=s[left:right+1]
                s_map[s[left]]-=1
                if s[left] in t_map and s_map[s[left]] < t_map[s[left]]:
                    count+=1
                left+=1
        return ans
                
