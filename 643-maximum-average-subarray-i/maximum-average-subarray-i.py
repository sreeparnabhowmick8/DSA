class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r,count=0,0,0
        sum1=0
        n=len(nums)
        maxavg=float('-inf')
        while(r<n):
            sum1+=nums[r]
            count+=1
            if(k==count):
                avg=sum1/k
                maxavg=max(avg,maxavg)
                sum1-=nums[l]
                l+=1
                count-=1
            r+=1
        return float(maxavg)        
        