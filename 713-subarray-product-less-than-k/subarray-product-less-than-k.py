class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l,r,pro=0,0,1
        n=len(nums)
        count=0
        while(r<n):
            pro*=nums[r]
            while(pro>=k and l<r):
                pro//=nums[l]
                l+=1    
            if(pro<k):
                count+=(r-l+1)
            r+=1    
        return count        


        