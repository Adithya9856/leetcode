class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len=len(words[0])
        total=len(words)
        wordfreq={}
        for word in words:
            wordfreq[word]=wordfreq.get(word,0)+1
        result=[]
        for i in range(word_len):
            left=i
            s_freq={}
            count=0
            for right in range(i,len(s)-word_len+1,word_len):
                word=s[right:right+word_len]
                if word in wordfreq:
                    s_freq[word]=s_freq.get(word,0)+1
                    count+=1
                    while s_freq[word]>wordfreq[word]:
                        left_word=s[left:left+word_len]
                        s_freq[left_word]-=1
                        left+=word_len
                        count-=1
                    if count==total:
                        result.append(left)
                else:
                    s_freq={}
                    left=right+word_len
                    count=0
        return result