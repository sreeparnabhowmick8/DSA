class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen,l,r=0,0,0
        zero_count=0
        n=len(nums)
        while(r<n):
            if(nums[r]==0):
                zero_count+=1
            while(zero_count>k):
                if(nums[l]==0):
                    zero_count-=1
                l+=1
            if(zero_count<=k):
                length=r-l+1
                maxlen=max(length,maxlen)
            else:
                break
            r+=1    
        return maxlen                        

        