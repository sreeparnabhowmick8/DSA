class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if(n==k):
            return sum(cardPoints)
        l_sum,maxsum=0,0
        r_sum=0
        for i in range(k):
            l_sum+=cardPoints[i]
            maxsum=max(maxsum,l_sum)
        r_len=n-1
        for i in range(k-1,-1,-1):
            l_sum-=cardPoints[i]
            r_sum+=cardPoints[r_len]
            r_len-=1
            maxsum=max(maxsum,(l_sum+r_sum))  
        return maxsum      

        