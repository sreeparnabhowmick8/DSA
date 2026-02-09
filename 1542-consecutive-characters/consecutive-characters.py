class Solution:
    def maxPower(self, s: str) -> int:
        # count,max1=0,0
        # same=" "
        # for i in s:
        #     if i!=same:
        #         count=1
        #         same=i
        #     same=i
        #     count+=1
        #     max1=max(max1,count)
        # return max1   
        ans,x=1,1
        for i in range(1,len(s)):
            if(s[i-1]==s[i]):
                x+=1
            else:
                ans=max(ans,x)
                x=1
        ans=max(ans,x)
        return ans                 
        