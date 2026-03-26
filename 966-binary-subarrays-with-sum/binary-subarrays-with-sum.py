class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(nums,goal):
            l,r,sum1=0,0,0
            count=0
            n=len(nums)
            while(r<n):
                sum1+=nums[r]
                while(sum1>goal and l<=r):
                    sum1-=nums[l]
                    l+=1
                if(sum1<=goal):
                    count+=r-l+1
                r+=1    
            return count
        return helper(nums,goal)-helper(nums,goal-1)                

        