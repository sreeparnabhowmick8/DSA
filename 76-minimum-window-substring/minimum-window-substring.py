class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        map = [0] * 128
        count = len(t)
        l = 0
        r = 0
        min_len = float('inf')
        start_index = 0
        for i in t:
            map[ord(i)]+=1
        while(r<len(s)):
            if map[ord(s[r])]>0:
                count-=1
            map[ord(s[r])]-=1
            r+=1
            while count==0:
                if r-l<min_len:
                    start_index=l
                    min_len=r-l
                if map[ord(s[l])]==0:
                    count+=1
                map[ord(s[l])]+=1
                l+=1
        return "" if min_len==float('inf') else s[start_index:start_index+min_len]            



        