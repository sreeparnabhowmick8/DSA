class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        best=nums[0]+nums[1]+nums[2] # Start with any valid triple
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:# Optional optimization: skip duplicate first elements
                continue
            l=i+1
            r=n-1
            while(l<r):
                sum1=nums[i]+nums[l]+nums[r]
                if(abs(sum1-target)<abs(best-target)):# Update best if this sum is closer
                    best=sum1
                # Move pointers to get closer to target    
                if(sum1<target):
                    l+=1
                elif(sum1>target):
                    r-=1
                else:
                    return sum1    # exact match is the closest possible
        return best                    

        