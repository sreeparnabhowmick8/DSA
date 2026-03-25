class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc=[-1,-1,-1]
        count,right=0,0
        while(right<len(s)):
            abc[ord(s[right])-ord('a')]=right
            minindex=min(abc)
            count+=(minindex+1)
            right+=1
        return count                
        