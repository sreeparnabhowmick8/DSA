class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,maxlen=0,0
        st=set()
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[left])
                left+=1
            st.add(s[i])
            maxlen=max(maxlen,i-left+1)
        return maxlen        


                   
        