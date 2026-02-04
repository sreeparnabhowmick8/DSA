class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,max1=0,0
        st=set()
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            max1=max(max1,right-left+1)
        return max1         

                   
        