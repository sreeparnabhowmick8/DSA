class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=defaultdict(int)
        res=0
        for i in s:
            count[i]+=1
            if(count[i]%2==0):
                res+=2
        for i in count.values():
            if i%2==1:
                res+=1
                break
        return res                

        